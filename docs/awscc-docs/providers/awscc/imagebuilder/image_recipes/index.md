---
title: image_recipes
hide_title: false
hide_table_of_contents: false
keywords:
  - image_recipes
  - imagebuilder
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>image_recipes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_recipes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>image_recipes</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.imagebuilder.image_recipes</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the image recipe.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>image_recipes</code> resource, the following permissions are required:

### Create
```json
iam:GetRole,
iam:CreateServiceLinkedRole,
imagebuilder:GetComponent,
imagebuilder:GetImage,
imagebuilder:TagResource,
imagebuilder:GetImageRecipe,
imagebuilder:CreateImageRecipe,
ec2:DescribeImages
```

### List
```json
imagebuilder:ListImageRecipes
```


## Example
```sql
SELECT
region,
arn
FROM awscc.imagebuilder.image_recipes
WHERE region = 'us-east-1'
```
