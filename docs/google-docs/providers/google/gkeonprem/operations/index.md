---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - gkeonprem
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
<tr><td><b>Id</b></td><td><code>google.gkeonprem.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `operations` | `array` | A list of operations that matches the specified filter in the request. |
| `nextPageToken` | `string` | The standard List next-page token. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_bare_metal_admin_clusters_operations_list` | `SELECT` | `bareMetalAdminClustersId, locationsId, projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_bare_metal_clusters_bare_metal_node_pools_operations_list` | `SELECT` | `bareMetalClustersId, bareMetalNodePoolsId, locationsId, projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_bare_metal_clusters_operations_list` | `SELECT` | `bareMetalClustersId, locationsId, projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_operations_list` | `SELECT` | `locationsId, projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_vmware_admin_clusters_operations_list` | `SELECT` | `locationsId, projectsId, vmwareAdminClustersId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_vmware_clusters_operations_list` | `SELECT` | `locationsId, projectsId, vmwareClustersId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_vmware_clusters_vmware_node_pools_operations_list` | `SELECT` | `locationsId, projectsId, vmwareClustersId, vmwareNodePoolsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_operations_delete` | `DELETE` | `locationsId, operationsId, projectsId` | Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. |
| `projects_locations_bare_metal_admin_clusters_operations_get` | `EXEC` | `bareMetalAdminClustersId, locationsId, operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_bare_metal_clusters_bare_metal_node_pools_operations_get` | `EXEC` | `bareMetalClustersId, bareMetalNodePoolsId, locationsId, operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_bare_metal_clusters_operations_get` | `EXEC` | `bareMetalClustersId, locationsId, operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_operations_cancel` | `EXEC` | `locationsId, operationsId, projectsId` | Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`. |
| `projects_locations_operations_get` | `EXEC` | `locationsId, operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_vmware_admin_clusters_operations_get` | `EXEC` | `locationsId, operationsId, projectsId, vmwareAdminClustersId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_vmware_clusters_operations_get` | `EXEC` | `locationsId, operationsId, projectsId, vmwareClustersId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_vmware_clusters_vmware_node_pools_operations_get` | `EXEC` | `locationsId, operationsId, projectsId, vmwareClustersId, vmwareNodePoolsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
