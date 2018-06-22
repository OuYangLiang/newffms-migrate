#!/bin/bash

$1 -u $3 -p$4 <<EOF
    create database $5;
EOF