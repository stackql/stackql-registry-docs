---
title: accessor
hide_title: false
hide_table_of_contents: false
keywords:
  - accessor
  - managedblockchain
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>accessor</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accessor</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>accessor</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.managedblockchain.accessor</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>billing_token</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>creation_date</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>accessor_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>network_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
billing_token,
creation_date,
id,
status,
accessor_type,
network_type,
tags
FROM awscc.managedblockchain.accessor
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>accessor</code> resource, the following permissions are required:

### Read
```json
managedblockchain:GetAccessor
```

### Update
```json
managedblockchain:GetAccessor,
managedblockchain:CreateAccessor,
managedblockchain:TagResource,
managedblockchain:UntagResource
```

### Delete
```json
managedblockchain:DeleteAccessor
```

