---
title: component_type
hide_title: false
hide_table_of_contents: false
keywords:
  - component_type
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
Gets or operates on an individual <code>component_type</code> resource, use <code>component_types</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>component_type</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTTwinMaker::ComponentType</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iottwinmaker.component_type</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>workspace_id</code></td><td><code>string</code></td><td>The ID of the workspace that contains the component type.</td></tr>
<tr><td><code>component_type_id</code></td><td><code>string</code></td><td>The ID of the component type.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the component type.</td></tr>
<tr><td><code>extends_from</code></td><td><code>array</code></td><td>Specifies the parent component type to extend.</td></tr>
<tr><td><code>functions</code></td><td><code>object</code></td><td>a Map of functions in the component type. Each function's key must be unique to this map.</td></tr>
<tr><td><code>is_singleton</code></td><td><code>boolean</code></td><td>A Boolean value that specifies whether an entity can have more than one component of this type.</td></tr>
<tr><td><code>property_definitions</code></td><td><code>object</code></td><td>An map of the property definitions in the component type. Each property definition's key must be unique to this map.</td></tr>
<tr><td><code>property_groups</code></td><td><code>object</code></td><td>An map of the property groups in the component type. Each property group's key must be unique to this map.</td></tr>
<tr><td><code>composite_component_types</code></td><td><code>object</code></td><td>An map of the composite component types in the component type. Each composite component type's key must be unique to this map.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the component type.</td></tr>
<tr><td><code>creation_date_time</code></td><td><code>string</code></td><td>The date and time when the component type was created.</td></tr>
<tr><td><code>update_date_time</code></td><td><code>string</code></td><td>The last date and time when the component type was updated.</td></tr>
<tr><td><code>status</code></td><td><code>object</code></td><td>The current status of the component type.</td></tr>
<tr><td><code>is_abstract</code></td><td><code>boolean</code></td><td>A Boolean value that specifies whether the component type is abstract.</td></tr>
<tr><td><code>is_schema_initialized</code></td><td><code>boolean</code></td><td>A Boolean value that specifies whether the component type has a schema initializer and that the schema initializer has run.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>A map of key-value pairs to associate with a resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.iottwinmaker.component_type
WHERE data__Identifier = '<WorkspaceId>|<ComponentTypeId>';
```

## Permissions

To operate on the <code>component_type</code> resource, the following permissions are required:

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

