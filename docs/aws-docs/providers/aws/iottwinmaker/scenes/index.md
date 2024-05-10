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


Used to retrieve a list of <code>scenes</code> in a region or to create or delete a <code>scenes</code> resource, use <code>scene</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scenes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTTwinMaker::Scene</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iottwinmaker.scenes" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="workspace_id" /></td><td><code>string</code></td><td>The ID of the scene.</td></tr>
<tr><td><CopyableCode code="scene_id" /></td><td><code>string</code></td><td>The ID of the scene.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
workspace_id,
scene_id
FROM aws.iottwinmaker.scenes
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "SceneId": "{{ SceneId }}",
 "ContentLocation": "{{ ContentLocation }}",
 "WorkspaceId": "{{ WorkspaceId }}"
}
>>>
--required properties only
INSERT INTO aws.iottwinmaker.scenes (
 SceneId,
 ContentLocation,
 WorkspaceId,
 region
)
SELECT 
{{ SceneId }},
 {{ ContentLocation }},
 {{ WorkspaceId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "SceneId": "{{ SceneId }}",
 "Description": "{{ Description }}",
 "ContentLocation": "{{ ContentLocation }}",
 "Tags": {},
 "WorkspaceId": "{{ WorkspaceId }}",
 "Capabilities": [
  "{{ Capabilities[0] }}"
 ],
 "SceneMetadata": {}
}
>>>
--all properties
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
 {{ SceneId }},
 {{ Description }},
 {{ ContentLocation }},
 {{ Tags }},
 {{ WorkspaceId }},
 {{ Capabilities }},
 {{ SceneMetadata }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

