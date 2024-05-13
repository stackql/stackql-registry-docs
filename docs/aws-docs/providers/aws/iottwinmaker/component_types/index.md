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
    <td><CopyableCode code="WorkspaceId, ComponentTypeId, region" /></td>
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

Use the following StackQL query and manifest file to create a new <code>component_type</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iottwinmaker.component_types (
 WorkspaceId,
 ComponentTypeId,
 region
)
SELECT 
'{{ WorkspaceId }}',
 '{{ ComponentTypeId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ WorkspaceId }}',
 '{{ ComponentTypeId }}',
 '{{ Description }}',
 '{{ ExtendsFrom }}',
 '{{ Functions }}',
 '{{ IsSingleton }}',
 '{{ PropertyDefinitions }}',
 '{{ PropertyGroups }}',
 '{{ CompositeComponentTypes }}',
 '{{ Tags }}',
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
  - name: component_type
    props:
      - name: WorkspaceId
        value: '{{ WorkspaceId }}'
      - name: ComponentTypeId
        value: '{{ ComponentTypeId }}'
      - name: Description
        value: '{{ Description }}'
      - name: ExtendsFrom
        value:
          - '{{ ExtendsFrom[0] }}'
      - name: Functions
        value: {}
      - name: IsSingleton
        value: '{{ IsSingleton }}'
      - name: PropertyDefinitions
        value: {}
      - name: PropertyGroups
        value: {}
      - name: CompositeComponentTypes
        value: {}
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
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

