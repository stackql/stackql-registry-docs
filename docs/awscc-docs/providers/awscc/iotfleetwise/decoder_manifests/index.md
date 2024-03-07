---
title: decoder_manifests
hide_title: false
hide_table_of_contents: false
keywords:
  - decoder_manifests
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
Retrieves a list of <code>decoder_manifests</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>decoder_manifests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>decoder_manifests</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotfleetwise.decoder_manifests</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>decoder_manifests</code> resource, the following permissions are required:

### Create
<pre>
iotfleetwise:CreateDecoderManifest,
iotfleetwise:GetDecoderManifest,
iotfleetwise:UpdateDecoderManifest,
iotfleetwise:ListDecoderManifestSignals,
iotfleetwise:ListDecoderManifestNetworkInterfaces,
iotfleetwise:ListTagsForResource,
iotfleetwise:TagResource</pre>

### List
<pre>
iotfleetwise:ListDecoderManifests</pre>


## Example
```sql
SELECT
region,
name
FROM awscc.iotfleetwise.decoder_manifests
WHERE region = 'us-east-1'
```
