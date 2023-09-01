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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `status` | `string` | The current status of the operation. |
| `selfLink` | `string` | Server-defined URI for the operation. Example: `https://container.googleapis.com/v1alpha1/projects/123/locations/us-central1/operations/operation-123`. |
| `zone` | `string` | The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the operation is taking place. This field is deprecated, use location instead. |
| `clusterConditions` | `array` | Which conditions caused the current cluster state. Deprecated. Use field error instead. |
| `statusMessage` | `string` | Output only. If an error has occurred, a textual description of the error. Deprecated. Use the field error instead. |
| `operationType` | `string` | The operation type. |
| `targetLink` | `string` | Server-defined URI for the target of the operation. The format of this is a URI to the resource being modified (such as a cluster, node pool, or node). For node pool repairs, there may be multiple nodes being repaired, but only one will be the target. Examples: - ## `https://container.googleapis.com/v1/projects/123/locations/us-central1/clusters/my-cluster` ## `https://container.googleapis.com/v1/projects/123/zones/us-central1-c/clusters/my-cluster/nodePools/my-np` `https://container.googleapis.com/v1/projects/123/zones/us-central1-c/clusters/my-cluster/nodePools/my-np/node/my-node` |
| `nodepoolConditions` | `array` | Which conditions caused the current node pool state. Deprecated. Use field error instead. |
| `endTime` | `string` | [Output only] The time the operation completed, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
| `error` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `detail` | `string` | Detailed operation progress, if available. |
| `location` | `string` | [Output only] The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) or [region](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) in which the cluster resides. |
| `startTime` | `string` | [Output only] The time the operation started, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
| `progress` | `object` | Information about operation (or operation stage) progress. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_operations_get` | `SELECT` | `locationsId, operationsId, projectsId` | Gets the specified operation. |
| `projects_locations_operations_list` | `SELECT` | `locationsId, projectsId` | Lists all operations in a project in a specific zone or all zones. |
| `projects_zones_operations_get` | `SELECT` | `operationId, projectId, zone` | Gets the specified operation. |
| `projects_zones_operations_list` | `SELECT` | `projectId, zone` | Lists all operations in a project in a specific zone or all zones. |
| `projects_locations_operations_cancel` | `EXEC` | `locationsId, operationsId, projectsId` | Cancels the specified operation. |
| `projects_zones_operations_cancel` | `EXEC` | `operationId, projectId, zone` | Cancels the specified operation. |
