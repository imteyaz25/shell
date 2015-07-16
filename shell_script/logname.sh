AH_SITE_ENVIRONMENT=dev
#export AH_SITE_ENVIRONMENT

lname=$(who am i)
llname=($lname)
LOGNAME=$llname
export LOGNAME

if [ "$LOGNAME" == "iahmad" ]
then
  AH_SITE_ENVIRONMENT=yahoo
  export AH_SITE_ENVIRONMENT
elif [ "$LOGNAME" == "test-stage" ]
then
  AH_SITE_ENVIRONMENT=google
  export AH_SITE_ENVIRONMENT
fi
echo $AH_SITE_ENVIRONMENT
