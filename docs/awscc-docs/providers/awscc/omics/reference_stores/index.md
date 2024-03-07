---
title: reference_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - reference_stores
  - omics
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>reference_stores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reference_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>reference_stores</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.omics.reference_stores</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>reference_store_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
reference_store_id
FROM awscc.omics.reference_stores
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>reference_stores</code> resource, the following permissions are required:

### Create
```json
omics:CreateReferenceStore,
omics:TagResource
```

### List
```json
omics:ListReferenceStores
```

