---
title: playback_key_pair
hide_title: false
hide_table_of_contents: false
keywords:
  - playback_key_pair
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
Gets an individual <code>playback_key_pair</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>playback_key_pair</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IVS::PlaybackKeyPair</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ivs.playback_key_pair</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>An arbitrary string (a nickname) assigned to a playback key pair that helps the customer identify that resource. The value does not need to be unique.</td></tr>
<tr><td><code>public_key_material</code></td><td><code>string</code></td><td>The public portion of a customer-generated key pair.</td></tr>
<tr><td><code>fingerprint</code></td><td><code>string</code></td><td>Key-pair identifier.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Key-pair identifier.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the asset model.</td></tr>
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
name,
public_key_material,
fingerprint,
arn,
tags
FROM aws.ivs.playback_key_pair
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>playback_key_pair</code> resource, the following permissions are required:

### Read
```json
ivs:GetPlaybackKeyPair
```

### Update
```json
ivs:GetPlaybackKeyPair,
ivs:ListTagsForResource,
ivs:UntagResource,
ivs:TagResource
```

### Delete
```json
ivs:DeletePlaybackKeyPair,
ivs:UntagResource
```

