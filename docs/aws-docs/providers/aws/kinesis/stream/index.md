---
title: stream
hide_title: false
hide_table_of_contents: false
keywords:
  - stream
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
Gets an individual <code>stream</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stream</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>stream</td></tr>
<tr><td><b>Id</b></td><td><code>aws.kinesis.stream</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>stream_mode_details</code></td><td><code>object</code></td><td>The mode in which the stream is running.</td></tr>
<tr><td><code>stream_encryption</code></td><td><code>object</code></td><td>When specified, enables or updates server-side encryption using an AWS KMS key for a specified stream.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon resource name (ARN) of the Kinesis stream</td></tr>
<tr><td><code>retention_period_hours</code></td><td><code>integer</code></td><td>The number of hours for the data records that are stored in shards to remain accessible.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An arbitrary set of tags (key–value pairs) to associate with the Kinesis stream.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the Kinesis stream.</td></tr>
<tr><td><code>shard_count</code></td><td><code>integer</code></td><td>The number of shards that the stream uses. Required when StreamMode = PROVISIONED is passed.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM aws.kinesis.stream
WHERE region = 'us-east-1'
AND data__Identifier = '<Name>'
```
