---
title: operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_status
  - dev_center
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

Creates, updates, deletes, gets or lists a <code>operation_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.operation_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified ID for the async operation. |
| <CopyableCode code="name" /> | `string` | Name of the async operation. |
| <CopyableCode code="endTime" /> | `string` | The end time of the operation. |
| <CopyableCode code="error" /> | `object` | The error detail. |
| <CopyableCode code="operations" /> | `array` | The operations list. |
| <CopyableCode code="percentComplete" /> | `number` | Percent of the operation that is complete. |
| <CopyableCode code="properties" /> | `object` | Custom operation properties, populated only for a successful operation. |
| <CopyableCode code="resourceId" /> | `string` | Fully qualified ID of the resource against which the original async operation was started. |
| <CopyableCode code="startTime" /> | `string` | The start time of the operation. |
| <CopyableCode code="status" /> | `string` | Operation status. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, operationId, subscriptionId" /> | Gets the current status of an async operation. |

## `SELECT` examples

Gets the current status of an async operation.


```sql
SELECT
id,
name,
endTime,
error,
operations,
percentComplete,
properties,
resourceId,
startTime,
status
FROM azure.dev_center.operation_status
WHERE location = '{{ location }}'
AND operationId = '{{ operationId }}'
AND subscriptionId = '{{ subscriptionId }}';
```