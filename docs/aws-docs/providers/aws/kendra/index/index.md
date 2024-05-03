---
title: index
hide_title: false
hide_table_of_contents: false
keywords:
  - index
  - kendra
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

Gets or operates on an individual <code>index</code> resource, use <code>indices</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>index</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A Kendra index</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kendra.index" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the index</td></tr>
<tr><td><CopyableCode code="server_side_encryption_configuration" /></td><td><code>object</code></td><td>Server side encryption configuration</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags for labeling the index</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="edition" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="document_metadata_configurations" /></td><td><code>array</code></td><td>Document metadata configurations</td></tr>
<tr><td><CopyableCode code="capacity_units" /></td><td><code>object</code></td><td>Capacity units</td></tr>
<tr><td><CopyableCode code="user_context_policy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="user_token_configurations" /></td><td><code>array</code></td><td></td></tr>
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
id,
arn,
description,
server_side_encryption_configuration,
tags,
name,
role_arn,
edition,
document_metadata_configurations,
capacity_units,
user_context_policy,
user_token_configurations
FROM aws.kendra.index
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>index</code> resource, the following permissions are required:

### Read
```json
kendra:DescribeIndex,
kendra:ListTagsForResource
```

### Update
```json
kendra:DescribeIndex,
kendra:UpdateIndex,
kendra:ListTagsForResource,
kendra:TagResource,
kendra:UntagResource,
iam:PassRole
```

### Delete
```json
kendra:DescribeIndex,
kendra:DeleteIndex
```

