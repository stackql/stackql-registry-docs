---
title: kinesisvideo_stream
hide_title: false
hide_table_of_contents: false
keywords:
  - kinesisvideo_stream
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
Gets an individual <code>kinesisvideo_stream</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kinesisvideo_stream</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS::KinesisVideo::Stream</td></tr>
<tr><td><b>Id</b></td><td><code>aws.kinesisvideo.kinesisvideo_stream</code></td></tr>
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

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.kinesisvideo.kinesisvideo_stream
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>kinesisvideo_stream</code> resource, the following permissions are required:

### Read
```json
kinesisvideo:DescribeStream
```

### Update
```json
kinesisvideo:DescribeStream,
kinesisvideo:UpdateStream,
kinesisvideo:UpdateDataRetention
```

### Delete
```json
kinesisvideo:DescribeStream,
kinesisvideo:DeleteStream
```

