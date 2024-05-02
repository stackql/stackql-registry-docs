---
title: signaling_channel
hide_title: false
hide_table_of_contents: false
keywords:
  - signaling_channel
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
Gets an individual <code>signaling_channel</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>signaling_channel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS::KinesisVideo::SignalingChannel</td></tr>
<tr><td><b>Id</b></td><td><code>aws.kinesisvideo.signaling_channel</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Kinesis Video Signaling Channel.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the Kinesis Video Signaling Channel.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of the Kinesis Video Signaling Channel to create. Currently, SINGLE_MASTER is the only supported channel type.</td></tr>
<tr><td><code>message_ttl_seconds</code></td><td><code>integer</code></td><td>The period of time a signaling channel retains undelivered messages before they are discarded.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
type,
message_ttl_seconds,
tags
FROM aws.kinesisvideo.signaling_channel
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>signaling_channel</code> resource, the following permissions are required:

### Read
```json
kinesisvideo:DescribeSignalingChannel
```

### Update
```json
kinesisvideo:UpdateSignalingChannel,
kinesisvideo:DescribeSignalingChannel
```

### Delete
```json
kinesisvideo:DeleteSignalingChannel,
kinesisvideo:DescribeSignalingChannel
```

