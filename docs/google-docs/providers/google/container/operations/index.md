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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.container.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The server-assigned ID for the operation. |
| <CopyableCode code="clusterConditions" /> | `array` | Which conditions caused the current cluster state. Deprecated. Use field error instead. |
| <CopyableCode code="detail" /> | `string` | Output only. Detailed operation progress, if available. |
| <CopyableCode code="endTime" /> | `string` | Output only. The time the operation completed, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="location" /> | `string` | Output only. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) or [region](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) in which the cluster resides. |
| <CopyableCode code="nodepoolConditions" /> | `array` | Which conditions caused the current node pool state. Deprecated. Use field error instead. |
| <CopyableCode code="operationType" /> | `string` | Output only. The operation type. |
| <CopyableCode code="progress" /> | `object` | Information about operation (or operation stage) progress. |
| <CopyableCode code="selfLink" /> | `string` | Output only. Server-defined URI for the operation. Example: `https://container.googleapis.com/v1alpha1/projects/123/locations/us-central1/operations/operation-123`. |
| <CopyableCode code="startTime" /> | `string` | Output only. The time the operation started, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
| <CopyableCode code="status" /> | `string` | Output only. The current status of the operation. |
| <CopyableCode code="statusMessage" /> | `string` | Output only. If an error has occurred, a textual description of the error. Deprecated. Use the field error instead. |
| <CopyableCode code="targetLink" /> | `string` | Output only. Server-defined URI for the target of the operation. The format of this is a URI to the resource being modified (such as a cluster, node pool, or node). For node pool repairs, there may be multiple nodes being repaired, but only one will be the target. Examples: - ## `https://container.googleapis.com/v1/projects/123/locations/us-central1/clusters/my-cluster` ## `https://container.googleapis.com/v1/projects/123/zones/us-central1-c/clusters/my-cluster/nodePools/my-np` `https://container.googleapis.com/v1/projects/123/zones/us-central1-c/clusters/my-cluster/nodePools/my-np/node/my-node` |
| <CopyableCode code="zone" /> | `string` | Output only. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the operation is taking place. This field is deprecated, use location instead. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_operations_get" /> | `SELECT` | <CopyableCode code="locationsId, operationsId, projectsId" /> | Gets the specified operation. |
| <CopyableCode code="projects_locations_operations_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all operations in a project in a specific zone or all zones. |
| <CopyableCode code="projects_zones_operations_get" /> | `SELECT` | <CopyableCode code="operationId, projectId, zone" /> | Gets the specified operation. |
| <CopyableCode code="projects_zones_operations_list" /> | `SELECT` | <CopyableCode code="projectId, zone" /> | Lists all operations in a project in a specific zone or all zones. |
| <CopyableCode code="projects_locations_operations_cancel" /> | `EXEC` | <CopyableCode code="locationsId, operationsId, projectsId" /> | Cancels the specified operation. |
| <CopyableCode code="projects_zones_operations_cancel" /> | `EXEC` | <CopyableCode code="operationId, projectId, zone" /> | Cancels the specified operation. |

## `SELECT` examples

Lists all operations in a project in a specific zone or all zones.

```sql
SELECT
name,
clusterConditions,
detail,
endTime,
error,
location,
nodepoolConditions,
operationType,
progress,
selfLink,
startTime,
status,
statusMessage,
targetLink,
zone
FROM google.container.operations
WHERE projectId = '{{ projectId }}'
AND zone = '{{ zone }}';
```
