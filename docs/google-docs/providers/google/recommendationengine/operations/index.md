---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - recommendationengine
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recommendationengine.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The standard List next-page token. |
| `operations` | `array` | A list of operations that matches the specified filter in the request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_catalogs_event_stores_operations_list` | `SELECT` | `catalogsId, eventStoresId, locationsId, projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_catalogs_operations_list` | `SELECT` | `catalogsId, locationsId, projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_catalogs_event_stores_operations_get` | `EXEC` | `catalogsId, eventStoresId, locationsId, operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_catalogs_operations_get` | `EXEC` | `catalogsId, locationsId, operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
