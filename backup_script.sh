#!/usr/bin/env bash

#set termination conditions
set -euo pipefail 

{
#Check the numbers of inputs and their validity: -d - the directory to backup; -a - the compression algorithm to use; -o - the output file name
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -d|--dir)
            input_dir="$2";
            shift;;
        -a|--algorithm)
            algorithm="$2";
            shift;;
        -o|--output)
            output_name="$2";
            shift;;
        *)
            echo "Unknown parameter passed: $1" >&2;
            exit 1;;
    esac
    shift
done

#Set the compression algorithm to use for tar command
case $algorithm in
  gzip)
    algo="--gzip";;
  bzip|bzip2)
    algo="--bzip2";;
  xz)
    algo="--xz";;
  lza)
    algo="--compress";;
  lzip)
    algo="--lzip";;
  lzma)
    algo="--lzma";;
  zstd)
    algo="--zstd";;
  *)
    algo="";;
esac

#Check the directory is existed
if [ ! -d "$input_dir" ]; then
    echo "Directory does not exist: ${input_dir}" >&2
    exit 1
fi

tar cfv - $algo $input_dir | openssl enc -e -aes-256-cbc -out "${output_name}.dat"
} 1>/dev/null 2>>error.log
