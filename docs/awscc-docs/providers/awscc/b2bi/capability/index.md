---
title: capability
hide_title: false
hide_table_of_contents: false
keywords:
  - capability
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
Gets an individual <code>capability</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capability</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>capability</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.b2bi.capability</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>capability_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>capability_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>configuration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>instructions_documents</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>modified_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
capability_arn,
capability_id,
configuration,
created_at,
instructions_documents,
modified_at,
name,
tags,
type
FROM awscc.b2bi.capability
WHERE data__Identifier = '<CapabilityId>';
```

## Permissions

To operate on the <code>capability</code> resource, the following permissions are required:

### Read
```json
b2bi:GetCapability,
b2bi:ListTagsForResource
```

### Update
```json
b2bi:TagResource,
b2bi:UntagResource,
b2bi:UpdateCapability
```

### Delete
```json
b2bi:DeleteCapability
```

