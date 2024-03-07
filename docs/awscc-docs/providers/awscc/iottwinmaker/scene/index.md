---
title: scene
hide_title: false
hide_table_of_contents: false
keywords:
  - scene
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
Gets an individual <code>scene</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scene</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>scene</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iottwinmaker.scene</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>scene_id</code></td><td><code>string</code></td><td>The ID of the scene.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the scene.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the scene.</td></tr>
<tr><td><code>content_location</code></td><td><code>string</code></td><td>The relative path that specifies the location of the content definition file.</td></tr>
<tr><td><code>creation_date_time</code></td><td><code>string</code></td><td>The date and time when the scene was created.</td></tr>
<tr><td><code>update_date_time</code></td><td><code>string</code></td><td>The date and time of the current update.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
<tr><td><code>workspace_id</code></td><td><code>string</code></td><td>The ID of the scene.</td></tr>
<tr><td><code>capabilities</code></td><td><code>array</code></td><td>A list of capabilities that the scene uses to render.</td></tr>
<tr><td><code>scene_metadata</code></td><td><code>object</code></td><td>A key-value pair of scene metadata for the scene.</td></tr>
<tr><td><code>generated_scene_metadata</code></td><td><code>object</code></td><td>A key-value pair of generated scene metadata for the scene.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
scene_id,
arn,
description,
content_location,
creation_date_time,
update_date_time,
tags,
workspace_id,
capabilities,
scene_metadata,
generated_scene_metadata
FROM awscc.iottwinmaker.scene
WHERE region = 'us-east-1'
AND data__Identifier = '{WorkspaceId}';
AND data__Identifier = '{SceneId}';
```

## Permissions

To operate on the <code>scene</code> resource, the following permissions are required:

### Read
```json
iottwinmaker:GetWorkspace,
iottwinmaker:GetScene,
iottwinmaker:ListTagsForResource
```

### Update
```json
iottwinmaker:GetScene,
iottwinmaker:GetWorkspace,
iottwinmaker:ListTagsForResource,
iottwinmaker:TagResource,
iottwinmaker:UntagResource,
iottwinmaker:UpdateScene
```

### Delete
```json
iottwinmaker:DeleteScene,
iottwinmaker:GetScene,
iottwinmaker:GetWorkspace
```

