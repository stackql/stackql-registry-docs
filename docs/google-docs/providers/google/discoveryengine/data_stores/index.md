
---
title: data_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - data_stores
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

Creates, updates, deletes or gets an <code>data_store</code> resource or lists <code>data_stores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.discoveryengine.data_stores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The full resource name of the data store. Format: `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}`. This field must be a UTF-8 encoded string with a length limit of 1024 characters. |
| <CopyableCode code="contentConfig" /> | `string` | Immutable. The content config of the data store. If this field is unset, the server behavior defaults to ContentConfig.NO_CONTENT. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp the DataStore was created at. |
| <CopyableCode code="defaultSchemaId" /> | `string` | Output only. The id of the default Schema asscociated to this data store. |
| <CopyableCode code="displayName" /> | `string` | Required. The data store display name. This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned. |
| <CopyableCode code="documentProcessingConfig" /> | `object` | A singleton resource of DataStore. It's empty when DataStore is created, which defaults to digital parser. The first call to DataStoreService.UpdateDocumentProcessingConfig method will initialize the config. |
| <CopyableCode code="industryVertical" /> | `string` | Immutable. The industry vertical that the data store registers. |
| <CopyableCode code="servingConfigDataStore" /> | `object` | Stores information regarding the serving configurations at DataStore level. |
| <CopyableCode code="solutionTypes" /> | `array` | The solutions that the data store enrolls. Available solutions for each industry_vertical: * `MEDIA`: `SOLUTION_TYPE_RECOMMENDATION` and `SOLUTION_TYPE_SEARCH`. * `SITE_SEARCH`: `SOLUTION_TYPE_SEARCH` is automatically enrolled. Other solutions cannot be enrolled. |
| <CopyableCode code="startingSchema" /> | `object` | Defines the structure and layout of a type of document data. |
| <CopyableCode code="workspaceConfig" /> | `object` | Config to store data store type configuration for workspace data |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_collections_data_stores_get" /> | `SELECT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Gets a DataStore. |
| <CopyableCode code="projects_locations_collections_data_stores_list" /> | `SELECT` | <CopyableCode code="collectionsId, locationsId, projectsId" /> | Lists all the DataStores associated with the project. |
| <CopyableCode code="projects_locations_data_stores_get" /> | `SELECT` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Gets a DataStore. |
| <CopyableCode code="projects_locations_data_stores_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all the DataStores associated with the project. |
| <CopyableCode code="projects_locations_collections_data_stores_create" /> | `INSERT` | <CopyableCode code="collectionsId, locationsId, projectsId" /> | Creates a DataStore. DataStore is for storing Documents. To serve these documents for Search, or Recommendation use case, an Engine needs to be created separately. |
| <CopyableCode code="projects_locations_data_stores_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a DataStore. DataStore is for storing Documents. To serve these documents for Search, or Recommendation use case, an Engine needs to be created separately. |
| <CopyableCode code="projects_locations_collections_data_stores_delete" /> | `DELETE` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Deletes a DataStore. |
| <CopyableCode code="projects_locations_data_stores_delete" /> | `DELETE` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Deletes a DataStore. |
| <CopyableCode code="projects_locations_collections_data_stores_patch" /> | `UPDATE` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Updates a DataStore |
| <CopyableCode code="projects_locations_data_stores_patch" /> | `UPDATE` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Updates a DataStore |
| <CopyableCode code="projects_locations_collections_data_stores_complete_query" /> | `EXEC` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Completes the specified user input with keyword suggestions. |
| <CopyableCode code="projects_locations_collections_data_stores_train_custom_model" /> | `EXEC` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Trains a custom model. |
| <CopyableCode code="projects_locations_data_stores_complete_query" /> | `EXEC` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Completes the specified user input with keyword suggestions. |

## `SELECT` examples

Lists all the DataStores associated with the project.

```sql
SELECT
name,
contentConfig,
createTime,
defaultSchemaId,
displayName,
documentProcessingConfig,
industryVertical,
servingConfigDataStore,
solutionTypes,
startingSchema,
workspaceConfig
FROM google.discoveryengine.data_stores
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_stores</code> resource.

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
INSERT INTO google.discoveryengine.data_stores (
locationsId,
projectsId,
name,
displayName,
industryVertical,
solutionTypes,
defaultSchemaId,
contentConfig,
createTime,
workspaceConfig,
documentProcessingConfig,
startingSchema,
servingConfigDataStore
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ industryVertical }}',
'{{ solutionTypes }}',
'{{ defaultSchemaId }}',
'{{ contentConfig }}',
'{{ createTime }}',
'{{ workspaceConfig }}',
'{{ documentProcessingConfig }}',
'{{ startingSchema }}',
'{{ servingConfigDataStore }}'
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
      - name: displayName
        value: '{{ displayName }}'
      - name: industryVertical
        value: '{{ industryVertical }}'
      - name: solutionTypes
        value: '{{ solutionTypes }}'
      - name: defaultSchemaId
        value: '{{ defaultSchemaId }}'
      - name: contentConfig
        value: '{{ contentConfig }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: workspaceConfig
        value: '{{ workspaceConfig }}'
      - name: documentProcessingConfig
        value: '{{ documentProcessingConfig }}'
      - name: startingSchema
        value: '{{ startingSchema }}'
      - name: servingConfigDataStore
        value: '{{ servingConfigDataStore }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a data_store only if the necessary resources are available.

```sql
UPDATE google.discoveryengine.data_stores
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
industryVertical = '{{ industryVertical }}',
solutionTypes = '{{ solutionTypes }}',
defaultSchemaId = '{{ defaultSchemaId }}',
contentConfig = '{{ contentConfig }}',
createTime = '{{ createTime }}',
workspaceConfig = '{{ workspaceConfig }}',
documentProcessingConfig = '{{ documentProcessingConfig }}',
startingSchema = '{{ startingSchema }}',
servingConfigDataStore = '{{ servingConfigDataStore }}'
WHERE 
dataStoresId = '{{ dataStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified data_store resource.

```sql
DELETE FROM google.discoveryengine.data_stores
WHERE dataStoresId = '{{ dataStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
