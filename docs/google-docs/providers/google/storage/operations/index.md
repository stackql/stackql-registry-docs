
---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - storage
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

Creates, updates, deletes or gets an <code>operation</code> resource or lists <code>operations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.storage.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the "name" should be a resource name ending with "operations/{operationId}". |
| <CopyableCode code="done" /> | `boolean` | If the value is "false", it means the operation is still in progress. If "true", the operation is completed, and either "error" or "response" is available. |
| <CopyableCode code="error" /> | `object` | The "Status" type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each "Status" message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="kind" /> | `string` | The kind of item this is. For operations, this is always storage#operation. |
| <CopyableCode code="metadata" /> | `object` | Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any. |
| <CopyableCode code="response" /> | `object` | The normal response of the operation in case of success. If the original method returns no data on success, such as "Delete", the response is google.protobuf.Empty. If the original method is standard Get/Create/Update, the response should be the resource. For other methods, the response should have the type "XxxResponse", where "Xxx" is the original method name. For example, if the original method name is "TakeSnapshot()", the inferred response type is "TakeSnapshotResponse". |
| <CopyableCode code="selfLink" /> | `string` | The link to this long running operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bucket, operationId" /> | Gets the latest state of a long-running operation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="bucket" /> | Lists operations that match the specified filter in the request. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="bucket, operationId" /> | Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. |

## `SELECT` examples

Lists operations that match the specified filter in the request.

```sql
SELECT
name,
done,
error,
kind,
metadata,
response,
selfLink
FROM google.storage.operations
WHERE bucket = '{{ bucket }}'; 
```
