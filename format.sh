#!/usr/bin/env bash
# Checks and formats input python files according to strict set of rules.
#
# Formatting, generally, does not change AST of input programm, but rather
# aims to change code style and overall appearance to a developer for maintain
# consistensy throughout project life.
#
# For this, we utilize power of wide-used python formatters, like Black
# (https://github.com/psf/black) and Isort
# (https://github.com/timothycrosley/isort). Note, that formatter assumes code
# src top-level __init__.py file to declate some consts values. Specifically,
# maximum line width.

# https://sipb.mit.edu/doc/safe-shell/
set -euf -o pipefail

# Consts
OK_CODE=0
ERROR_CODE=1
BLACK=black
ISORT=isort

# ----------------------------------- Args -----------------------------------

help() {
  cat <<EOF
Usage: ./$(basename $0) [--files=FILES] [--fix] [--src_dir=SRC_DIR] \
[--help]

  Python code formatter.

Options:
  --files FILES         Scope (dir or file) of files to operate within.
                        [default: . (Current directory)]
  --fix                 True if try to fix errors in-place. [default: False]
  --src_dir SRD_DIR     Code source directory to fetch project consts from.
                        [default: Autodetect based on projet structure]
  --help                Show this message and exit.
EOF
}

src_dir=""
files="."
fix=false

while (("$#")); do
  case "$1" in
  --files)
    files="$2"
    shift
    ;;
  --files=*)
    files="${1#*=}"
    ;;
  --fix)
    fix=true
    ;;
  --src_dir)
    src_dir="$2"
    shift
    ;;
  --src_dir=*)
    src_dir="${1#*=}"
    ;;
  --help)
    help
    exit "${OK_CODE}"
    ;;
  *)
    help
    exit "${ERROR_CODE}"
    ;;
  esac
  shift
done

if [ -z "${src_dir}" ]; then
  # Output list of __init__.py files within one depth distance from root.
  src_dir=$(
    find . -mindepth 2 -maxdepth 2 -type f -name __init__.py -print -quit
  )
  if [ -z "${src_dir}" ]; then
    echo "Failed to find src code directory automatically."
    exit "${ERROR_CODE}"
  fi
  src_dir=$(dirname "${src_dir}")
fi

# ---------------------------------- Black -----------------------------------

has_command() {
  if command -v $1 >/dev/null 2>&1; then
    true
  else
    false
  fi
}

get_const() {
  value=$(awk -F "=" "/__$1__/ {print \$2}" "${src_dir}/__init__.py")
  # shellcheck disable=SC2001
  value=$(echo ${value} | sed 's/ *$//g') # Trim spaces around.
  echo $value
}

if ! has_command "${BLACK}"; then
  echo "${BLACK} is not found."
  exit "${ERROR_CODE}"
fi

line_width=$(get_const line_width)

black_flags="--skip-string-normalization --line-length=${line_width}"
if ! "${fix}"; then
  black_flags="${black_flags} --check --diff"
fi
black_flags="${black_flags} ${files}"

printf "Executing:\n${BLACK} %s\n" "${black_flags}"
${BLACK} ${black_flags}

# ---------------------------------- Isort -----------------------------------

if ! has_command "${ISORT}"; then
  echo "${ISORT} is not found."
  exit "${ERROR_CODE}"
fi

isort_flags="--line-width=${line_width}"
if ! "${fix}"; then
  isort_flags="${isort_flags} --check-only --diff"
fi
isort_flags="${isort_flags} -rc ${files}"

printf "Executing:\n${ISORT} %s\n" "${isort_flags}"
${ISORT} ${isort_flags}
