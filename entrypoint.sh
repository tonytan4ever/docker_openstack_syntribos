#!/bin/bash
echo "Start running security test suite..."


export REPORT_FILE_NAME = ${MY_JOB_NAME}_$(date +%d-%b-%H_%M)_report.html
/usr/bin/syntribos --config-file ${config_file_location} --no_colorize --report_outfile /mount-opt/syntribos_report/${REPORT_FILE_NAME}.html run > /mount-opt/syntribos_run/${MY_JOB_NAME}_$(date +%d-%b-%H_%M)_result.txt 2>&1
./root/send_report_email.py -s ${SMTP_EMAIL_SERVER} -u ${SMTP_USER} -p ${SMTP_PASSWORD} -f ${FROM_EMAIL} -t ${TO_EMAIL} -r /mount-opt/syntribos_report/${REPORT_FILE_NAME}.html

echo "End run."