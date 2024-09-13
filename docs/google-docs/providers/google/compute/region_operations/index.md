---
title: region_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - region_operations
  - compute
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

Creates, updates, deletes or gets an <code>region_operation</code> resource or lists <code>region_operations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the operation. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | [Output Only] Name of the operation. |
| <CopyableCode code="description" /> | `string` | [Output Only] A textual description of the operation, which is set when the operation is created. |
| <CopyableCode code="clientOperationId" /> | `string` | [Output Only] The value of `requestId` if you provided it in the request. Not present otherwise. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Deprecated] This field is deprecated. |
| <CopyableCode code="endTime" /> | `string` | [Output Only] The time that this operation was completed. This value is in RFC3339 text format. |
| <CopyableCode code="error" /> | `object` | [Output Only] If errors are generated during processing of the operation, this field will be populated. |
| <CopyableCode code="httpErrorMessage" /> | `string` | [Output Only] If the operation fails, this field contains the HTTP error message that was returned, such as `NOT FOUND`. |
| <CopyableCode code="httpErrorStatusCode" /> | `integer` | [Output Only] If the operation fails, this field contains the HTTP error status code that was returned. For example, a `404` means the resource was not found. |
| <CopyableCode code="insertTime" /> | `string` | [Output Only] The time that this operation was requested. This value is in RFC3339 text format. |
| <CopyableCode code="instancesBulkInsertOperationMetadata" /> | `object` |  |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always `compute#operation` for Operation resources. |
| <CopyableCode code="operationGroupId" /> | `string` | [Output Only] An ID that represents a group of operations, such as when a group of operations results from a `bulkInsert` API request. |
| <CopyableCode code="operationType" /> | `string` | [Output Only] The type of operation, such as `insert`, `update`, or `delete`, and so on. |
| <CopyableCode code="progress" /> | `integer` | [Output Only] An optional progress indicator that ranges from 0 to 100. There is no requirement that this be linear or support any granularity of operations. This should not be used to guess when the operation will be complete. This number should monotonically increase as the operation progresses. |
| <CopyableCode code="region" /> | `string` | [Output Only] The URL of the region where the operation resides. Only applicable when performing regional operations. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="setCommonInstanceMetadataOperationMetadata" /> | `object` |  |
| <CopyableCode code="startTime" /> | `string` | [Output Only] The time that this operation was started by the server. This value is in RFC3339 text format. |
| <CopyableCode code="status" /> | `string` | [Output Only] The status of the operation, which can be one of the following: `PENDING`, `RUNNING`, or `DONE`. |
| <CopyableCode code="statusMessage" /> | `string` | [Output Only] An optional textual description of the current status of the operation. |
| <CopyableCode code="targetId" /> | `string` | [Output Only] The unique target ID, which identifies a specific incarnation of the target resource. |
| <CopyableCode code="targetLink" /> | `string` | [Output Only] The URL of the resource that the operation modifies. For operations related to creating a snapshot, this points to the persistent disk that the snapshot was created from. |
| <CopyableCode code="user" /> | `string` | [Output Only] User who requested the operation, for example: `user@example.com` or `alice_smith_identifier (global/workforcePools/example-com-us-employees)`. |
| <CopyableCode code="warnings" /> | `array` | [Output Only] If warning messages are generated during processing of the operation, this field will be populated. |
| <CopyableCode code="zone" /> | `string` | [Output Only] The URL of the zone where the operation resides. Only applicable when performing per-zone operations. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operation, project, region" /> | Retrieves the specified region-specific Operations resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Retrieves a list of Operation resources contained within the specified region. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="operation, project, region" /> | Deletes the specified region-specific Operations resource. |
| <CopyableCode code="wait" /> | `EXEC` | <CopyableCode code="operation, project, region" /> | Waits for the specified Operation resource to return as `DONE` or for the request to approach the 2 minute deadline, and retrieves the specified Operation resource. This method differs from the `GET` method in that it waits for no more than the default deadline (2 minutes) and then returns the current state of the operation, which might be `DONE` or still in progress. This method is called on a best-effort basis. Specifically: - In uncommon cases, when the server is overloaded, the request might return before the default deadline is reached, or might return after zero seconds. - If the default deadline is reached, there is no guarantee that the operation is actually done when the method returns. Be prepared to retry if the operation is not `DONE`.  |

## `SELECT` examples

Retrieves a list of Operation resources contained within the specified region.

```sql
SELECT
id,
name,
description,
clientOperationId,
creationTimestamp,
endTime,
error,
httpErrorMessage,
httpErrorStatusCode,
insertTime,
instancesBulkInsertOperationMetadata,
kind,
operationGroupId,
operationType,
progress,
region,
selfLink,
setCommonInstanceMetadataOperationMetadata,
startTime,
status,
statusMessage,
targetId,
targetLink,
user,
warnings,
zone
FROM google.compute.region_operations
WHERE project = '{{ project }}'
AND region = '{{ region }}'; 
```

## `DELETE` example

Deletes the specified region_operation resource.

```sql
DELETE FROM google.compute.region_operations
WHERE operation = '{{ operation }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```
