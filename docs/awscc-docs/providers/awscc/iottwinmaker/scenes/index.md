---
title: scenes
hide_title: false
hide_table_of_contents: false
keywords:
  - scenes
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
Retrieves a list of <code>scenes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scenes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>scenes</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iottwinmaker.scenes</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>workspace_id</code></td><td><code>string</code></td><td>The ID of the scene.</td></tr>
<tr><td><code>scene_id</code></td><td><code>string</code></td><td>The ID of the scene.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>scenes</code> resource, the following permissions are required:

### Create
```json
iottwinmaker:CreateScene,
iottwinmaker:GetScene,
iottwinmaker:GetWorkspace,
iottwinmaker:ListTagsForResource,
iottwinmaker:TagResource
```

### List
```json
iottwinmaker:GetWorkspace,
iottwinmaker:ListTagsForResource,
iottwinmaker:ListScenes
```


## Example
```sql
SELECT
region,
workspace_id,
scene_id
FROM awscc.iottwinmaker.scenes
WHERE region = 'us-east-1'
```
