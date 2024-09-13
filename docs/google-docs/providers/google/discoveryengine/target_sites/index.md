---
title: target_sites
hide_title: false
hide_table_of_contents: false
keywords:
  - target_sites
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

Creates, updates, deletes, gets or lists a <code>target_sites</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.discoveryengine.target_sites" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The fully qualified resource name of the target site. `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine/targetSites/{target_site}` The `target_site_id` is system-generated. |
| <CopyableCode code="exactMatch" /> | `boolean` | Input only. If set to false, a uri_pattern is generated to include all pages whose address contains the provided_uri_pattern. If set to true, an uri_pattern is generated to try to be an exact match of the provided_uri_pattern or just the specific page if the provided_uri_pattern is a specific one. provided_uri_pattern is always normalized to generate the URI pattern to be used by the search engine. |
| <CopyableCode code="failureReason" /> | `object` | Site search indexing failure reasons. |
| <CopyableCode code="generatedUriPattern" /> | `string` | Output only. This is system-generated based on the provided_uri_pattern. |
| <CopyableCode code="indexingStatus" /> | `string` | Output only. Indexing status. |
| <CopyableCode code="providedUriPattern" /> | `string` | Required. Input only. The user provided URI pattern from which the `generated_uri_pattern` is generated. |
| <CopyableCode code="rootDomainUri" /> | `string` | Output only. Root domain of the provided_uri_pattern. |
| <CopyableCode code="siteVerificationInfo" /> | `object` | Verification information for target sites in advanced site search. |
| <CopyableCode code="type" /> | `string` | The type of the target site, e.g., whether the site is to be included or excluded. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The target site's last updated time. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_collections_data_stores_site_search_engine_target_sites_get" /> | `SELECT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId, targetSitesId" /> | Gets a TargetSite. |
| <CopyableCode code="projects_locations_collections_data_stores_site_search_engine_target_sites_list" /> | `SELECT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Gets a list of TargetSites. |
| <CopyableCode code="projects_locations_data_stores_site_search_engine_target_sites_get" /> | `SELECT` | <CopyableCode code="dataStoresId, locationsId, projectsId, targetSitesId" /> | Gets a TargetSite. |
| <CopyableCode code="projects_locations_data_stores_site_search_engine_target_sites_list" /> | `SELECT` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Gets a list of TargetSites. |
| <CopyableCode code="projects_locations_collections_data_stores_site_search_engine_target_sites_batch_create" /> | `INSERT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Creates TargetSite in a batch. |
| <CopyableCode code="projects_locations_collections_data_stores_site_search_engine_target_sites_create" /> | `INSERT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Creates a TargetSite. |
| <CopyableCode code="projects_locations_data_stores_site_search_engine_target_sites_batch_create" /> | `INSERT` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Creates TargetSite in a batch. |
| <CopyableCode code="projects_locations_data_stores_site_search_engine_target_sites_create" /> | `INSERT` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Creates a TargetSite. |
| <CopyableCode code="projects_locations_collections_data_stores_site_search_engine_target_sites_delete" /> | `DELETE` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId, targetSitesId" /> | Deletes a TargetSite. |
| <CopyableCode code="projects_locations_data_stores_site_search_engine_target_sites_delete" /> | `DELETE` | <CopyableCode code="dataStoresId, locationsId, projectsId, targetSitesId" /> | Deletes a TargetSite. |
| <CopyableCode code="projects_locations_collections_data_stores_site_search_engine_target_sites_patch" /> | `UPDATE` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId, targetSitesId" /> | Updates a TargetSite. |
| <CopyableCode code="projects_locations_data_stores_site_search_engine_target_sites_patch" /> | `UPDATE` | <CopyableCode code="dataStoresId, locationsId, projectsId, targetSitesId" /> | Updates a TargetSite. |

## `SELECT` examples

Gets a list of TargetSites.

```sql
SELECT
name,
exactMatch,
failureReason,
generatedUriPattern,
indexingStatus,
providedUriPattern,
rootDomainUri,
siteVerificationInfo,
type,
updateTime
FROM google.discoveryengine.target_sites
WHERE dataStoresId = '{{ dataStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>target_sites</code> resource.

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
INSERT INTO google.discoveryengine.target_sites (
dataStoresId,
locationsId,
projectsId,
requests
)
SELECT 
'{{ dataStoresId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ requests }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: requests
        value: '{{ requests }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>target_sites</code> resource.

```sql
/*+ update */
UPDATE google.discoveryengine.target_sites
SET 
name = '{{ name }}',
providedUriPattern = '{{ providedUriPattern }}',
type = '{{ type }}',
exactMatch = true|false,
generatedUriPattern = '{{ generatedUriPattern }}',
rootDomainUri = '{{ rootDomainUri }}',
siteVerificationInfo = '{{ siteVerificationInfo }}',
indexingStatus = '{{ indexingStatus }}',
updateTime = '{{ updateTime }}',
failureReason = '{{ failureReason }}'
WHERE 
dataStoresId = '{{ dataStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND targetSitesId = '{{ targetSitesId }}';
```

## `DELETE` example

Deletes the specified <code>target_sites</code> resource.

```sql
/*+ delete */
DELETE FROM google.discoveryengine.target_sites
WHERE dataStoresId = '{{ dataStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND targetSitesId = '{{ targetSitesId }}';
```
