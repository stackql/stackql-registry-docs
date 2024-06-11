---
title: entities
hide_title: false
hide_table_of_contents: false
keywords:
  - entities
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

Creates, updates, deletes or gets an <code>entity</code> resource or lists <code>entities</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTTwinMaker::Entity</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iottwinmaker.entities" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="entity_id" /></td><td><code>string</code></td><td>The ID of the entity.</td></tr>
<tr><td><CopyableCode code="entity_name" /></td><td><code>string</code></td><td>The name of the entity.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>object</code></td><td>The current status of the entity.</td></tr>
<tr><td><CopyableCode code="has_child_entities" /></td><td><code>boolean</code></td><td>A Boolean value that specifies whether the entity has child entities or not.</td></tr>
<tr><td><CopyableCode code="parent_entity_id" /></td><td><code>string</code></td><td>The ID of the parent entity.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the entity.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the entity.</td></tr>
<tr><td><CopyableCode code="creation_date_time" /></td><td><code>string</code></td><td>The date and time when the entity was created.</td></tr>
<tr><td><CopyableCode code="update_date_time" /></td><td><code>string</code></td><td>The last date and time when the entity was updated.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
<tr><td><CopyableCode code="workspace_id" /></td><td><code>string</code></td><td>The ID of the workspace.</td></tr>
<tr><td><CopyableCode code="components" /></td><td><code>object</code></td><td>A map that sets information about a component type.</td></tr>
<tr><td><CopyableCode code="composite_components" /></td><td><code>object</code></td><td>A map that sets information about a composite component.</td></tr>
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
    <td><CopyableCode code="WorkspaceId, EntityName, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>entities</code> in a region.
```sql
SELECT
region,
workspace_id,
entity_id
FROM aws.iottwinmaker.entities
WHERE region = 'us-east-1';
```
Gets all properties from an <code>entity</code>.
```sql
SELECT
region,
entity_id,
entity_name,
status,
has_child_entities,
parent_entity_id,
arn,
description,
creation_date_time,
update_date_time,
tags,
workspace_id,
components,
composite_components
FROM aws.iottwinmaker.entities
WHERE region = 'us-east-1' AND data__Identifier = '<WorkspaceId>|<EntityId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>entity</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iottwinmaker.entities (
 EntityName,
 WorkspaceId,
 region
)
SELECT 
'{{ EntityName }}',
 '{{ WorkspaceId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iottwinmaker.entities (
 EntityId,
 EntityName,
 ParentEntityId,
 Description,
 Tags,
 WorkspaceId,
 Components,
 CompositeComponents,
 region
)
SELECT 
 '{{ EntityId }}',
 '{{ EntityName }}',
 '{{ ParentEntityId }}',
 '{{ Description }}',
 '{{ Tags }}',
 '{{ WorkspaceId }}',
 '{{ Components }}',
 '{{ CompositeComponents }}',
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
  - name: entity
    props:
      - name: EntityId
        value: '{{ EntityId }}'
      - name: EntityName
        value: '{{ EntityName }}'
      - name: ParentEntityId
        value: '{{ ParentEntityId }}'
      - name: Description
        value: '{{ Description }}'
      - name: Tags
        value: {}
      - name: WorkspaceId
        value: '{{ WorkspaceId }}'
      - name: Components
        value: {}
      - name: CompositeComponents
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iottwinmaker.entities
WHERE data__Identifier = '<WorkspaceId|EntityId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>entities</code> resource, the following permissions are required:

### Create
```json
iottwinmaker:GetWorkspace,
iottwinmaker:CreateEntity,
iottwinmaker:GetEntity,
iottwinmaker:ListComponents,
iottwinmaker:ListProperties,
iottwinmaker:ListTagsForResource,
iottwinmaker:TagResource
```

### Read
```json
iottwinmaker:GetComponentType,
iottwinmaker:GetEntity,
iottwinmaker:ListComponents,
iottwinmaker:ListProperties,
iottwinmaker:GetWorkspace,
iottwinmaker:ListEntities,
iottwinmaker:ListTagsForResource
```

### Update
```json
iottwinmaker:GetComponentType,
iottwinmaker:GetEntity,
iottwinmaker:ListComponents,
iottwinmaker:ListProperties,
iottwinmaker:GetWorkspace,
iottwinmaker:ListTagsForResource,
iottwinmaker:TagResource,
iottwinmaker:UntagResource,
iottwinmaker:UpdateEntity,
iottwinmaker:UpdateComponentType
```

### Delete
```json
iottwinmaker:GetEntity,
iottwinmaker:GetWorkspace,
iottwinmaker:DeleteEntity
```

### List
```json
iottwinmaker:GetWorkspace,
iottwinmaker:ListTagsForResource,
iottwinmaker:GetEntity,
iottwinmaker:ListEntities
```

