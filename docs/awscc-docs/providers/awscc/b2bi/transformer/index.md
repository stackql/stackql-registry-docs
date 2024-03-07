---
title: transformer
hide_title: false
hide_table_of_contents: false
keywords:
  - transformer
  - b2bi
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>transformer</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transformer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>transformer</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.b2bi.transformer</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>edi_type</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>file_format</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>mapping_template</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>modified_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>sample_document</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>transformer_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>transformer_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
created_at,
edi_type,
file_format,
mapping_template,
modified_at,
name,
sample_document,
status,
tags,
transformer_arn,
transformer_id
FROM awscc.b2bi.transformer
WHERE region = 'us-east-1'
AND data__Identifier = '{TransformerId}';
```

## Permissions

To operate on the <code>transformer</code> resource, the following permissions are required:

### Read
```json
b2bi:GetTransformer,
b2bi:ListTagsForResource
```

### Update
```json
b2bi:TagResource,
b2bi:UntagResource,
b2bi:UpdateTransformer
```

### Delete
```json
b2bi:DeleteTransformer,
logs:DeleteLogDelivery,
logs:ListLogDeliveries
```

