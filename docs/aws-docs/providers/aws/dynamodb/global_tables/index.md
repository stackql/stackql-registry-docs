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


Used to retrieve a list of <code>global_tables</code> in a region or to create or delete a <code>global_tables</code> resource, use <code>global_table</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Version: None. Resource Type definition for AWS::DynamoDB::GlobalTable</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dynamodb.global_tables" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="table_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="KeySchema, AttributeDefinitions, Replicas, region" /></td>
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
table_name
FROM aws.dynamodb.global_tables
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
 Replicas,
 AttributeDefinitions,
 KeySchema,
 region
)
SELECT 
'{{ Replicas }}',
 '{{ AttributeDefinitions }}',
 '{{ KeySchema }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.dynamodb.global_tables (
 SSESpecification,
 StreamSpecification,
 Replicas,
 WriteProvisionedThroughputSettings,
 TableName,
 AttributeDefinitions,
 BillingMode,
 GlobalSecondaryIndexes,
 KeySchema,
 LocalSecondaryIndexes,
 TimeToLiveSpecification,
 region
)
SELECT 
 '{{ SSESpecification }}',
 '{{ StreamSpecification }}',
 '{{ Replicas }}',
 '{{ WriteProvisionedThroughputSettings }}',
 '{{ TableName }}',
 '{{ AttributeDefinitions }}',
 '{{ BillingMode }}',
 '{{ GlobalSecondaryIndexes }}',
 '{{ KeySchema }}',
 '{{ LocalSecondaryIndexes }}',
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
      - name: SSESpecification
        value:
          SSEEnabled: '{{ SSEEnabled }}'
          SSEType: '{{ SSEType }}'
          KMSMasterKeyId: '{{ KMSMasterKeyId }}'
      - name: StreamSpecification
        value:
          StreamViewType: '{{ StreamViewType }}'
          ResourcePolicy:
            PolicyDocument: {}
      - name: Replicas
        value:
          - SSESpecification:
              KMSMasterKeyId: '{{ KMSMasterKeyId }}'
            KinesisStreamSpecification:
              ApproximateCreationDateTimePrecision: '{{ ApproximateCreationDateTimePrecision }}'
              StreamArn: '{{ StreamArn }}'
            ContributorInsightsSpecification:
              Enabled: '{{ Enabled }}'
            PointInTimeRecoverySpecification:
              PointInTimeRecoveryEnabled: '{{ PointInTimeRecoveryEnabled }}'
            ReplicaStreamSpecification:
              ResourcePolicy: null
            GlobalSecondaryIndexes:
              - IndexName: '{{ IndexName }}'
                ContributorInsightsSpecification: null
                ReadProvisionedThroughputSettings:
                  ReadCapacityUnits: '{{ ReadCapacityUnits }}'
                  ReadCapacityAutoScalingSettings:
                    MinCapacity: '{{ MinCapacity }}'
                    SeedCapacity: '{{ SeedCapacity }}'
                    TargetTrackingScalingPolicyConfiguration:
                      ScaleOutCooldown: '{{ ScaleOutCooldown }}'
                      TargetValue: null
                      DisableScaleIn: '{{ DisableScaleIn }}'
                      ScaleInCooldown: '{{ ScaleInCooldown }}'
                    MaxCapacity: '{{ MaxCapacity }}'
            Region: '{{ Region }}'
            ResourcePolicy: null
            ReadProvisionedThroughputSettings: null
            TableClass: '{{ TableClass }}'
            DeletionProtectionEnabled: '{{ DeletionProtectionEnabled }}'
            Tags:
              - Value: '{{ Value }}'
                Key: '{{ Key }}'
      - name: WriteProvisionedThroughputSettings
        value:
          WriteCapacityAutoScalingSettings: null
      - name: TableName
        value: '{{ TableName }}'
      - name: AttributeDefinitions
        value:
          - AttributeType: '{{ AttributeType }}'
            AttributeName: '{{ AttributeName }}'
      - name: BillingMode
        value: '{{ BillingMode }}'
      - name: GlobalSecondaryIndexes
        value:
          - IndexName: '{{ IndexName }}'
            ContributorInsightsSpecification: null
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
      - name: KeySchema
        value:
          - null
      - name: LocalSecondaryIndexes
        value:
          - IndexName: '{{ IndexName }}'
            Projection: null
            KeySchema:
              - null
      - name: TimeToLiveSpecification
        value:
          Enabled: '{{ Enabled }}'
          AttributeName: '{{ AttributeName }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

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

### List
```json
dynamodb:ListTables,
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

