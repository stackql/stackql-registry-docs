---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - lifesciences
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.lifesciences.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The server-assigned name for the operation. This may be passed to the other operation methods to retrieve information about the operation's status. |
| <CopyableCode code="done" /> | `boolean` | If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="metadata" /> | `object` | An Metadata object. This will always be returned with the Operation. |
| <CopyableCode code="response" /> | `object` | An Empty object. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, operationsId, projectsId" /> | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission: * `lifesciences.operations.get` |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists operations that match the specified filter in the request. Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission: * `lifesciences.operations.list` |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="locationsId, operationsId, projectsId" /> | Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. Clients may use Operations.GetOperation or Operations.ListOperations to check whether the cancellation succeeded or the operation completed despite cancellation. Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission: * `lifesciences.operations.cancel` |

## `SELECT` examples

Lists operations that match the specified filter in the request. Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission: * `lifesciences.operations.list`

```sql
SELECT
name,
done,
error,
metadata,
response
FROM google.lifesciences.operations
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
