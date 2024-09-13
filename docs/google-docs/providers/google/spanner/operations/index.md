---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - spanner
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.spanner.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`. |
| <CopyableCode code="done" /> | `boolean` | If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="metadata" /> | `object` | Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any. |
| <CopyableCode code="response" /> | `object` | The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_instance_configs_operations_get" /> | `SELECT` | <CopyableCode code="instanceConfigsId, operationsId, projectsId" /> | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| <CopyableCode code="projects_instance_configs_operations_list" /> | `SELECT` | <CopyableCode code="instanceConfigsId, projectsId" /> | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| <CopyableCode code="projects_instance_configs_ssd_caches_operations_get" /> | `SELECT` | <CopyableCode code="instanceConfigsId, operationsId, projectsId, ssdCachesId" /> | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| <CopyableCode code="projects_instance_configs_ssd_caches_operations_list" /> | `SELECT` | <CopyableCode code="instanceConfigsId, projectsId, ssdCachesId" /> | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| <CopyableCode code="projects_instances_backups_operations_get" /> | `SELECT` | <CopyableCode code="backupsId, instancesId, operationsId, projectsId" /> | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| <CopyableCode code="projects_instances_backups_operations_list" /> | `SELECT` | <CopyableCode code="backupsId, instancesId, projectsId" /> | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| <CopyableCode code="projects_instances_databases_operations_get" /> | `SELECT` | <CopyableCode code="databasesId, instancesId, operationsId, projectsId" /> | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| <CopyableCode code="projects_instances_databases_operations_list" /> | `SELECT` | <CopyableCode code="databasesId, instancesId, projectsId" /> | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| <CopyableCode code="projects_instances_instance_partitions_operations_get" /> | `SELECT` | <CopyableCode code="instancePartitionsId, instancesId, operationsId, projectsId" /> | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| <CopyableCode code="projects_instances_instance_partitions_operations_list" /> | `SELECT` | <CopyableCode code="instancePartitionsId, instancesId, projectsId" /> | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| <CopyableCode code="projects_instances_operations_get" /> | `SELECT` | <CopyableCode code="instancesId, operationsId, projectsId" /> | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| <CopyableCode code="projects_instances_operations_list" /> | `SELECT` | <CopyableCode code="instancesId, projectsId" /> | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. |
| <CopyableCode code="projects_instance_configs_operations_delete" /> | `DELETE` | <CopyableCode code="instanceConfigsId, operationsId, projectsId" /> | Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. |
| <CopyableCode code="projects_instance_configs_ssd_caches_operations_delete" /> | `DELETE` | <CopyableCode code="instanceConfigsId, operationsId, projectsId, ssdCachesId" /> | Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. |
| <CopyableCode code="projects_instances_backups_operations_delete" /> | `DELETE` | <CopyableCode code="backupsId, instancesId, operationsId, projectsId" /> | Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. |
| <CopyableCode code="projects_instances_databases_operations_delete" /> | `DELETE` | <CopyableCode code="databasesId, instancesId, operationsId, projectsId" /> | Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. |
| <CopyableCode code="projects_instances_instance_partitions_operations_delete" /> | `DELETE` | <CopyableCode code="instancePartitionsId, instancesId, operationsId, projectsId" /> | Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. |
| <CopyableCode code="projects_instances_operations_delete" /> | `DELETE` | <CopyableCode code="instancesId, operationsId, projectsId" /> | Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. |
| <CopyableCode code="projects_instance_configs_operations_cancel" /> | `EXEC` | <CopyableCode code="instanceConfigsId, operationsId, projectsId" /> | Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`. |
| <CopyableCode code="projects_instance_configs_ssd_caches_operations_cancel" /> | `EXEC` | <CopyableCode code="instanceConfigsId, operationsId, projectsId, ssdCachesId" /> | Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`. |
| <CopyableCode code="projects_instances_backups_operations_cancel" /> | `EXEC` | <CopyableCode code="backupsId, instancesId, operationsId, projectsId" /> | Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`. |
| <CopyableCode code="projects_instances_databases_operations_cancel" /> | `EXEC` | <CopyableCode code="databasesId, instancesId, operationsId, projectsId" /> | Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`. |
| <CopyableCode code="projects_instances_instance_partitions_operations_cancel" /> | `EXEC` | <CopyableCode code="instancePartitionsId, instancesId, operationsId, projectsId" /> | Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`. |
| <CopyableCode code="projects_instances_operations_cancel" /> | `EXEC` | <CopyableCode code="instancesId, operationsId, projectsId" /> | Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`. |

## `SELECT` examples

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

```sql
SELECT
name,
done,
error,
metadata,
response
FROM google.spanner.operations
WHERE instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `DELETE` example

Deletes the specified <code>operations</code> resource.

```sql
/*+ delete */
DELETE FROM google.spanner.operations
WHERE instancesId = '{{ instancesId }}'
AND operationsId = '{{ operationsId }}'
AND projectsId = '{{ projectsId }}';
```
