---
title: streams
hide_title: false
hide_table_of_contents: false
keywords:
  - streams
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
Retrieves a list of <code>streams</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.kinesis.streams</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>StreamModeDetails</code></td><td><code>undefined</code></td><td>The mode in which the stream is running.</td></tr><tr><td><code>StreamEncryption</code></td><td><code>undefined</code></td><td>When specified, enables or updates server-side encryption using an AWS KMS key for a specified stream.</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon resource name (ARN) of the Kinesis stream</td></tr><tr><td><code>RetentionPeriodHours</code></td><td><code>integer</code></td><td>The number of hours for the data records that are stored in shards to remain accessible.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An arbitrary set of tags (key–value pairs) to associate with the Kinesis stream.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the Kinesis stream.</td></tr><tr><td><code>ShardCount</code></td><td><code>integer</code></td><td>The number of shards that the stream uses. Required when StreamMode = PROVISIONED is passed.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.kinesis.streams
WHERE region = 'us-east-1'
</pre>
