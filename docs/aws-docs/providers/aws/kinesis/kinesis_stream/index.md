---
title: kinesis_stream
hide_title: false
hide_table_of_contents: false
keywords:
  - kinesis_stream
  - kinesis
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


Gets or updates an individual <code>kinesis_stream</code> resource, use <code>kinesis_streams</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kinesis_stream</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Kinesis::Stream</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kinesis.kinesis_stream" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="stream_mode_details" /></td><td><code>object</code></td><td>The mode in which the stream is running.</td></tr>
<tr><td><CopyableCode code="stream_encryption" /></td><td><code>object</code></td><td>When specified, enables or updates server-side encryption using an AWS KMS key for a specified stream.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon resource name (ARN) of the Kinesis stream</td></tr>
<tr><td><CopyableCode code="retention_period_hours" /></td><td><code>integer</code></td><td>The number of hours for the data records that are stored in shards to remain accessible.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An arbitrary set of tags (key–value pairs) to associate with the Kinesis stream.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the Kinesis stream.</td></tr>
<tr><td><CopyableCode code="shard_count" /></td><td><code>integer</code></td><td>The number of shards that the stream uses. Required when StreamMode = PROVISIONED is passed.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
stream_mode_details,
stream_encryption,
arn,
retention_period_hours,
tags,
name,
shard_count
FROM aws.kinesis.kinesis_stream
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## Permissions

To operate on the <code>kinesis_stream</code> resource, the following permissions are required:

### Read
```json
kinesis:DescribeStreamSummary,
kinesis:ListTagsForStream
```

### Update
```json
kinesis:EnableEnhancedMonitoring,
kinesis:DisableEnhancedMonitoring,
kinesis:DescribeStreamSummary,
kinesis:UpdateShardCount,
kinesis:UpdateStreamMode,
kinesis:IncreaseStreamRetentionPeriod,
kinesis:DecreaseStreamRetentionPeriod,
kinesis:StartStreamEncryption,
kinesis:StopStreamEncryption,
kinesis:AddTagsToStream,
kinesis:RemoveTagsFromStream,
kinesis:ListTagsForStream
```

