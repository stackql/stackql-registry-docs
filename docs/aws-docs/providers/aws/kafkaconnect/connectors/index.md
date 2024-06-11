---
title: connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors
  - kafkaconnect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>connector</code> resource or lists <code>connectors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::KafkaConnect::Connector</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kafkaconnect.connectors" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="capacity" /></td><td><code>Information about the capacity allocated to the connector.</code></td><td></td></tr>
<tr><td><CopyableCode code="connector_arn" /></td><td><code>string</code></td><td>Amazon Resource Name for the created Connector.</td></tr>
<tr><td><CopyableCode code="connector_configuration" /></td><td><code>object</code></td><td>The configuration for the connector.</td></tr>
<tr><td><CopyableCode code="connector_description" /></td><td><code>string</code></td><td>A summary description of the connector.</td></tr>
<tr><td><CopyableCode code="connector_name" /></td><td><code>string</code></td><td>The name of the connector.</td></tr>
<tr><td><CopyableCode code="kafka_cluster" /></td><td><code>Details of how to connect to the Kafka cluster.</code></td><td></td></tr>
<tr><td><CopyableCode code="kafka_cluster_client_authentication" /></td><td><code>Details of the client authentication used by the Kafka cluster.</code></td><td></td></tr>
<tr><td><CopyableCode code="kafka_cluster_encryption_in_transit" /></td><td><code>Details of encryption in transit to the Kafka cluster.</code></td><td></td></tr>
<tr><td><CopyableCode code="kafka_connect_version" /></td><td><code>string</code></td><td>The version of Kafka Connect. It has to be compatible with both the Kafka cluster's version and the plugins.</td></tr>
<tr><td><CopyableCode code="log_delivery" /></td><td><code>Details of what logs are delivered and where they are delivered.</code></td><td></td></tr>
<tr><td><CopyableCode code="plugins" /></td><td><code>array</code></td><td>List of plugins to use with the connector.</td></tr>
<tr><td><CopyableCode code="service_execution_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM role used by the connector to access Amazon S3 objects and other external resources.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
<tr><td><CopyableCode code="worker_configuration" /></td><td><code>The configuration of the workers, which are the processes that run the connector logic.</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="Capacity, ConnectorConfiguration, ConnectorName, KafkaConnectVersion, KafkaCluster, KafkaClusterClientAuthentication, KafkaClusterEncryptionInTransit, Plugins, ServiceExecutionRoleArn, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>connectors</code> in a region.
```sql
SELECT
region,
connector_arn
FROM aws.kafkaconnect.connectors
WHERE region = 'us-east-1';
```
Gets all properties from a <code>connector</code>.
```sql
SELECT
region,
capacity,
connector_arn,
connector_configuration,
connector_description,
connector_name,
kafka_cluster,
kafka_cluster_client_authentication,
kafka_cluster_encryption_in_transit,
kafka_connect_version,
log_delivery,
plugins,
service_execution_role_arn,
tags,
worker_configuration
FROM aws.kafkaconnect.connectors
WHERE region = 'us-east-1' AND data__Identifier = '<ConnectorArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connector</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.kafkaconnect.connectors (
 Capacity,
 ConnectorConfiguration,
 ConnectorName,
 KafkaCluster,
 KafkaClusterClientAuthentication,
 KafkaClusterEncryptionInTransit,
 KafkaConnectVersion,
 Plugins,
 ServiceExecutionRoleArn,
 region
)
SELECT 
'{{ Capacity }}',
 '{{ ConnectorConfiguration }}',
 '{{ ConnectorName }}',
 '{{ KafkaCluster }}',
 '{{ KafkaClusterClientAuthentication }}',
 '{{ KafkaClusterEncryptionInTransit }}',
 '{{ KafkaConnectVersion }}',
 '{{ Plugins }}',
 '{{ ServiceExecutionRoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.kafkaconnect.connectors (
 Capacity,
 ConnectorConfiguration,
 ConnectorDescription,
 ConnectorName,
 KafkaCluster,
 KafkaClusterClientAuthentication,
 KafkaClusterEncryptionInTransit,
 KafkaConnectVersion,
 LogDelivery,
 Plugins,
 ServiceExecutionRoleArn,
 Tags,
 WorkerConfiguration,
 region
)
SELECT 
 '{{ Capacity }}',
 '{{ ConnectorConfiguration }}',
 '{{ ConnectorDescription }}',
 '{{ ConnectorName }}',
 '{{ KafkaCluster }}',
 '{{ KafkaClusterClientAuthentication }}',
 '{{ KafkaClusterEncryptionInTransit }}',
 '{{ KafkaConnectVersion }}',
 '{{ LogDelivery }}',
 '{{ Plugins }}',
 '{{ ServiceExecutionRoleArn }}',
 '{{ Tags }}',
 '{{ WorkerConfiguration }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: connector
    props:
      - name: Capacity
        value:
          AutoScaling:
            MaxWorkerCount: '{{ MaxWorkerCount }}'
            MinWorkerCount: '{{ MinWorkerCount }}'
            ScaleInPolicy:
              CpuUtilizationPercentage: '{{ CpuUtilizationPercentage }}'
            ScaleOutPolicy:
              CpuUtilizationPercentage: '{{ CpuUtilizationPercentage }}'
            McuCount: '{{ McuCount }}'
          ProvisionedCapacity:
            McuCount: '{{ McuCount }}'
            WorkerCount: '{{ WorkerCount }}'
      - name: ConnectorConfiguration
        value: {}
      - name: ConnectorDescription
        value: '{{ ConnectorDescription }}'
      - name: ConnectorName
        value: '{{ ConnectorName }}'
      - name: KafkaCluster
        value:
          ApacheKafkaCluster:
            BootstrapServers: '{{ BootstrapServers }}'
            Vpc:
              SecurityGroups:
                - '{{ SecurityGroups[0] }}'
              Subnets:
                - '{{ Subnets[0] }}'
      - name: KafkaClusterClientAuthentication
        value:
          AuthenticationType: '{{ AuthenticationType }}'
      - name: KafkaClusterEncryptionInTransit
        value:
          EncryptionType: '{{ EncryptionType }}'
      - name: KafkaConnectVersion
        value: '{{ KafkaConnectVersion }}'
      - name: LogDelivery
        value:
          WorkerLogDelivery:
            CloudWatchLogs:
              Enabled: '{{ Enabled }}'
              LogGroup: '{{ LogGroup }}'
            Firehose:
              DeliveryStream: '{{ DeliveryStream }}'
              Enabled: '{{ Enabled }}'
            S3:
              Bucket: '{{ Bucket }}'
              Enabled: '{{ Enabled }}'
              Prefix: '{{ Prefix }}'
      - name: Plugins
        value:
          - CustomPlugin:
              Name: '{{ Name }}'
              Description: '{{ Description }}'
              ContentType: '{{ ContentType }}'
              Location:
                S3Location:
                  BucketArn: '{{ BucketArn }}'
                  FileKey: '{{ FileKey }}'
                  ObjectVersion: '{{ ObjectVersion }}'
              Tags:
                - Key: '{{ Key }}'
                  Value: '{{ Value }}'
      - name: ServiceExecutionRoleArn
        value: '{{ ServiceExecutionRoleArn }}'
      - name: Tags
        value:
          - null
      - name: WorkerConfiguration
        value:
          Name: '{{ Name }}'
          Description: '{{ Description }}'
          PropertiesFileContent: '{{ PropertiesFileContent }}'
          Tags:
            - null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.kafkaconnect.connectors
WHERE data__Identifier = '<ConnectorArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>connectors</code> resource, the following permissions are required:

### Create
```json
kafkaconnect:CreateConnector,
kafkaconnect:DescribeConnector,
kafkaconnect:TagResource,
kafkaconnect:ListTagsForResource,
iam:CreateServiceLinkedRole,
iam:PassRole,
ec2:CreateNetworkInterface,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcs,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:ListLogDeliveries,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
s3:GetBucketPolicy,
s3:PutBucketPolicy,
firehose:TagDeliveryStream
```

### Read
```json
kafkaconnect:DescribeConnector,
kafkaconnect:ListTagsForResource
```

### Delete
```json
kafkaconnect:DeleteConnector,
kafkaconnect:DescribeConnector,
logs:DeleteLogDelivery,
logs:GetLogDelivery,
logs:ListLogDeliveries
```

### Update
```json
kafkaconnect:UpdateConnector,
kafkaconnect:DescribeConnector,
kafkaconnect:TagResource,
kafkaconnect:ListTagsForResource,
kafkaconnect:UntagResource,
iam:CreateServiceLinkedRole,
logs:UpdateLogDelivery,
logs:GetLogDelivery,
logs:ListLogDeliveries,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
s3:GetBucketPolicy,
s3:PutBucketPolicy,
firehose:TagDeliveryStream
```

### List
```json
kafkaconnect:ListConnectors
```

