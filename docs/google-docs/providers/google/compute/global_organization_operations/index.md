---
title: global_organization_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - global_organization_operations
  - compute
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
<tr><td><b>Name</b></td><td><code>global_organization_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.global_organization_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the operation. This identifier is defined by the server. |
| `name` | `string` | [Output Only] Name of the operation. |
| `description` | `string` | [Output Only] A textual description of the operation, which is set when the operation is created. |
| `kind` | `string` | [Output Only] Type of the resource. Always `compute#operation` for Operation resources. |
| `progress` | `integer` | [Output Only] An optional progress indicator that ranges from 0 to 100. There is no requirement that this be linear or support any granularity of operations. This should not be used to guess when the operation will be complete. This number should monotonically increase as the operation progresses. |
| `status` | `string` | [Output Only] The status of the operation, which can be one of the following: `PENDING`, `RUNNING`, or `DONE`. |
| `operationType` | `string` | [Output Only] The type of operation, such as `insert`, `update`, or `delete`, and so on. |
| `warnings` | `array` | [Output Only] If warning messages are generated during processing of the operation, this field will be populated. |
| `user` | `string` | [Output Only] User who requested the operation, for example: `user@example.com`. |
| `insertTime` | `string` | [Output Only] The time that this operation was requested. This value is in RFC3339 text format. |
| `error` | `object` | [Output Only] If errors are generated during processing of the operation, this field will be populated. |
| `endTime` | `string` | [Output Only] The time that this operation was completed. This value is in RFC3339 text format. |
| `operationGroupId` | `string` | [Output Only] An ID that represents a group of operations, such as when a group of operations results from a `bulkInsert` API request. |
| `region` | `string` | [Output Only] The URL of the region where the operation resides. Only applicable when performing regional operations. |
| `targetId` | `string` | [Output Only] The unique target ID, which identifies a specific incarnation of the target resource. |
| `targetLink` | `string` | [Output Only] The URL of the resource that the operation modifies. For operations related to creating a snapshot, this points to the persistent disk that the snapshot was created from. |
| `statusMessage` | `string` | [Output Only] An optional textual description of the current status of the operation. |
| `clientOperationId` | `string` | [Output Only] The value of `requestId` if you provided it in the request. Not present otherwise. |
| `startTime` | `string` | [Output Only] The time that this operation was started by the server. This value is in RFC3339 text format. |
| `creationTimestamp` | `string` | [Deprecated] This field is deprecated. |
| `httpErrorStatusCode` | `integer` | [Output Only] If the operation fails, this field contains the HTTP error status code that was returned. For example, a `404` means the resource was not found. |
| `zone` | `string` | [Output Only] The URL of the zone where the operation resides. Only applicable when performing per-zone operations. |
| `httpErrorMessage` | `string` | [Output Only] If the operation fails, this field contains the HTTP error message that was returned, such as `NOT FOUND`. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `globalOrganizationOperations_get` | `SELECT` | `operation` | Retrieves the specified Operations resource. Gets a list of operations by making a `list()` request. |
| `globalOrganizationOperations_list` | `SELECT` |  | Retrieves a list of Operation resources contained within the specified organization. |
| `globalOrganizationOperations_delete` | `DELETE` | `operation` | Deletes the specified Operations resource. |
