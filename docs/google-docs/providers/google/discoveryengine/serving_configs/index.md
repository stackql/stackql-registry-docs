---
title: serving_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - serving_configs
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
<tr><td><b>Name</b></td><td><code>serving_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.discoveryengine.serving_configs" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_collections_data_stores_serving_configs_answer" /> | `EXEC` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId, servingConfigsId" /> | Answer query method. |
| <CopyableCode code="projects_locations_collections_data_stores_serving_configs_recommend" /> | `EXEC` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId, servingConfigsId" /> | Makes a recommendation, which requires a contextual user event. |
| <CopyableCode code="projects_locations_collections_data_stores_serving_configs_search" /> | `EXEC` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId, servingConfigsId" /> | Performs a search. |
| <CopyableCode code="projects_locations_collections_engines_serving_configs_answer" /> | `EXEC` | <CopyableCode code="collectionsId, enginesId, locationsId, projectsId, servingConfigsId" /> | Answer query method. |
| <CopyableCode code="projects_locations_collections_engines_serving_configs_recommend" /> | `EXEC` | <CopyableCode code="collectionsId, enginesId, locationsId, projectsId, servingConfigsId" /> | Makes a recommendation, which requires a contextual user event. |
| <CopyableCode code="projects_locations_collections_engines_serving_configs_search" /> | `EXEC` | <CopyableCode code="collectionsId, enginesId, locationsId, projectsId, servingConfigsId" /> | Performs a search. |
| <CopyableCode code="projects_locations_data_stores_serving_configs_answer" /> | `EXEC` | <CopyableCode code="dataStoresId, locationsId, projectsId, servingConfigsId" /> | Answer query method. |
| <CopyableCode code="projects_locations_data_stores_serving_configs_recommend" /> | `EXEC` | <CopyableCode code="dataStoresId, locationsId, projectsId, servingConfigsId" /> | Makes a recommendation, which requires a contextual user event. |
| <CopyableCode code="projects_locations_data_stores_serving_configs_search" /> | `EXEC` | <CopyableCode code="dataStoresId, locationsId, projectsId, servingConfigsId" /> | Performs a search. |
