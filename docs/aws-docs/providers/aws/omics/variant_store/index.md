---
title: variant_store
hide_title: false
hide_table_of_contents: false
keywords:
  - variant_store
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>variant_store</code> resource, use <code>variant_stores</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>variant_store</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Omics::VariantStore Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.omics.variant_store" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="reference" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="sse_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status_message" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="store_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="store_size_bytes" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="update_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
creation_time,
description,
id,
name,
reference,
sse_config,
status,
status_message,
store_arn,
store_size_bytes,
tags,
update_time
FROM aws.omics.variant_store
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>variant_store</code> resource, the following permissions are required:

### Read
```json
omics:GetVariantStore
```

### Update
```json
omics:UpdateVariantStore,
omics:TagResource,
omics:UntagResource,
omics:ListTagsForResource,
omics:GetVariantStore
```

### Delete
```json
omics:DeleteVariantStore,
omics:ListVariantStores
```

