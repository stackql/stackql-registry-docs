---
title: stream
hide_title: false
hide_table_of_contents: false
keywords:
  - stream
  - kinesisvideo
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
<tr><td><b>Id</b></td><td><code>aws.kinesisvideo.stream</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Kinesis Video stream.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the Kinesis Video stream.</td></tr>
<tr><td><code>data_retention_in_hours</code></td><td><code>integer</code></td><td>The number of hours till which Kinesis Video will retain the data in the stream</td></tr>
<tr><td><code>device_name</code></td><td><code>string</code></td><td>The name of the device that is writing to the stream.</td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td>AWS KMS key ID that Kinesis Video Streams uses to encrypt stream data.</td></tr>
<tr><td><code>media_type</code></td><td><code>string</code></td><td>The media type of the stream. Consumers of the stream can use this information when processing the stream.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs associated with the Kinesis Video Stream.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
name,
data_retention_in_hours,
device_name,
kms_key_id,
media_type,
tags
FROM aws.kinesisvideo.stream
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Name&gt;'
```
