---
title: transfer_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - transfer_operations
  - storagetransfer
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

Creates, updates, deletes, gets or lists a <code>transfer_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transfer_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.storagetransfer.transfer_operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The server-assigned unique name. The format of `name` is `transferOperations/some/unique/name`. |
| <CopyableCode code="done" /> | `boolean` | If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="metadata" /> | `object` | Represents the transfer operation object. To request a TransferOperation object, use transferOperations.get. |
| <CopyableCode code="response" /> | `object` | The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="transferOperationsId" /> | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="filter" /> | Lists transfer operations. Operations are ordered by their creation time in reverse chronological order. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="transferOperationsId" /> | Cancels a transfer. Use the transferOperations.get method to check if the cancellation succeeded or if the operation completed despite the `cancel` request. When you cancel an operation, the currently running transfer is interrupted. For recurring transfer jobs, the next instance of the transfer job will still run. For example, if your job is configured to run every day at 1pm and you cancel Monday's operation at 1:05pm, Monday's transfer will stop. However, a transfer job will still be attempted on Tuesday. This applies only to currently running operations. If an operation is not currently running, `cancel` does nothing. *Caution:* Canceling a transfer job can leave your data in an unknown state. We recommend that you restore the state at both the destination and the source after the `cancel` request completes so that your data is in a consistent state. When you cancel a job, the next job computes a delta of files and may repair any inconsistent state. For instance, if you run a job every day, and today's job found 10 new files and transferred five files before you canceled the job, tomorrow's transfer operation will compute a new delta with the five files that were not copied today plus any new files discovered tomorrow. |
| <CopyableCode code="pause" /> | `EXEC` | <CopyableCode code="transferOperationsId" /> | Pauses a transfer operation. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="transferOperationsId" /> | Resumes a transfer operation that is paused. |

## `SELECT` examples

Lists transfer operations. Operations are ordered by their creation time in reverse chronological order.

```sql
SELECT
name,
done,
error,
metadata,
response
FROM google.storagetransfer.transfer_operations
WHERE filter = '{{ filter }}';
```
