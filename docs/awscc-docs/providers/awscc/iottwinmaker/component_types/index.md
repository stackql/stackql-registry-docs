---
title: component_types
hide_title: false
hide_table_of_contents: false
keywords:
  - component_types
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
Retrieves a list of <code>component_types</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>component_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>component_types</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iottwinmaker.component_types</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>workspace_id</code></td><td><code>string</code></td><td>The ID of the workspace that contains the component type.</td></tr>
<tr><td><code>component_type_id</code></td><td><code>string</code></td><td>The ID of the component type.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>component_types</code> resource, the following permissions are required:

### Create
<pre>
iottwinmaker:CreateComponentType,
iottwinmaker:GetComponentType,
iottwinmaker:GetWorkspace,
iottwinmaker:ListTagsForResource,
iottwinmaker:TagResource</pre>

### List
<pre>
iottwinmaker:GetComponentType,
iottwinmaker:GetWorkspace,
iottwinmaker:ListComponentTypes,
iottwinmaker:ListTagsForResource</pre>


## Example
```sql
SELECT
region,
workspace_id,
component_type_id
FROM awscc.iottwinmaker.component_types
WHERE region = 'us-east-1'
```
