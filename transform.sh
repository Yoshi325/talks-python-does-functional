#!/bin/bash

set -e

[ -n "$(command -v pandoc)" ] || (echo "pandoc is required for this script" && exit 1)
[ -n "$(command -v sed)"    ]    || (echo "sed is required for this script"    && exit 1)
[ -n "$(command -v tidy)"   ]   || (echo "tidy is required for this script"   && exit 1)

echo "Copying outline for building..."
cp -v outline.rst built-outline.rst

echo "Processing .. include:: shim for pandoc..."
python -u ./include-shim-for-pandoc.py built-outline.rst

echo "Converting to reveal.js presentation..."
pandoc \
    built-outline.rst \
    --read=rst \
    --write=revealjs \
    --slide-level 1 \
    --variable theme="black" \
    --variable transition="fade" \
    --variable center="false" \
    --standalone \
  | tidy \
        -indent \
        -wrap 0 \
        -quiet \
        --doctype html5  \
        --indent-spaces 4 \
  | sed '/<\/head>/i \
            <style>   \
                .reveal .slides section .fragment.current-visible.current-fragment.collapsable-fragment { display: initial; } \
                .reveal .slides section .fragment.current-visible.collapsable-fragment { display: none; } \
                h1.subtitle { font-size: 2em; } \
                .code { text-align: left; } \
                .reveal dd > p { margin: 0; } \
                figure, img { border:none !important; outline: none !important; } \
                li { white-space: nowrap; } \
                section#history div.fragment { text-align: left; } \
                .reveal { font-size: 38px; } \
            </style>  \
    ' \
  > index.html \
;

PDF_FILENAME="$(basename $(pwd)).pdf"
echo "Converting to pdf (via latex): ${PDF_FILENAME}..."
pandoc \
    built-outline.rst \
    --read=rst \
    --write=beamer \
    --slide-level 1 \
    --standalone \
    --output="${PDF_FILENAME}" \
;

echo "Removing built outline..."
rm -v built-outline.rst