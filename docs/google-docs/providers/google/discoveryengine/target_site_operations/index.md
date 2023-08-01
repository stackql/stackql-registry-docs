---
title: target_site_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - target_site_operations
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_site_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.discoveryengine.target_site_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `operations` | `array` | A list of operations that matches the specified filter in the request. |
| `nextPageToken` | `string` | The standard List next-page token. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_collections_data_stores_site_search_engine_target_sites_operations_list` | `SELECT` | `collectionsId, dataStoresId, locationsId, projectsId` |
