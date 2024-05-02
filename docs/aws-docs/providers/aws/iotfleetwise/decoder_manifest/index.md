---
title: decoder_manifest
hide_title: false
hide_table_of_contents: false
keywords:
  - decoder_manifest
  - iotfleetwise
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>decoder_manifest</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>decoder_manifest</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::IoTFleetWise::DecoderManifest Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotfleetwise.decoder_manifest</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>last_modification_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>model_manifest_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>network_interfaces</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>signal_decoders</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
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
creation_time,
description,
last_modification_time,
model_manifest_arn,
name,
network_interfaces,
signal_decoders,
status,
tags
FROM aws.iotfleetwise.decoder_manifest
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>decoder_manifest</code> resource, the following permissions are required:

### Read
```json
iotfleetwise:GetDecoderManifest,
iotfleetwise:ListDecoderManifestSignals,
iotfleetwise:ListDecoderManifestNetworkInterfaces,
iotfleetwise:ListTagsForResource
```

### Update
```json
iotfleetwise:UpdateDecoderManifest,
iotfleetwise:GetDecoderManifest,
iotfleetwise:ListDecoderManifestSignals,
iotfleetwise:ListDecoderManifestNetworkInterfaces,
iotfleetwise:ListTagsForResource,
iotfleetwise:TagResource,
iotfleetwise:UntagResource
```

### Delete
```json
iotfleetwise:DeleteDecoderManifest,
iotfleetwise:GetDecoderManifest
```

