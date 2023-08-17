---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - retail
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
<tr><td><b>Id</b></td><td><code>google.retail.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/&#123;unique_id&#125;`. |
| `done` | `boolean` | If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available. |
| `error` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `metadata` | `object` | Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any. |
| `response` | `object` | The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_catalogs_operations_list` | `SELECT` | `catalogsId, locationsId, projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_operations_list` | `SELECT` | `locationsId, projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_operations_list` | `SELECT` | `projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `_projects_locations_catalogs_operations_list` | `EXEC` | `catalogsId, locationsId, projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `_projects_locations_operations_list` | `EXEC` | `locationsId, projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `_projects_operations_list` | `EXEC` | `projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| `projects_locations_catalogs_branches_operations_get` | `EXEC` | `branchesId, catalogsId, locationsId, operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_catalogs_operations_get` | `EXEC` | `catalogsId, locationsId, operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_locations_operations_get` | `EXEC` | `locationsId, operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `projects_operations_get` | `EXEC` | `operationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
