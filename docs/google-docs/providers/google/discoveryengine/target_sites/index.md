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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.discoveryengine.target_sites" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The fully qualified resource name of the target site. `projects/&#123;project&#125;/locations/&#123;location&#125;/collections/&#123;collection&#125;/dataStores/&#123;data_store&#125;/siteSearchEngine/targetSites/&#123;target_site&#125;` The `target_site_id` is system-generated. |
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
| <CopyableCode code="projects_locations_collections_data_stores_site_search_engine_target_sites_create" /> | `INSERT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Creates a TargetSite. |
| <CopyableCode code="projects_locations_data_stores_site_search_engine_target_sites_create" /> | `INSERT` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Creates a TargetSite. |
| <CopyableCode code="projects_locations_collections_data_stores_site_search_engine_target_sites_delete" /> | `DELETE` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId, targetSitesId" /> | Deletes a TargetSite. |
| <CopyableCode code="projects_locations_data_stores_site_search_engine_target_sites_delete" /> | `DELETE` | <CopyableCode code="dataStoresId, locationsId, projectsId, targetSitesId" /> | Deletes a TargetSite. |
| <CopyableCode code="projects_locations_collections_data_stores_site_search_engine_target_sites_patch" /> | `UPDATE` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId, targetSitesId" /> | Updates a TargetSite. |
| <CopyableCode code="projects_locations_data_stores_site_search_engine_target_sites_patch" /> | `UPDATE` | <CopyableCode code="dataStoresId, locationsId, projectsId, targetSitesId" /> | Updates a TargetSite. |
| <CopyableCode code="_projects_locations_collections_data_stores_site_search_engine_target_sites_list" /> | `EXEC` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Gets a list of TargetSites. |
| <CopyableCode code="_projects_locations_data_stores_site_search_engine_target_sites_list" /> | `EXEC` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Gets a list of TargetSites. |
| <CopyableCode code="projects_locations_collections_data_stores_site_search_engine_target_sites_batch_create" /> | `EXEC` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Creates TargetSite in a batch. |
| <CopyableCode code="projects_locations_data_stores_site_search_engine_target_sites_batch_create" /> | `EXEC` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Creates TargetSite in a batch. |
