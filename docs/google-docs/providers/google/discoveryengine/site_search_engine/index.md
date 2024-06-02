---
title: site_search_engine
hide_title: false
hide_table_of_contents: false
keywords:
  - site_search_engine
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
<tr><td><b>Name</b></td><td><code>site_search_engine</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="discoveryengine.site_search_engine" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_collections_data_stores_site_search_engine_batch_verify_target_sites" /> | `EXEC` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Verify target sites' ownership and validity. This API sends all the target sites under site search engine for verification. |
| <CopyableCode code="projects_locations_collections_data_stores_site_search_engine_disable_advanced_site_search" /> | `EXEC` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Downgrade from advanced site search to basic site search. |
| <CopyableCode code="projects_locations_collections_data_stores_site_search_engine_enable_advanced_site_search" /> | `EXEC` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Upgrade from basic site search to advanced site search. |
| <CopyableCode code="projects_locations_collections_data_stores_site_search_engine_recrawl_uris" /> | `EXEC` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Request on-demand recrawl for a list of URIs. |
| <CopyableCode code="projects_locations_data_stores_site_search_engine_disable_advanced_site_search" /> | `EXEC` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Downgrade from advanced site search to basic site search. |
| <CopyableCode code="projects_locations_data_stores_site_search_engine_enable_advanced_site_search" /> | `EXEC` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Upgrade from basic site search to advanced site search. |
| <CopyableCode code="projects_locations_data_stores_site_search_engine_recrawl_uris" /> | `EXEC` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Request on-demand recrawl for a list of URIs. |
