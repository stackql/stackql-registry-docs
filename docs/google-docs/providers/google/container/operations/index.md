---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - container
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.container.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The server-assigned ID for the operation. |
| `endTime` | `string` | [Output only] The time the operation completed, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
| `error` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `clusterConditions` | `array` | Which conditions caused the current cluster state. Deprecated. Use field error instead. |
| `progress` | `object` | Information about operation (or operation stage) progress. |
| `detail` | `string` | Detailed operation progress, if available. |
| `startTime` | `string` | [Output only] The time the operation started, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
| `status` | `string` | The current status of the operation. |
| `selfLink` | `string` | Server-defined URL for the resource. |
| `targetLink` | `string` | Server-defined URL for the target of the operation. |
| `location` | `string` | [Output only] The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) or [region](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) in which the cluster resides. |
| `operationType` | `string` | The operation type. |
| `statusMessage` | `string` | Output only. If an error has occurred, a textual description of the error. Deprecated. Use the field error instead. |
| `nodepoolConditions` | `array` | Which conditions caused the current node pool state. Deprecated. Use field error instead. |
| `zone` | `string` | The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the operation is taking place. This field is deprecated, use location instead. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_operations_get` | `SELECT` | `locationsId, operationsId, projectsId` | Gets the specified operation. |
| `projects_locations_operations_list` | `SELECT` | `locationsId, projectsId` | Lists all operations in a project in a specific zone or all zones. |
| `projects_zones_operations_get` | `SELECT` | `operationId, projectId, zone` | Gets the specified operation. |
| `projects_zones_operations_list` | `SELECT` | `projectId, zone` | Lists all operations in a project in a specific zone or all zones. |
| `projects_locations_operations_cancel` | `EXEC` | `locationsId, operationsId, projectsId` | Cancels the specified operation. |
| `projects_zones_operations_cancel` | `EXEC` | `operationId, projectId, zone` | Cancels the specified operation. |
