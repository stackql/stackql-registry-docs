---
title: data_stores_site_search_engine
hide_title: false
hide_table_of_contents: false
keywords:
  - data_stores_site_search_engine
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
<tr><td><b>Name</b></td><td><code>data_stores_site_search_engine</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.discoveryengine.data_stores_site_search_engine" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_locations_collections_data_stores_get_site_search_engine" /> | `SELECT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> |
| <CopyableCode code="projects_locations_data_stores_get_site_search_engine" /> | `SELECT` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> |