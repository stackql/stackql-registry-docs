---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - policysimulator
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
<tr><td><b>Id</b></td><td><code>google.policysimulator.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The standard List next-page token. |
| `operations` | `array` | A list of operations that matches the specified filter in the request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_locations_replays_operations_list` | `SELECT` | `foldersId, locationsId, replaysId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `operations_list` | `SELECT` |  | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `organizations_locations_replays_operations_list` | `SELECT` | `locationsId, organizationsId, replaysId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_replays_operations_list` | `SELECT` | `locationsId, projectsId, replaysId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `folders_locations_replays_operations_get` | `EXEC` | `foldersId, locationsId, operationsId, replaysId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `operations_get` | `EXEC` | `operationsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `organizations_locations_replays_operations_get` | `EXEC` | `locationsId, operationsId, organizationsId, replaysId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_replays_operations_get` | `EXEC` | `locationsId, operationsId, projectsId, replaysId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
