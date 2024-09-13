---
title: controls
hide_title: false
hide_table_of_contents: false
keywords:
  - controls
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

Creates, updates, deletes, gets or lists a <code>controls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.discoveryengine.controls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Fully qualified name `projects/*/locations/global/dataStore/*/controls/*` |
| <CopyableCode code="associatedServingConfigIds" /> | `array` | Output only. List of all ServingConfig IDs this control is attached to. May take up to 10 minutes to update after changes. |
| <CopyableCode code="boostAction" /> | `object` | Adjusts order of products in returned list. |
| <CopyableCode code="conditions" /> | `array` | Determines when the associated action will trigger. Omit to always apply the action. Currently only a single condition may be specified. Otherwise an INVALID ARGUMENT error is thrown. |
| <CopyableCode code="displayName" /> | `string` | Required. Human readable name. The identifier used in UI views. Must be UTF-8 encoded string. Length limit is 128 characters. Otherwise an INVALID ARGUMENT error is thrown. |
| <CopyableCode code="filterAction" /> | `object` | Specified which products may be included in results. Uses same filter as boost. |
| <CopyableCode code="redirectAction" /> | `object` | Redirects a shopper to the provided URI. |
| <CopyableCode code="solutionType" /> | `string` | Required. Immutable. What solution the control belongs to. Must be compatible with vertical of resource. Otherwise an INVALID ARGUMENT error is thrown. |
| <CopyableCode code="synonymsAction" /> | `object` | Creates a set of terms that will act as synonyms of one another. Example: "happy" will also be considered as "glad", "glad" will also be considered as "happy". |
| <CopyableCode code="useCases" /> | `array` | Specifies the use case for the control. Affects what condition fields can be set. Only applies to SOLUTION_TYPE_SEARCH. Currently only allow one use case per control. Must be set when solution_type is SolutionType.SOLUTION_TYPE_SEARCH. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_collections_data_stores_controls_get" /> | `SELECT` | <CopyableCode code="collectionsId, controlsId, dataStoresId, locationsId, projectsId" /> | Gets a Control. |
| <CopyableCode code="projects_locations_collections_data_stores_controls_list" /> | `SELECT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Lists all Controls by their parent DataStore. |
| <CopyableCode code="projects_locations_collections_engines_controls_get" /> | `SELECT` | <CopyableCode code="collectionsId, controlsId, enginesId, locationsId, projectsId" /> | Gets a Control. |
| <CopyableCode code="projects_locations_collections_engines_controls_list" /> | `SELECT` | <CopyableCode code="collectionsId, enginesId, locationsId, projectsId" /> | Lists all Controls by their parent DataStore. |
| <CopyableCode code="projects_locations_data_stores_controls_get" /> | `SELECT` | <CopyableCode code="controlsId, dataStoresId, locationsId, projectsId" /> | Gets a Control. |
| <CopyableCode code="projects_locations_data_stores_controls_list" /> | `SELECT` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Lists all Controls by their parent DataStore. |
| <CopyableCode code="projects_locations_collections_data_stores_controls_create" /> | `INSERT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Creates a Control. By default 1000 controls are allowed for a data store. A request can be submitted to adjust this limit. If the Control to create already exists, an ALREADY_EXISTS error is returned. |
| <CopyableCode code="projects_locations_collections_engines_controls_create" /> | `INSERT` | <CopyableCode code="collectionsId, enginesId, locationsId, projectsId" /> | Creates a Control. By default 1000 controls are allowed for a data store. A request can be submitted to adjust this limit. If the Control to create already exists, an ALREADY_EXISTS error is returned. |
| <CopyableCode code="projects_locations_data_stores_controls_create" /> | `INSERT` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Creates a Control. By default 1000 controls are allowed for a data store. A request can be submitted to adjust this limit. If the Control to create already exists, an ALREADY_EXISTS error is returned. |
| <CopyableCode code="projects_locations_collections_data_stores_controls_delete" /> | `DELETE` | <CopyableCode code="collectionsId, controlsId, dataStoresId, locationsId, projectsId" /> | Deletes a Control. If the Control to delete does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="projects_locations_collections_engines_controls_delete" /> | `DELETE` | <CopyableCode code="collectionsId, controlsId, enginesId, locationsId, projectsId" /> | Deletes a Control. If the Control to delete does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="projects_locations_data_stores_controls_delete" /> | `DELETE` | <CopyableCode code="controlsId, dataStoresId, locationsId, projectsId" /> | Deletes a Control. If the Control to delete does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="projects_locations_collections_data_stores_controls_patch" /> | `UPDATE` | <CopyableCode code="collectionsId, controlsId, dataStoresId, locationsId, projectsId" /> | Updates a Control. Control action type cannot be changed. If the Control to update does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="projects_locations_collections_engines_controls_patch" /> | `UPDATE` | <CopyableCode code="collectionsId, controlsId, enginesId, locationsId, projectsId" /> | Updates a Control. Control action type cannot be changed. If the Control to update does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="projects_locations_data_stores_controls_patch" /> | `UPDATE` | <CopyableCode code="controlsId, dataStoresId, locationsId, projectsId" /> | Updates a Control. Control action type cannot be changed. If the Control to update does not exist, a NOT_FOUND error is returned. |

## `SELECT` examples

Lists all Controls by their parent DataStore.

```sql
SELECT
name,
associatedServingConfigIds,
boostAction,
conditions,
displayName,
filterAction,
redirectAction,
solutionType,
synonymsAction,
useCases
FROM google.discoveryengine.controls
WHERE dataStoresId = '{{ dataStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>controls</code> resource.

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
INSERT INTO google.discoveryengine.controls (
dataStoresId,
locationsId,
projectsId,
boostAction,
filterAction,
redirectAction,
synonymsAction,
name,
displayName,
associatedServingConfigIds,
solutionType,
useCases,
conditions
)
SELECT 
'{{ dataStoresId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ boostAction }}',
'{{ filterAction }}',
'{{ redirectAction }}',
'{{ synonymsAction }}',
'{{ name }}',
'{{ displayName }}',
'{{ associatedServingConfigIds }}',
'{{ solutionType }}',
'{{ useCases }}',
'{{ conditions }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: boostAction
        value: '{{ boostAction }}'
      - name: filterAction
        value: '{{ filterAction }}'
      - name: redirectAction
        value: '{{ redirectAction }}'
      - name: synonymsAction
        value: '{{ synonymsAction }}'
      - name: name
        value: '{{ name }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: associatedServingConfigIds
        value: '{{ associatedServingConfigIds }}'
      - name: solutionType
        value: '{{ solutionType }}'
      - name: useCases
        value: '{{ useCases }}'
      - name: conditions
        value: '{{ conditions }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>controls</code> resource.

```sql
/*+ update */
UPDATE google.discoveryengine.controls
SET 
boostAction = '{{ boostAction }}',
filterAction = '{{ filterAction }}',
redirectAction = '{{ redirectAction }}',
synonymsAction = '{{ synonymsAction }}',
name = '{{ name }}',
displayName = '{{ displayName }}',
associatedServingConfigIds = '{{ associatedServingConfigIds }}',
solutionType = '{{ solutionType }}',
useCases = '{{ useCases }}',
conditions = '{{ conditions }}'
WHERE 
controlsId = '{{ controlsId }}'
AND dataStoresId = '{{ dataStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>controls</code> resource.

```sql
/*+ delete */
DELETE FROM google.discoveryengine.controls
WHERE controlsId = '{{ controlsId }}'
AND dataStoresId = '{{ dataStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
