---
title: schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - schemas
  - discoveryengine
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

Creates, updates, deletes, gets or lists a <code>schemas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.discoveryengine.schemas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The full resource name of the schema, in the format of `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/schemas/{schema}`. This field must be a UTF-8 encoded string with a length limit of 1024 characters. |
| <CopyableCode code="jsonSchema" /> | `string` | The JSON representation of the schema. |
| <CopyableCode code="structSchema" /> | `object` | The structured representation of the schema. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_collections_data_stores_schemas_get" /> | `SELECT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId, schemasId" /> | Gets a Schema. |
| <CopyableCode code="projects_locations_collections_data_stores_schemas_list" /> | `SELECT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Gets a list of Schemas. |
| <CopyableCode code="projects_locations_data_stores_schemas_get" /> | `SELECT` | <CopyableCode code="dataStoresId, locationsId, projectsId, schemasId" /> | Gets a Schema. |
| <CopyableCode code="projects_locations_data_stores_schemas_list" /> | `SELECT` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Gets a list of Schemas. |
| <CopyableCode code="projects_locations_collections_data_stores_schemas_create" /> | `INSERT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Creates a Schema. |
| <CopyableCode code="projects_locations_data_stores_schemas_create" /> | `INSERT` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Creates a Schema. |
| <CopyableCode code="projects_locations_collections_data_stores_schemas_delete" /> | `DELETE` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId, schemasId" /> | Deletes a Schema. |
| <CopyableCode code="projects_locations_data_stores_schemas_delete" /> | `DELETE` | <CopyableCode code="dataStoresId, locationsId, projectsId, schemasId" /> | Deletes a Schema. |
| <CopyableCode code="projects_locations_collections_data_stores_schemas_patch" /> | `UPDATE` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId, schemasId" /> | Updates a Schema. |
| <CopyableCode code="projects_locations_data_stores_schemas_patch" /> | `UPDATE` | <CopyableCode code="dataStoresId, locationsId, projectsId, schemasId" /> | Updates a Schema. |

## `SELECT` examples

Gets a list of Schemas.

```sql
SELECT
name,
jsonSchema,
structSchema
FROM google.discoveryengine.schemas
WHERE dataStoresId = '{{ dataStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>schemas</code> resource.

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
INSERT INTO google.discoveryengine.schemas (
dataStoresId,
locationsId,
projectsId,
structSchema,
jsonSchema,
name
)
SELECT 
'{{ dataStoresId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ structSchema }}',
'{{ jsonSchema }}',
'{{ name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: structSchema
      value: '{{ structSchema }}'
    - name: jsonSchema
      value: '{{ jsonSchema }}'
    - name: name
      value: '{{ name }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>schemas</code> resource.

```sql
/*+ update */
UPDATE google.discoveryengine.schemas
SET 
structSchema = '{{ structSchema }}',
jsonSchema = '{{ jsonSchema }}',
name = '{{ name }}'
WHERE 
dataStoresId = '{{ dataStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND schemasId = '{{ schemasId }}';
```

## `DELETE` example

Deletes the specified <code>schemas</code> resource.

```sql
/*+ delete */
DELETE FROM google.discoveryengine.schemas
WHERE dataStoresId = '{{ dataStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND schemasId = '{{ schemasId }}';
```
