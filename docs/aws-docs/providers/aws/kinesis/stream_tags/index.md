---
title: stream_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - stream_tags
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

Expands all tag keys and values for <code>streams</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stream_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Kinesis::Stream</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kinesis.stream_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="stream_mode_details" /></td><td><code>object</code></td><td>The mode in which the stream is running.</td></tr>
<tr><td><CopyableCode code="stream_encryption" /></td><td><code>object</code></td><td>When specified, enables or updates server-side encryption using an AWS KMS key for a specified stream.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon resource name (ARN) of the Kinesis stream</td></tr>
<tr><td><CopyableCode code="retention_period_hours" /></td><td><code>integer</code></td><td>The number of hours for the data records that are stored in shards to remain accessible.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the Kinesis stream.</td></tr>
<tr><td><CopyableCode code="shard_count" /></td><td><code>integer</code></td><td>The number of shards that the stream uses. Required when StreamMode = PROVISIONED is passed.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>streams</code> in a region.
```sql
SELECT
region,
stream_mode_details,
stream_encryption,
arn,
retention_period_hours,
name,
shard_count,
tag_key,
tag_value
FROM aws.kinesis.stream_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>stream_tags</code> resource, see <a href="/providers/aws/kinesis/streams/#permissions"><code>streams</code></a>

