---
title: entities
hide_title: false
hide_table_of_contents: false
keywords:
  - entities
  - connectors
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>entities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.connectors.entities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the Entity. Format: projects/{project}/locations/{location}/connections/{connection}/entityTypes/{type}/entities/{id} |
| <CopyableCode code="fields" /> | `object` | Fields of the entity. The key is name of the field and the value contains the applicable `google.protobuf.Value` entry for this field. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionsId, entitiesId, entityTypesId, locationsId, projectsId" /> | Gets a single entity row matching the entity type and entity id specified in the request. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="connectionsId, entityTypesId, locationsId, projectsId" /> | Lists entity rows of a particular entity type contained in the request. Note: 1. Currently, only max of one 'sort_by' column is supported. 2. If no 'sort_by' column is provided, the primary key of the table is used. If zero or more than one primary key is available, we default to the unpaginated list entities logic which only returns the first page. 3. The values of the 'sort_by' columns must uniquely identify an entity row, otherwise undefined behaviors may be observed during pagination. 4. Since transactions are not supported, any updates, inserts or deletes during pagination can lead to stale data being returned or other unexpected behaviors. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="connectionsId, entityTypesId, locationsId, projectsId" /> | Creates a new entity row of the specified entity type in the external system. The field values for creating the row are contained in the body of the request. The response message contains a `Entity` message object returned as a response by the external system. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionsId, entitiesId, entityTypesId, locationsId, projectsId" /> | Deletes an existing entity row matching the entity type and entity id specified in the request. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="connectionsId, entitiesId, entityTypesId, locationsId, projectsId" /> | Updates an existing entity row matching the entity type and entity id specified in the request. The fields in the entity row that need to be modified are contained in the body of the request. All unspecified fields are left unchanged. The response message contains a `Entity` message object returned as a response by the external system. |

## `SELECT` examples

Lists entity rows of a particular entity type contained in the request. Note: 1. Currently, only max of one 'sort_by' column is supported. 2. If no 'sort_by' column is provided, the primary key of the table is used. If zero or more than one primary key is available, we default to the unpaginated list entities logic which only returns the first page. 3. The values of the 'sort_by' columns must uniquely identify an entity row, otherwise undefined behaviors may be observed during pagination. 4. Since transactions are not supported, any updates, inserts or deletes during pagination can lead to stale data being returned or other unexpected behaviors.

```sql
SELECT
name,
fields
FROM google.connectors.entities
WHERE connectionsId = '{{ connectionsId }}'
AND entityTypesId = '{{ entityTypesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>entities</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.connectors.entities (
connectionsId,
entityTypesId,
locationsId,
projectsId,
name,
fields
)
SELECT 
'{{ connectionsId }}',
'{{ entityTypesId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ fields }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: fields
        value: '{{ fields }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>entities</code> resource.

```sql
/*+ update */
UPDATE google.connectors.entities
SET 
name = '{{ name }}',
fields = '{{ fields }}'
WHERE 
connectionsId = '{{ connectionsId }}'
AND entitiesId = '{{ entitiesId }}'
AND entityTypesId = '{{ entityTypesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>entities</code> resource.

```sql
/*+ delete */
DELETE FROM google.connectors.entities
WHERE connectionsId = '{{ connectionsId }}'
AND entitiesId = '{{ entitiesId }}'
AND entityTypesId = '{{ entityTypesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
