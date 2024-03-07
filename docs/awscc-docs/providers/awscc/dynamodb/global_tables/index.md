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
Retrieves a list of <code>global_tables</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>global_tables</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.dynamodb.global_tables</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>table_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
table_name
FROM awscc.dynamodb.global_tables
WHERE region = 'us-east-1'
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

