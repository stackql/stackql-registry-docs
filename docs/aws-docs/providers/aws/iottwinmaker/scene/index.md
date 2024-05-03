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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>scene</code> resource, use <code>scenes</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scene</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTTwinMaker::Scene</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iottwinmaker.scene" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="scene_id" /></td><td><code>string</code></td><td>The ID of the scene.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the scene.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the scene.</td></tr>
<tr><td><CopyableCode code="content_location" /></td><td><code>string</code></td><td>The relative path that specifies the location of the content definition file.</td></tr>
<tr><td><CopyableCode code="creation_date_time" /></td><td><code>string</code></td><td>The date and time when the scene was created.</td></tr>
<tr><td><CopyableCode code="update_date_time" /></td><td><code>string</code></td><td>The date and time of the current update.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
<tr><td><CopyableCode code="workspace_id" /></td><td><code>string</code></td><td>The ID of the scene.</td></tr>
<tr><td><CopyableCode code="capabilities" /></td><td><code>array</code></td><td>A list of capabilities that the scene uses to render.</td></tr>
<tr><td><CopyableCode code="scene_metadata" /></td><td><code>object</code></td><td>A key-value pair of scene metadata for the scene.</td></tr>
<tr><td><CopyableCode code="generated_scene_metadata" /></td><td><code>object</code></td><td>A key-value pair of generated scene metadata for the scene.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.iottwinmaker.scene
WHERE data__Identifier = '<WorkspaceId>|<SceneId>';
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

