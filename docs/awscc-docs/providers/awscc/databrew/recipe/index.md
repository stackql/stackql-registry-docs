---
title: recipe
hide_title: false
hide_table_of_contents: false
keywords:
  - recipe
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
Gets an individual <code>recipe</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recipe</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>recipe</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.databrew.recipe</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Description of the recipe</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Recipe name</td></tr>
<tr><td><code>steps</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>recipe</code> resource, the following permissions are required:

### Read
<pre>
databrew:DescribeRecipe,
databrew:ListTagsForResource,
iam:ListRoles</pre>

### Delete
<pre>
databrew:DeleteRecipeVersion</pre>

### Update
<pre>
databrew:UpdateRecipe</pre>


## Example
```sql
SELECT
region,
description,
name,
steps,
tags
FROM awscc.databrew.recipe
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Name&gt;'
```
