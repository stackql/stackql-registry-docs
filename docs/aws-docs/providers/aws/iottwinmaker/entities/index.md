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


Used to retrieve a list of <code>entities</code> in a region or to create or delete a <code>entities</code> resource, use <code>entity</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTTwinMaker::Entity</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iottwinmaker.entities" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="workspace_id" /></td><td><code>string</code></td><td>The ID of the workspace.</td></tr>
<tr><td><CopyableCode code="entity_id" /></td><td><code>string</code></td><td>The ID of the entity.</td></tr>
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
entity_id
FROM aws.iottwinmaker.entities
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- entity.iql (required properties only)
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
-- entity.iql (all properties)
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

## `DELETE` Example

```sql
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

