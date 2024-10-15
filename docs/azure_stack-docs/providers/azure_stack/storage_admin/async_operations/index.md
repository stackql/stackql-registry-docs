---
title: async_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - async_operations
  - storage_admin
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

Creates, updates, deletes, gets or lists a <code>async_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>async_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.storage_admin.async_operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The operation id. |
| <CopyableCode code="context" /> | `object` | Operation request context. |
| <CopyableCode code="httpStatus" /> | `string` | Http status for the async operation. |
| <CopyableCode code="locationHeader" /> | `string` | Location header for async operation. |
| <CopyableCode code="operation" /> | `object` | Async operation content |
| <CopyableCode code="operationEndTime" /> | `string` | Operation end time. |
| <CopyableCode code="operationStartTime" /> | `string` | Operation start time. |
| <CopyableCode code="response" /> | `string` | Response for the async operation. |
| <CopyableCode code="subscriptionId" /> | `string` | Subscription id for async operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="asyncOperationId, location, subscriptionId" /> | Returns the async operation specified by asyncOperationId. |

## `SELECT` examples

Returns the async operation specified by asyncOperationId.


```sql
SELECT
id,
context,
httpStatus,
locationHeader,
operation,
operationEndTime,
operationStartTime,
response,
subscriptionId
FROM azure_stack.storage_admin.async_operations
WHERE asyncOperationId = '{{ asyncOperationId }}'
AND location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```