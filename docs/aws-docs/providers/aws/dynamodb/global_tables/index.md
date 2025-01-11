---
title: global_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - global_tables
  - dynamodb
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

Creates, updates, deletes or gets a <code>global_table</code> resource or lists <code>global_tables</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Version: None. Resource Type definition for AWS::DynamoDB::GlobalTable</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dynamodb.global_tables" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stream_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="attribute_definitions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="billing_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="global_secondary_indexes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="key_schema" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="local_secondary_indexes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="point_in_time_recovery_specification" /></td><td><code>object</code></td><td>The settings used to enable point in time recovery.</td></tr>
<tr><td><CopyableCode code="write_provisioned_throughput_settings" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="write_on_demand_throughput_settings" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="warm_throughput" /></td><td><code>object</code></td><td>Provides visibility into the number of read and write operations your table or secondary index can instantaneously support. The settings can be modified using the <code>UpdateTable</code> operation to meet the throughput requirements of an upcoming peak event.</td></tr>
<tr><td><CopyableCode code="replicas" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="sse_specification" /></td><td><code>object</code></td><td>Represents the settings used to enable server-side encryption.</td></tr>
<tr><td><CopyableCode code="stream_specification" /></td><td><code>object</code></td><td>Represents the DynamoDB Streams configuration for a table in DynamoDB.</td></tr>
<tr><td><CopyableCode code="table_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="table_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="time_to_live_specification" /></td><td><code>object</code></td><td>Represents the settings used to enable or disable Time to Live (TTL) for the specified table.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html"><code>AWS::DynamoDB::GlobalTable</code></a>.

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
    <td><CopyableCode code="KeySchema, AttributeDefinitions, Replicas, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>global_tables</code> in a region.
```sql
SELECT
region,
arn,
stream_arn,
attribute_definitions,
billing_mode,
global_secondary_indexes,
key_schema,
local_secondary_indexes,
point_in_time_recovery_specification,
write_provisioned_throughput_settings,
write_on_demand_throughput_settings,
warm_throughput,
replicas,
sse_specification,
stream_specification,
table_name,
table_id,
time_to_live_specification
FROM aws.dynamodb.global_tables
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>global_table</code>.
```sql
SELECT
region,
arn,
stream_arn,
attribute_definitions,
billing_mode,
global_secondary_indexes,
key_schema,
local_secondary_indexes,
point_in_time_recovery_specification,
write_provisioned_throughput_settings,
write_on_demand_throughput_settings,
warm_throughput,
replicas,
sse_specification,
stream_specification,
table_name,
table_id,
time_to_live_specification
FROM aws.dynamodb.global_tables
WHERE region = 'us-east-1' AND data__Identifier = '<TableName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>global_table</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.dynamodb.global_tables (
 AttributeDefinitions,
 KeySchema,
 Replicas,
 region
)
SELECT 
'{{ AttributeDefinitions }}',
 '{{ KeySchema }}',
 '{{ Replicas }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.dynamodb.global_tables (
 AttributeDefinitions,
 BillingMode,
 GlobalSecondaryIndexes,
 KeySchema,
 LocalSecondaryIndexes,
 PointInTimeRecoverySpecification,
 WriteProvisionedThroughputSettings,
 WriteOnDemandThroughputSettings,
 WarmThroughput,
 Replicas,
 SSESpecification,
 StreamSpecification,
 TableName,
 TimeToLiveSpecification,
 region
)
SELECT 
 '{{ AttributeDefinitions }}',
 '{{ BillingMode }}',
 '{{ GlobalSecondaryIndexes }}',
 '{{ KeySchema }}',
 '{{ LocalSecondaryIndexes }}',
 '{{ PointInTimeRecoverySpecification }}',
 '{{ WriteProvisionedThroughputSettings }}',
 '{{ WriteOnDemandThroughputSettings }}',
 '{{ WarmThroughput }}',
 '{{ Replicas }}',
 '{{ SSESpecification }}',
 '{{ StreamSpecification }}',
 '{{ TableName }}',
 '{{ TimeToLiveSpecification }}',
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
  - name: global_table
    props:
      - name: AttributeDefinitions
        value:
          - AttributeType: '{{ AttributeType }}'
            AttributeName: '{{ AttributeName }}'
      - name: BillingMode
        value: '{{ BillingMode }}'
      - name: GlobalSecondaryIndexes
        value:
          - IndexName: '{{ IndexName }}'
            OnDemandThroughput:
              MaxReadRequestUnits: '{{ MaxReadRequestUnits }}'
              MaxWriteRequestUnits: '{{ MaxWriteRequestUnits }}'
            ContributorInsightsSpecification:
              Enabled: '{{ Enabled }}'
            Projection:
              NonKeyAttributes:
                - '{{ NonKeyAttributes[0] }}'
              ProjectionType: '{{ ProjectionType }}'
            ProvisionedThroughput:
              WriteCapacityUnits: '{{ WriteCapacityUnits }}'
              ReadCapacityUnits: '{{ ReadCapacityUnits }}'
            KeySchema:
              - KeyType: '{{ KeyType }}'
                AttributeName: '{{ AttributeName }}'
            WarmThroughput:
              ReadUnitsPerSecond: '{{ ReadUnitsPerSecond }}'
              WriteUnitsPerSecond: '{{ WriteUnitsPerSecond }}'
      - name: KeySchema
        value:
          - null
      - name: LocalSecondaryIndexes
        value:
          - IndexName: '{{ IndexName }}'
            Projection: null
            KeySchema:
              - null
      - name: PointInTimeRecoverySpecification
        value:
          PointInTimeRecoveryEnabled: '{{ PointInTimeRecoveryEnabled }}'
          RecoveryPeriodInDays: '{{ RecoveryPeriodInDays }}'
      - name: WriteProvisionedThroughputSettings
        value:
          WriteCapacityAutoScalingSettings:
            MinCapacity: '{{ MinCapacity }}'
            MaxCapacity: '{{ MaxCapacity }}'
            SeedCapacity: '{{ SeedCapacity }}'
            TargetTrackingScalingPolicyConfiguration:
              DisableScaleIn: '{{ DisableScaleIn }}'
              ScaleInCooldown: '{{ ScaleInCooldown }}'
              ScaleOutCooldown: '{{ ScaleOutCooldown }}'
              TargetValue: null
      - name: WriteOnDemandThroughputSettings
        value:
          MaxWriteRequestUnits: '{{ MaxWriteRequestUnits }}'
      - name: WarmThroughput
        value: null
      - name: Replicas
        value:
          - Region: '{{ Region }}'
            GlobalSecondaryIndexes:
              - IndexName: '{{ IndexName }}'
                ContributorInsightsSpecification: null
                ReadProvisionedThroughputSettings:
                  ReadCapacityUnits: '{{ ReadCapacityUnits }}'
                  ReadCapacityAutoScalingSettings: null
                ReadOnDemandThroughputSettings:
                  MaxReadRequestUnits: '{{ MaxReadRequestUnits }}'
            ContributorInsightsSpecification: null
            PointInTimeRecoverySpecification: null
            TableClass: '{{ TableClass }}'
            DeletionProtectionEnabled: '{{ DeletionProtectionEnabled }}'
            SSESpecification:
              KMSMasterKeyId: '{{ KMSMasterKeyId }}'
            Tags:
              - Value: '{{ Value }}'
                Key: '{{ Key }}'
            ReadProvisionedThroughputSettings: null
            ReadOnDemandThroughputSettings: null
            KinesisStreamSpecification:
              ApproximateCreationDateTimePrecision: '{{ ApproximateCreationDateTimePrecision }}'
              StreamArn: '{{ StreamArn }}'
            ResourcePolicy:
              PolicyDocument: {}
            ReplicaStreamSpecification:
              ResourcePolicy: null
      - name: SSESpecification
        value:
          SSEEnabled: '{{ SSEEnabled }}'
          SSEType: '{{ SSEType }}'
          KMSMasterKeyId: '{{ KMSMasterKeyId }}'
      - name: StreamSpecification
        value:
          StreamViewType: '{{ StreamViewType }}'
          ResourcePolicy: null
      - name: TableName
        value: '{{ TableName }}'
      - name: TimeToLiveSpecification
        value:
          Enabled: '{{ Enabled }}'
          AttributeName: '{{ AttributeName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.dynamodb.global_tables
WHERE data__Identifier = '<TableName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>global_tables</code> resource, the following permissions are required:

### Create
```json
dynamodb:CreateTable,
dynamodb:CreateTableReplica,
dynamodb:Describe*,
dynamodb:UpdateTimeToLive,
dynamodb:UpdateContributorInsights,
dynamodb:UpdateContinuousBackups,
dynamodb:ListTagsOfResource,
dynamodb:Query,
dynamodb:Scan,
dynamodb:UpdateItem,
dynamodb:PutItem,
dynamodb:GetItem,
dynamodb:DeleteItem,
dynamodb:BatchWriteItem,
dynamodb:TagResource,
dynamodb:EnableKinesisStreamingDestination,
dynamodb:DisableKinesisStreamingDestination,
dynamodb:UpdateTableReplicaAutoScaling,
dynamodb:TagResource,
dynamodb:GetResourcePolicy,
dynamodb:PutResourcePolicy,
application-autoscaling:DeleteScalingPolicy,
application-autoscaling:DeleteScheduledAction,
application-autoscaling:DeregisterScalableTarget,
application-autoscaling:Describe*,
application-autoscaling:PutScalingPolicy,
application-autoscaling:PutScheduledAction,
application-autoscaling:RegisterScalableTarget,
kinesis:ListStreams,
kinesis:DescribeStream,
kinesis:PutRecords,
kms:CreateGrant,
kms:DescribeKey,
kms:ListAliases,
kms:Decrypt,
kms:RevokeGrant,
cloudwatch:PutMetricData,
iam:CreateServiceLinkedRole
```

### Read
```json
dynamodb:Describe*,
dynamodb:GetResourcePolicy,
application-autoscaling:Describe*,
cloudwatch:PutMetricData,
dynamodb:ListTagsOfResource,
kms:DescribeKey
```

### Update
```json
dynamodb:Describe*,
dynamodb:CreateTableReplica,
dynamodb:UpdateTable,
dynamodb:UpdateTimeToLive,
dynamodb:UpdateContinuousBackups,
dynamodb:UpdateContributorInsights,
dynamodb:ListTagsOfResource,
dynamodb:Query,
dynamodb:Scan,
dynamodb:UpdateItem,
dynamodb:PutItem,
dynamodb:GetItem,
dynamodb:DeleteItem,
dynamodb:BatchWriteItem,
dynamodb:DeleteTable,
dynamodb:DeleteTableReplica,
dynamodb:UpdateItem,
dynamodb:TagResource,
dynamodb:UntagResource,
dynamodb:EnableKinesisStreamingDestination,
dynamodb:DisableKinesisStreamingDestination,
dynamodb:UpdateTableReplicaAutoScaling,
dynamodb:UpdateKinesisStreamingDestination,
dynamodb:GetResourcePolicy,
dynamodb:PutResourcePolicy,
dynamodb:DeleteResourcePolicy,
application-autoscaling:DeleteScalingPolicy,
application-autoscaling:DeleteScheduledAction,
application-autoscaling:DeregisterScalableTarget,
application-autoscaling:Describe*,
application-autoscaling:PutScalingPolicy,
application-autoscaling:PutScheduledAction,
application-autoscaling:RegisterScalableTarget,
kinesis:ListStreams,
kinesis:DescribeStream,
kinesis:PutRecords,
kms:CreateGrant,
kms:DescribeKey,
kms:ListAliases,
kms:RevokeGrant,
cloudwatch:PutMetricData
```

### Delete
```json
dynamodb:Describe*,
dynamodb:DeleteTable,
application-autoscaling:DeleteScalingPolicy,
application-autoscaling:DeleteScheduledAction,
application-autoscaling:DeregisterScalableTarget,
application-autoscaling:Describe*,
application-autoscaling:PutScalingPolicy,
application-autoscaling:PutScheduledAction,
application-autoscaling:RegisterScalableTarget
```

### List
```json
dynamodb:ListTables,
cloudwatch:PutMetricData
```
