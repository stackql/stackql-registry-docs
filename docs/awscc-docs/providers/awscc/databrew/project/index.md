---
title: project
hide_title: false
hide_table_of_contents: false
keywords:
  - project
  - databrew
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>project</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>project</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>project</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.databrew.project</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>dataset_name</code></td><td><code>string</code></td><td>Dataset name</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Project name</td></tr>
<tr><td><code>recipe_name</code></td><td><code>string</code></td><td>Recipe name</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>Role arn</td></tr>
<tr><td><code>sample</code></td><td><code>object</code></td><td>Sample</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
dataset_name,
name,
recipe_name,
role_arn,
sample,
tags
FROM awscc.databrew.project
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>project</code> resource, the following permissions are required:

### Read
```json
databrew:DescribeProject,
databrew:ListTagsForResource,
iam:ListRoles
```

### Update
```json
databrew:UpdateProject,
iam:PassRole
```

### Delete
```json
databrew:DeleteProject
```

