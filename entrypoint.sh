#!/bin/bash
echo "Start running security test suite..."

/usr/bin/syntribos --config-file ${config_file_location} --no_colorize run > /mount-opt/syntribos_run/${MY_JOB_NAME}_$(date +%d-%b-%H_%M)_result.txt 2>&1

echo "End run."