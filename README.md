# Python Basic Unit Test and when use Mock

## Use case:

In this example, we will use practical case which  is used by cloud provider 
during resource instantiation. We will use database provision workflow. 

## Vocabulary

    cluster: means virtual machine which contains a database engine.

    hostname: is the name of the host which the database is hosted.

    servername: means the name of the server. It's a technical name which
                is used by an agent inside the cluster. This agent is in charge
                to send database activity to another server (CloudWatch) in AWS.


Below the workflow during provision
====================================

## Workflow of provisioning

To create a cluster, some inputs are expected:

### inputs

In this first case, the cluster to create is a PostgreSQL engine

    environment: the environment of the cluster: DEV, HML or PRD
    vm_profile: virtual machine flavor
    version: version of the cluster postgres

Custom errors are raised when inputs are invalid


## Workflow of creation a database

    ensure the inputs are well transmitted
    generate a hostname for the cluster
    call server to build the servername
    
 
 ## Workflow of building a unique servername for a cluster

    environment should be DEV, HML or PRD
    db_engine should be POSTGRESQL or ORACLE
    hostname should be a full qualified domain name like database.server.cloud
    servername is a unique name of the given cluster
    