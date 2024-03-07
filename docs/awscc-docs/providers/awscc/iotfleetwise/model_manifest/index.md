---
title: model_manifest
hide_title: false
hide_table_of_contents: false
keywords:
  - model_manifest
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
Gets an individual <code>model_manifest</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_manifest</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>model_manifest</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotfleetwise.model_manifest</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>last_modification_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>nodes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>signal_catalog_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
creation_time,
description,
last_modification_time,
name,
nodes,
signal_catalog_arn,
status,
tags
FROM awscc.iotfleetwise.model_manifest
WHERE region = 'us-east-1'
AND data__Identifier = '{Name}';
```

## Permissions

To operate on the <code>model_manifest</code> resource, the following permissions are required:

### Read
```json
iotfleetwise:GetModelManifest,
iotfleetwise:ListModelManifestNodes,
iotfleetwise:ListTagsForResource
```

### Update
```json
iotfleetwise:UpdateModelManifest,
iotfleetwise:GetModelManifest,
iotfleetwise:ListModelManifestNodes,
iotfleetwise:ListTagsForResource,
iotfleetwise:TagResource,
iotfleetwise:UntagResource
```

### Delete
```json
iotfleetwise:DeleteModelManifest,
iotfleetwise:GetModelManifest
```

