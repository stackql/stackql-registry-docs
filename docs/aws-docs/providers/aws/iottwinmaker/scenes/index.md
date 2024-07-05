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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>scene</code> resource or lists <code>scenes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scenes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTTwinMaker::Scene</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iottwinmaker.scenes" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="scene_id" /></td><td><code>string</code></td><td>The ID of the scene.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="WorkspaceId, SceneId, ContentLocation, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>scenes</code> in a region.
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
FROM aws.iottwinmaker.scenes
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>scene</code>.
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
FROM aws.iottwinmaker.scenes
WHERE region = 'us-east-1' AND data__Identifier = '<WorkspaceId>|<SceneId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scene</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.iottwinmaker.scenes (
 SceneId,
 ContentLocation,
 WorkspaceId,
 region
)
SELECT 
'{{ SceneId }}',
 '{{ ContentLocation }}',
 '{{ WorkspaceId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iottwinmaker.scenes (
 SceneId,
 Description,
 ContentLocation,
 Tags,
 WorkspaceId,
 Capabilities,
 SceneMetadata,
 region
)
SELECT 
 '{{ SceneId }}',
 '{{ Description }}',
 '{{ ContentLocation }}',
 '{{ Tags }}',
 '{{ WorkspaceId }}',
 '{{ Capabilities }}',
 '{{ SceneMetadata }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: scene
    props:
      - name: SceneId
        value: '{{ SceneId }}'
      - name: Description
        value: '{{ Description }}'
      - name: ContentLocation
        value: '{{ ContentLocation }}'
      - name: Tags
        value: {}
      - name: WorkspaceId
        value: '{{ WorkspaceId }}'
      - name: Capabilities
        value:
          - '{{ Capabilities[0] }}'
      - name: SceneMetadata
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iottwinmaker.scenes
WHERE data__Identifier = '<WorkspaceId|SceneId>'
AND region = 'us-east-1';
```

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

### List
```json
iottwinmaker:GetWorkspace,
iottwinmaker:ListTagsForResource,
iottwinmaker:ListScenes
```

