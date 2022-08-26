#!/bin/bash
  
BACKUPDIR=$1
ZIPTYPE=$2
BACKUPNAME=$3


{
tar --overwrite -cvf $BACKUPDIR/$BACKUPNAME.tar /home
$ZIPTYPE -f $BACKUPDIR/$BACKUPNAME.tar | openssl enc -aes-256-cbc -out $BACKUPNAME.dat
} 1>/dev/null 2>>error.log

