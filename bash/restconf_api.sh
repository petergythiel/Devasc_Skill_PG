#!/bin/bash
echo "Datum /tijd is: `date`"
#bij declaratie van variabelen: geen spatie voor of na '=' teken
IP_HOST="192.168.56.101"
RESTCONF_USERNAME="cisco"
RESTCONF_PASSWORD="cisco123!"
DATA_FORMAT="application/yang-data+json"
LOOPBACK_INTERFACE="Loopback199"
LOOPBACK_IP="10.1.99.1"
#echo "de parameters starten met IP_hosts"
#echo $IP_HOST
#echo $RESTCONF_USERNAME
#echo $RESTCONF_PASSWORD

DATA_FORMAT="application/yang-data+json"
LOOPBACK_INTERFACE="Loopback199"
LOOPBACK_IP="10.1.99.1"

#api_url_put=f"https://{IP_HOST}/restconf/data/ietf-interfaces:interfaces/interface={LOOPBACK_INTERFACE}"
#api_url_get=f"https://{IP_HOST}/restconf/data/ietf-interfaces:interfaces"
headers='{ "Accept": $DATA_FORMAT ,  "Content-type": $DATA_FORMAT }'
basicauth='($RESTCONF_USERNAME, $RESTCONF_PASSWORD)'
yangConfig='{
  "ietf-interfaces:interface": {
        "name": $LOOPBACK_INTERFACE,
        "description": f"RESTCONF => {$LOOPBACK_INTERFACE}",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": $LOOPBACK_IP,
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}'
#echo $DATA_FORMAT
#echo "Yang config is $yangConfig"
#echo "Headers zijn $headers"
#echo " Basic aut is  $basicauth"


echo "START REST API CALL"
echo "===================="
echo "FIRST API CALL"
#curl -i -k -X "OPTIONS" "https://192.168.56.101:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity" -H 'Accept: application/yang-data+json' -u 'cisco:cisco'
url_put=https://$IP_HOST/restconf/data/ietf-interfaces:interfaces/interface=$LOOPBACK_INTERFACE
##echo "url_put is $url_put"
#curl -k  https://$IP_HOST/restconf/data/ietf-interfaces:interfaces/interface=$LOOPBACK_INTERFACE
#curl -i -k $url >xx

#echo "###########test result1 start###############"
result1=$(curl -i -k -X PUT \
    -H "Accept: $DATAFORMAT" \
    -H "Content-type: $DATAFORMAT" \
    -u "${RESTCONF_USERNAME}:${RESTCONF_PASSWORD}" \
    -d  '$yangConfig' \
        $url_put )


#echo "##################"
#echo "STATUS bepaling"
#echo "##################"
status=`echo $result1 | grep HTTP |cut -d " " -f2`
#echo "Result1 is $result1"
#echo "De status is $status"

#echo "###########test result1 - PUT stop###############"


if [[ ${status} -ge 200 &&  ${status} -le  300 ]]
then
    echo "-------"
    echo "STATUS OK: $status"
    echo "-------"
else
 #   echo "-------"
    echo "Error"
    echo $status
    echo $result1
 #   echo "-------"
fi 


echo "===================="
echo "SECOND API CALL"
echo "===================="
url_get=https://$IP_HOST/restconf/data/ietf-interfaces:interfaces
#echo "url_get is : $url_get"
#echo "na url_get---------------"


result2=$( curl -i -k \
    -H "Content-type: $DATAFORMAT" \
    -H "Accept: $DATAFORMAT" -X GET \
    -u "${RESTCONF_USERNAME}:${RESTCONF_PASSWORD}" \
      $url_get )

#echo "--------------na curl"
#echo $result2 

#cat $result2 |python3 -mjson.tool
status2=`echo $result2 | grep HTTP |cut -d " " -f2`

echo "Status code : $status2"
echo "interfaces: $result2"

echo "END REST API CALL"