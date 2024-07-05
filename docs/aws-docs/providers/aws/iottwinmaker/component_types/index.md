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

Creates, updates, deletes or gets a <code>component_type</code> resource or lists <code>component_types</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>component_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTTwinMaker::ComponentType</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iottwinmaker.component_types" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="workspace_id" /></td><td><code>string</code></td><td>The ID of the workspace that contains the component type.</td></tr>
<tr><td><CopyableCode code="component_type_id" /></td><td><code>string</code></td><td>The ID of the component type.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the component type.</td></tr>
<tr><td><CopyableCode code="extends_from" /></td><td><code>array</code></td><td>Specifies the parent component type to extend.</td></tr>
<tr><td><CopyableCode code="functions" /></td><td><code>object</code></td><td>a Map of functions in the component type. Each function's key must be unique to this map.</td></tr>
<tr><td><CopyableCode code="is_singleton" /></td><td><code>boolean</code></td><td>A Boolean value that specifies whether an entity can have more than one component of this type.</td></tr>
<tr><td><CopyableCode code="property_definitions" /></td><td><code>object</code></td><td>An map of the property definitions in the component type. Each property definition's key must be unique to this map.</td></tr>
<tr><td><CopyableCode code="property_groups" /></td><td><code>object</code></td><td>An map of the property groups in the component type. Each property group's key must be unique to this map.</td></tr>
<tr><td><CopyableCode code="composite_component_types" /></td><td><code>object</code></td><td>An map of the composite component types in the component type. Each composite component type's key must be unique to this map.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the component type.</td></tr>
<tr><td><CopyableCode code="creation_date_time" /></td><td><code>string</code></td><td>The date and time when the component type was created.</td></tr>
<tr><td><CopyableCode code="update_date_time" /></td><td><code>string</code></td><td>The last date and time when the component type was updated.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>object</code></td><td>The current status of the component type.</td></tr>
<tr><td><CopyableCode code="is_abstract" /></td><td><code>boolean</code></td><td>A Boolean value that specifies whether the component type is abstract.</td></tr>
<tr><td><CopyableCode code="is_schema_initialized" /></td><td><code>boolean</code></td><td>A Boolean value that specifies whether the component type has a schema initializer and that the schema initializer has run.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A map of key-value pairs to associate with a resource.</td></tr>
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
Gets all <code>component_types</code> in a region.
```sql
SELECT
region,
workspace_id,
component_type_id,
description,
extends_from,
functions,
is_singleton,
property_definitions,
property_groups,
composite_component_types,
arn,
creation_date_time,
update_date_time,
status,
is_abstract,
is_schema_initialized,
tags
FROM aws.iottwinmaker.component_types
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>component_type</code>.
```sql
SELECT
region,
workspace_id,
component_type_id,
description,
extends_from,
functions,
is_singleton,
property_definitions,
property_groups,
composite_component_types,
arn,
creation_date_time,
update_date_time,
status,
is_abstract,
is_schema_initialized,
tags
FROM aws.iottwinmaker.component_types
WHERE region = 'us-east-1' AND data__Identifier = '<WorkspaceId>|<ComponentTypeId>';
```

## `INSERT` example

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

## `DELETE` example

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

### Read
```json
iottwinmaker:GetComponentType,
iottwinmaker:GetWorkspace,
iottwinmaker:ListTagsForResource
```

### Update
```json
iottwinmaker:GetComponentType,
iottwinmaker:GetWorkspace,
iottwinmaker:ListTagsForResource,
iottwinmaker:TagResource,
iottwinmaker:UntagResource,
iottwinmaker:UpdateComponentType
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

