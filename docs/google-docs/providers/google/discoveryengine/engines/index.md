---
title: engines
hide_title: false
hide_table_of_contents: false
keywords:
  - engines
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

Creates, updates, deletes, gets or lists a <code>engines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>engines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.discoveryengine.engines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The fully qualified resource name of the engine. This field must be a UTF-8 encoded string with a length limit of 1024 characters. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}` engine should be 1-63 characters, and valid characters are /a-z0-9*/. Otherwise, an INVALID_ARGUMENT error is returned. |
| <CopyableCode code="chatEngineConfig" /> | `object` | Configurations for a Chat Engine. |
| <CopyableCode code="chatEngineMetadata" /> | `object` | Additional information of a Chat Engine. Fields in this message are output only. |
| <CopyableCode code="commonConfig" /> | `object` | Common configurations for an Engine. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp the Recommendation Engine was created at. |
| <CopyableCode code="dataStoreIds" /> | `array` | The data stores associated with this engine. For SOLUTION_TYPE_SEARCH and SOLUTION_TYPE_RECOMMENDATION type of engines, they can only associate with at most one data store. If solution_type is SOLUTION_TYPE_CHAT, multiple DataStores in the same Collection can be associated here. Note that when used in CreateEngineRequest, one DataStore id must be provided as the system will use it for necessary initializations. |
| <CopyableCode code="displayName" /> | `string` | Required. The display name of the engine. Should be human readable. UTF-8 encoded string with limit of 1024 characters. |
| <CopyableCode code="industryVertical" /> | `string` | The industry vertical that the engine registers. The restriction of the Engine industry vertical is based on DataStore: If unspecified, default to `GENERIC`. Vertical on Engine has to match vertical of the DataStore linked to the engine. |
| <CopyableCode code="searchEngineConfig" /> | `object` | Configurations for a Search Engine. |
| <CopyableCode code="solutionType" /> | `string` | Required. The solutions of the engine. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp the Recommendation Engine was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_collections_engines_get" /> | `SELECT` | <CopyableCode code="collectionsId, enginesId, locationsId, projectsId" /> | Gets a Engine. |
| <CopyableCode code="projects_locations_collections_engines_list" /> | `SELECT` | <CopyableCode code="collectionsId, locationsId, projectsId" /> | Lists all the Engines associated with the project. |
| <CopyableCode code="projects_locations_collections_engines_create" /> | `INSERT` | <CopyableCode code="collectionsId, locationsId, projectsId" /> | Creates a Engine. |
| <CopyableCode code="projects_locations_collections_engines_delete" /> | `DELETE` | <CopyableCode code="collectionsId, enginesId, locationsId, projectsId" /> | Deletes a Engine. |
| <CopyableCode code="projects_locations_collections_engines_patch" /> | `UPDATE` | <CopyableCode code="collectionsId, enginesId, locationsId, projectsId" /> | Updates an Engine |

## `SELECT` examples

Lists all the Engines associated with the project.

```sql
SELECT
name,
chatEngineConfig,
chatEngineMetadata,
commonConfig,
createTime,
dataStoreIds,
displayName,
industryVertical,
searchEngineConfig,
solutionType,
updateTime
FROM google.discoveryengine.engines
WHERE collectionsId = '{{ collectionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>engines</code> resource.

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
INSERT INTO google.discoveryengine.engines (
collectionsId,
locationsId,
projectsId,
chatEngineConfig,
searchEngineConfig,
chatEngineMetadata,
name,
displayName,
createTime,
updateTime,
dataStoreIds,
solutionType,
industryVertical,
commonConfig
)
SELECT 
'{{ collectionsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ chatEngineConfig }}',
'{{ searchEngineConfig }}',
'{{ chatEngineMetadata }}',
'{{ name }}',
'{{ displayName }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ dataStoreIds }}',
'{{ solutionType }}',
'{{ industryVertical }}',
'{{ commonConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: chatEngineConfig
        value: '{{ chatEngineConfig }}'
      - name: searchEngineConfig
        value: '{{ searchEngineConfig }}'
      - name: chatEngineMetadata
        value: '{{ chatEngineMetadata }}'
      - name: name
        value: '{{ name }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: dataStoreIds
        value: '{{ dataStoreIds }}'
      - name: solutionType
        value: '{{ solutionType }}'
      - name: industryVertical
        value: '{{ industryVertical }}'
      - name: commonConfig
        value: '{{ commonConfig }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>engines</code> resource.

```sql
/*+ update */
UPDATE google.discoveryengine.engines
SET 
chatEngineConfig = '{{ chatEngineConfig }}',
searchEngineConfig = '{{ searchEngineConfig }}',
chatEngineMetadata = '{{ chatEngineMetadata }}',
name = '{{ name }}',
displayName = '{{ displayName }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
dataStoreIds = '{{ dataStoreIds }}',
solutionType = '{{ solutionType }}',
industryVertical = '{{ industryVertical }}',
commonConfig = '{{ commonConfig }}'
WHERE 
collectionsId = '{{ collectionsId }}'
AND enginesId = '{{ enginesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>engines</code> resource.

```sql
/*+ delete */
DELETE FROM google.discoveryengine.engines
WHERE collectionsId = '{{ collectionsId }}'
AND enginesId = '{{ enginesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
