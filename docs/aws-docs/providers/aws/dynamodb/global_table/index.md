---
title: global_table
hide_title: false
hide_table_of_contents: false
keywords:
  - global_table
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

Gets or operates on an individual <code>global_table</code> resource, use <code>global_tables</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_table</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Version: None. Resource Type definition for AWS::DynamoDB::GlobalTable</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dynamodb.global_table" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="table_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sse_specification" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="stream_specification" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="replicas" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="write_provisioned_throughput_settings" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="table_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="attribute_definitions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="billing_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="global_secondary_indexes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="key_schema" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="local_secondary_indexes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stream_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="time_to_live_specification" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
table_id,
sse_specification,
stream_specification,
replicas,
write_provisioned_throughput_settings,
table_name,
attribute_definitions,
billing_mode,
global_secondary_indexes,
key_schema,
local_secondary_indexes,
arn,
stream_arn,
time_to_live_specification
FROM aws.dynamodb.global_table
WHERE data__Identifier = '<TableName>';
```

## Permissions

To operate on the <code>global_table</code> resource, the following permissions are required:

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

