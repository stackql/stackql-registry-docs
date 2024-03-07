---
title: image
hide_title: false
hide_table_of_contents: false
keywords:
  - image
  - sagemaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>image</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>image</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sagemaker.image</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>image_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>image_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>image_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>image_display_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>image_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
image_name,
image_arn,
image_role_arn,
image_display_name,
image_description,
tags
FROM awscc.sagemaker.image
WHERE region = 'us-east-1'
AND data__Identifier = '{ImageArn}';
```

## Permissions

To operate on the <code>image</code> resource, the following permissions are required:

### Read
```json
sagemaker:DescribeImage,
sagemaker:ListTags
```

### Update
```json
sagemaker:UpdateImage,
sagemaker:DescribeImage,
sagemaker:ListTags,
sagemaker:AddTags,
sagemaker:DeleteTags,
iam:PassRole
```

### Delete
```json
sagemaker:DeleteImage,
sagemaker:DescribeImage
```

