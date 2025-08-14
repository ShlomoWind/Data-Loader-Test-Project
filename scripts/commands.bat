*create the SQL deployment:*
oc apply -f infrastructure/k8s/mysql.yaml
====
*logging into the Pod to run commands:*
oc get pods
oc rsh <pod-name>
mysql --user=appduser --password=appdpass sampledb
====
