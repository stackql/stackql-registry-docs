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


Used to retrieve a list of <code>connectors</code> in a region or to create or delete a <code>connectors</code> resource, use <code>connector</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::KafkaConnect::Connector</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kafkaconnect.connectors" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="connector_arn" /></td><td><code>string</code></td><td>Amazon Resource Name for the created Connector.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
connector_arn
FROM aws.kafkaconnect.connectors
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- connector.iql (required properties only)
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
-- connector.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
kafkaconnect:DeleteConnector,
kafkaconnect:DescribeConnector,
logs:DeleteLogDelivery,
logs:GetLogDelivery,
logs:ListLogDeliveries
```

### List
```json
kafkaconnect:ListConnectors
```

