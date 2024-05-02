---
title: recording_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - recording_configuration
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
Gets an individual <code>recording_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recording_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IVS::RecordingConfiguration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ivs.recording_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Recording Configuration ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Recording Configuration Name.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>Recording Configuration State.</td></tr>
<tr><td><code>recording_reconnect_window_seconds</code></td><td><code>integer</code></td><td>Recording Reconnect Window Seconds. (0 means disabled)</td></tr>
<tr><td><code>destination_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the asset model.</td></tr>
<tr><td><code>thumbnail_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>rendition_configuration</code></td><td><code>object</code></td><td></td></tr>
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
state,
recording_reconnect_window_seconds,
destination_configuration,
tags,
thumbnail_configuration,
rendition_configuration
FROM aws.ivs.recording_configuration
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>recording_configuration</code> resource, the following permissions are required:

### Read
```json
ivs:GetRecordingConfiguration,
s3:GetBucketLocation,
ivs:ListTagsForResource
```

### Update
```json
ivs:GetRecordingConfiguration,
sts:AssumeRole,
iam:CreateServiceLinkedRole,
iam:PutRolePolicy,
iam:AttachRolePolicy,
s3:ListBucket,
ivs:TagResource,
ivs:UntagResource,
ivs:ListTagsForResource
```

### Delete
```json
ivs:DeleteRecordingConfiguration,
ivs:UntagResource,
iam:CreateServiceLinkedRole
```

