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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>component_types</code> in a region or to create or delete a <code>component_types</code> resource, use <code>component_type</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>component_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTTwinMaker::ComponentType</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iottwinmaker.component_types" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="workspace_id" /></td><td><code>string</code></td><td>The ID of the workspace that contains the component type.</td></tr>
<tr><td><CopyableCode code="component_type_id" /></td><td><code>string</code></td><td>The ID of the component type.</td></tr>
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
component_type_id
FROM aws.iottwinmaker.component_types
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
 "WorkspaceId": "{{ WorkspaceId }}",
 "ComponentTypeId": "{{ ComponentTypeId }}"
}
>>>
--required properties only
INSERT INTO aws.iottwinmaker.component_types (
 WorkspaceId,
 ComponentTypeId,
 region
)
SELECT 
{{ WorkspaceId }},
 {{ ComponentTypeId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "WorkspaceId": "{{ WorkspaceId }}",
 "ComponentTypeId": "{{ ComponentTypeId }}",
 "Description": "{{ Description }}",
 "ExtendsFrom": [
  "{{ ExtendsFrom[0] }}"
 ],
 "Functions": {},
 "IsSingleton": "{{ IsSingleton }}",
 "PropertyDefinitions": {},
 "PropertyGroups": {},
 "CompositeComponentTypes": {},
 "Tags": {}
}
>>>
--all properties
INSERT INTO aws.iottwinmaker.component_types (
 WorkspaceId,
 ComponentTypeId,
 Description,
 ExtendsFrom,
 Functions,
 IsSingleton,
 PropertyDefinitions,
 PropertyGroups,
 CompositeComponentTypes,
 Tags,
 region
)
SELECT 
 {{ WorkspaceId }},
 {{ ComponentTypeId }},
 {{ Description }},
 {{ ExtendsFrom }},
 {{ Functions }},
 {{ IsSingleton }},
 {{ PropertyDefinitions }},
 {{ PropertyGroups }},
 {{ CompositeComponentTypes }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iottwinmaker.component_types
WHERE data__Identifier = '<WorkspaceId|ComponentTypeId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>component_types</code> resource, the following permissions are required:

### Create
```json
iottwinmaker:CreateComponentType,
iottwinmaker:GetComponentType,
iottwinmaker:GetWorkspace,
iottwinmaker:ListTagsForResource,
iottwinmaker:TagResource
```

### Delete
```json
iottwinmaker:DeleteComponentType,
iottwinmaker:GetComponentType,
iottwinmaker:GetWorkspace
```

### List
```json
iottwinmaker:GetComponentType,
iottwinmaker:GetWorkspace,
iottwinmaker:ListComponentTypes,
iottwinmaker:ListTagsForResource
```

