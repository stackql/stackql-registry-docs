---
title: encoder_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - encoder_configuration
  - ivs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>encoder_configuration</code> resource, use <code>encoder_configurations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>encoder_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IVS::EncoderConfiguration.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ivs.encoder_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Encoder configuration identifier.</td></tr>
<tr><td><code>video</code></td><td><code>object</code></td><td>Video configuration. Default: video resolution 1280x720, bitrate 2500 kbps, 30 fps</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Encoder configuration name.</td></tr>
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
video,
name,
tags
FROM aws.ivs.encoder_configuration
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>encoder_configuration</code> resource, the following permissions are required:

### Read
```json
ivs:GetEncoderConfiguration,
ivs:ListTagsForResource
```

### Update
```json
ivs:GetEncoderConfiguration,
ivs:ListTagsForResource,
ivs:UntagResource,
ivs:TagResource
```

### Delete
```json
ivs:DeleteEncoderConfiguration,
ivs:UntagResource
```

