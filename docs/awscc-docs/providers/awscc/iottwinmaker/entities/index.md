---
title: entities
hide_title: false
hide_table_of_contents: false
keywords:
  - entities
  - iottwinmaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>entities</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>entities</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iottwinmaker.entities</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>workspace_id</code></td><td><code>string</code></td><td>The ID of the workspace.</td></tr>
<tr><td><code>entity_id</code></td><td><code>string</code></td><td>The ID of the entity.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>entities</code> resource, the following permissions are required:

### Create
<pre>
iottwinmaker:GetWorkspace,
iottwinmaker:CreateEntity,
iottwinmaker:GetEntity,
iottwinmaker:ListComponents,
iottwinmaker:ListProperties,
iottwinmaker:ListTagsForResource,
iottwinmaker:TagResource</pre>

### List
<pre>
iottwinmaker:GetWorkspace,
iottwinmaker:ListTagsForResource,
iottwinmaker:GetEntity,
iottwinmaker:ListEntities</pre>


## Example
```sql
SELECT
region,
workspace_id,
entity_id
FROM awscc.iottwinmaker.entities
WHERE region = 'us-east-1'
```
