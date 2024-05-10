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


Used to retrieve a list of <code>tables</code> in a region or to create or delete a <code>tables</code> resource, use <code>table</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Cassandra::Table</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cassandra.tables" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="keyspace_name" /></td><td><code>string</code></td><td>Name for Cassandra keyspace</td></tr>
<tr><td><CopyableCode code="table_name" /></td><td><code>string</code></td><td>Name for Cassandra table</td></tr>
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
keyspace_name,
table_name
FROM aws.cassandra.tables
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- table.iql (required properties only)
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
-- table.iql (all properties)
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

## `DELETE` Example

```sql
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

