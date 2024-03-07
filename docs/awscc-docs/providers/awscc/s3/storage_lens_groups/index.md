---
title: storage_lens_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_lens_groups
  - s3
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>storage_lens_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_lens_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>storage_lens_groups</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.s3.storage_lens_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name
FROM awscc.s3.storage_lens_groups
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>storage_lens_groups</code> resource, the following permissions are required:

### Create
```json
s3:CreateStorageLensGroup,
s3:GetStorageLensGroup,
s3:TagResource,
s3:ListTagsForResource
```

### List
```json
s3:ListStorageLensGroups
```

