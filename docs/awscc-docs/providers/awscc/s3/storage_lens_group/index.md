---
title: storage_lens_group
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_lens_group
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
Gets an individual <code>storage_lens_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_lens_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>storage_lens_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.s3.storage_lens_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>filter</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>storage_lens_group_arn</code></td><td><code>string</code></td><td>The ARN for the Amazon S3 Storage Lens Group.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A set of tags (key-value pairs) for this Amazon S3 Storage Lens Group.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
filter,
storage_lens_group_arn,
tags
FROM awscc.s3.storage_lens_group
WHERE region = 'us-east-1'
AND data__Identifier = '{Name}';
```

## Permissions

To operate on the <code>storage_lens_group</code> resource, the following permissions are required:

### Read
```json
s3:GetStorageLensGroup,
s3:ListTagsForResource
```

### Update
```json
s3:GetStorageLensGroup,
s3:UpdateStorageLensGroup,
s3:TagResource,
s3:UntagResource,
s3:ListTagsForResource
```

### Delete
```json
s3:DeleteStorageLensGroup
```

