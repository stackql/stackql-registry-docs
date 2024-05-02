---
title: faq
hide_title: false
hide_table_of_contents: false
keywords:
  - faq
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
Gets or operates on an individual <code>faq</code> resource, use <code>faqs</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>faq</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A Kendra FAQ resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.kendra.faq</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>index_id</code></td><td><code>string</code></td><td>Index ID</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>FAQ name</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>FAQ description</td></tr>
<tr><td><code>file_format</code></td><td><code>string</code></td><td>FAQ file format</td></tr>
<tr><td><code>s3_path</code></td><td><code>object</code></td><td>FAQ S3 path</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>FAQ role ARN</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Tags for labeling the FAQ</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>language_code</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id,
index_id,
name,
description,
file_format,
s3_path,
role_arn,
tags,
arn,
language_code
FROM aws.kendra.faq
WHERE data__Identifier = '<Id>|<IndexId>';
```

## Permissions

To operate on the <code>faq</code> resource, the following permissions are required:

### Update
```json
kendra:ListTagsForResource,
kendra:UntagResource,
kendra:TagResource
```

### Read
```json
kendra:DescribeFaq,
kendra:ListTagsForResource
```

### Delete
```json
kendra:DeleteFaq,
kendra:DescribeFaq
```

