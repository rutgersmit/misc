#!/bin/bash

declare -A email;
email['subject']=$1
email['from']='rutger@rutgersmit.com'
email['to']='rutger@rutgersmit.com'
email['host']='192.168.100.10'

email_content='From: '"${email['from']}"'
To: '"${email['to']}"'
Subject: '"${email['subject']}"'
Date: '"$(date)"'
'$2'
';


echo "$email_content" | curl -s \
    --url "smtp://${email['host']}" \
    --mail-from "${email['from']}" \
    --mail-rcpt "${email['to']}" \
    --upload-file - # email.txt

if [[ $? == 0 ]]; then
    echo 'okay';
else
    echo "curl error code $?";
    man curl | grep "^ \+$? \+"
fi

