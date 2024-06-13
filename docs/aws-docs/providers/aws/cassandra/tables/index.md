---
title: tables
hide_title: false
hide_table_of_contents: false
keywords:
  - tables
  - cassandra
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

Creates, updates, deletes or gets a <code>table</code> resource or lists <code>tables</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Cassandra::Table</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cassandra.tables" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="keyspace_name" /></td><td><code>string</code></td><td>Name for Cassandra keyspace</td></tr>
<tr><td><CopyableCode code="table_name" /></td><td><code>string</code></td><td>Name for Cassandra table</td></tr>
<tr><td><CopyableCode code="regular_columns" /></td><td><code>array</code></td><td>Non-key columns of the table</td></tr>
<tr><td><CopyableCode code="partition_key_columns" /></td><td><code>array</code></td><td>Partition key columns of the table</td></tr>
<tr><td><CopyableCode code="clustering_key_columns" /></td><td><code>array</code></td><td>Clustering key columns of the table</td></tr>
<tr><td><CopyableCode code="billing_mode" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="point_in_time_recovery_enabled" /></td><td><code>boolean</code></td><td>Indicates whether point in time recovery is enabled (true) or disabled (false) on the table</td></tr>
<tr><td><CopyableCode code="client_side_timestamps_enabled" /></td><td><code>boolean</code></td><td>Indicates whether client side timestamps are enabled (true) or disabled (false) on the table. False by default, once it is enabled it cannot be disabled again.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource</td></tr>
<tr><td><CopyableCode code="default_time_to_live" /></td><td><code>integer</code></td><td>Default TTL (Time To Live) in seconds, where zero is disabled. If the value is greater than zero, TTL is enabled for the entire table and an expiration timestamp is added to each column.</td></tr>
<tr><td><CopyableCode code="encryption_specification" /></td><td><code>object</code></td><td>Represents the settings used to enable server-side encryption</td></tr>
<tr><td><CopyableCode code="auto_scaling_specifications" /></td><td><code>object</code></td><td>Represents the read and write settings used for AutoScaling.</td></tr>
<tr><td><CopyableCode code="replica_specifications" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="KeyspaceName, PartitionKeyColumns, region" /></td>
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
List all <code>tables</code> in a region.
```sql
SELECT
region,
keyspace_name,
table_name
FROM aws.cassandra.tables
WHERE region = 'us-east-1';
```
Gets all properties from a <code>table</code>.
```sql
SELECT
region,
keyspace_name,
table_name,
regular_columns,
partition_key_columns,
clustering_key_columns,
billing_mode,
point_in_time_recovery_enabled,
client_side_timestamps_enabled,
tags,
default_time_to_live,
encryption_specification,
auto_scaling_specifications,
replica_specifications
FROM aws.cassandra.tables
WHERE region = 'us-east-1' AND data__Identifier = '<KeyspaceName>|<TableName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>table</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cassandra.tables (
 KeyspaceName,
 PartitionKeyColumns,
 region
)
SELECT 
'{{ KeyspaceName }}',
 '{{ PartitionKeyColumns }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cassandra.tables (
 KeyspaceName,
 TableName,
 RegularColumns,
 PartitionKeyColumns,
 ClusteringKeyColumns,
 BillingMode,
 PointInTimeRecoveryEnabled,
 ClientSideTimestampsEnabled,
 Tags,
 DefaultTimeToLive,
 EncryptionSpecification,
 AutoScalingSpecifications,
 ReplicaSpecifications,
 region
)
SELECT 
 '{{ KeyspaceName }}',
 '{{ TableName }}',
 '{{ RegularColumns }}',
 '{{ PartitionKeyColumns }}',
 '{{ ClusteringKeyColumns }}',
 '{{ BillingMode }}',
 '{{ PointInTimeRecoveryEnabled }}',
 '{{ ClientSideTimestampsEnabled }}',
 '{{ Tags }}',
 '{{ DefaultTimeToLive }}',
 '{{ EncryptionSpecification }}',
 '{{ AutoScalingSpecifications }}',
 '{{ ReplicaSpecifications }}',
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
  - name: table
    props:
      - name: KeyspaceName
        value: '{{ KeyspaceName }}'
      - name: TableName
        value: '{{ TableName }}'
      - name: RegularColumns
        value:
          - ColumnName: '{{ ColumnName }}'
            ColumnType: '{{ ColumnType }}'
      - name: PartitionKeyColumns
        value:
          - null
      - name: ClusteringKeyColumns
        value:
          - Column: null
            OrderBy: '{{ OrderBy }}'
      - name: BillingMode
        value:
          Mode: '{{ Mode }}'
          ProvisionedThroughput:
            ReadCapacityUnits: '{{ ReadCapacityUnits }}'
            WriteCapacityUnits: '{{ WriteCapacityUnits }}'
      - name: PointInTimeRecoveryEnabled
        value: '{{ PointInTimeRecoveryEnabled }}'
      - name: ClientSideTimestampsEnabled
        value: '{{ ClientSideTimestampsEnabled }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: DefaultTimeToLive
        value: '{{ DefaultTimeToLive }}'
      - name: EncryptionSpecification
        value:
          EncryptionType: '{{ EncryptionType }}'
          KmsKeyIdentifier: '{{ KmsKeyIdentifier }}'
      - name: AutoScalingSpecifications
        value:
          WriteCapacityAutoScaling:
            AutoScalingDisabled: '{{ AutoScalingDisabled }}'
            MinimumUnits: '{{ MinimumUnits }}'
            MaximumUnits: '{{ MaximumUnits }}'
            ScalingPolicy:
              TargetTrackingScalingPolicyConfiguration:
                DisableScaleIn: '{{ DisableScaleIn }}'
                ScaleInCooldown: '{{ ScaleInCooldown }}'
                ScaleOutCooldown: '{{ ScaleOutCooldown }}'
                TargetValue: '{{ TargetValue }}'
          ReadCapacityAutoScaling: null
      - name: ReplicaSpecifications
        value:
          - Region: '{{ Region }}'
            ReadCapacityUnits: '{{ ReadCapacityUnits }}'
            ReadCapacityAutoScaling: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cassandra.tables
WHERE data__Identifier = '<KeyspaceName|TableName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>tables</code> resource, the following permissions are required:

### Create
```json
cassandra:Create,
cassandra:CreateMultiRegionResource,
cassandra:Select,
cassandra:SelectMultiRegionResource,
cassandra:TagResource,
cassandra:TagMultiRegionResource,
kms:CreateGrant,
kms:DescribeKey,
kms:Encrypt,
kms:Decrypt,
application-autoscaling:DescribeScalableTargets,
application-autoscaling:DescribeScalingPolicies,
application-autoscaling:DeregisterScalableTarget,
application-autoscaling:RegisterScalableTarget,
application-autoscaling:PutScalingPolicy,
cloudwatch:DeleteAlarms,
cloudwatch:DescribeAlarms,
cloudwatch:GetMetricData,
cloudwatch:PutMetricAlarm
```

### Read
```json
cassandra:Select,
cassandra:SelectMultiRegionResource,
application-autoscaling:DescribeScalableTargets,
application-autoscaling:DescribeScalingPolicies,
application-autoscaling:DeregisterScalableTarget,
application-autoscaling:RegisterScalableTarget,
application-autoscaling:PutScalingPolicy,
cloudwatch:DeleteAlarms,
cloudwatch:DescribeAlarms,
cloudwatch:GetMetricData,
cloudwatch:PutMetricAlarm
```

### Update
```json
cassandra:Alter,
cassandra:AlterMultiRegionResource,
cassandra:Select,
cassandra:SelectMultiRegionResource,
cassandra:TagResource,
cassandra:TagMultiRegionResource,
cassandra:UntagResource,
cassandra:UntagMultiRegionResource,
kms:CreateGrant,
kms:DescribeKey,
kms:Encrypt,
kms:Decrypt,
application-autoscaling:DescribeScalableTargets,
application-autoscaling:DescribeScalingPolicies,
application-autoscaling:DeregisterScalableTarget,
application-autoscaling:RegisterScalableTarget,
application-autoscaling:PutScalingPolicy,
cloudwatch:DeleteAlarms,
cloudwatch:DescribeAlarms,
cloudwatch:GetMetricData,
cloudwatch:PutMetricAlarm
```

### Delete
```json
cassandra:Drop,
cassandra:DropMultiRegionResource,
cassandra:Select,
cassandra:SelectMultiRegionResource,
application-autoscaling:DescribeScalableTargets,
application-autoscaling:DescribeScalingPolicies,
application-autoscaling:DeregisterScalableTarget,
application-autoscaling:RegisterScalableTarget,
application-autoscaling:PutScalingPolicy,
cloudwatch:DeleteAlarms,
cloudwatch:DescribeAlarms,
cloudwatch:GetMetricData,
cloudwatch:PutMetricAlarm
```

### List
```json
cassandra:Select,
cassandra:SelectMultiRegionResource,
application-autoscaling:DescribeScalableTargets,
application-autoscaling:DescribeScalingPolicies,
application-autoscaling:DeregisterScalableTarget,
application-autoscaling:RegisterScalableTarget,
application-autoscaling:PutScalingPolicy,
cloudwatch:DeleteAlarms,
cloudwatch:DescribeAlarms,
cloudwatch:GetMetricData,
cloudwatch:PutMetricAlarm
```

