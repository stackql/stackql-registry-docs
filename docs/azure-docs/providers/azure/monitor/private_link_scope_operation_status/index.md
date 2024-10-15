---
title: private_link_scope_operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_scope_operation_status
  - monitor
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

Creates, updates, deletes, gets or lists a <code>private_link_scope_operation_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_link_scope_operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.private_link_scope_operation_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The operation Id. |
| <CopyableCode code="name" /> | `string` | The operation name. |
| <CopyableCode code="endTime" /> | `string` | End time of the job in standard ISO8601 format. |
| <CopyableCode code="error" /> | `object` | The error detail. |
| <CopyableCode code="startTime" /> | `string` | Start time of the job in standard ISO8601 format. |
| <CopyableCode code="status" /> | `string` | The status of the operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="asyncOperationId, resourceGroupName, subscriptionId" /> | Get the status of an azure asynchronous operation associated with a private link scope operation. |

## `SELECT` examples

Get the status of an azure asynchronous operation associated with a private link scope operation.


```sql
SELECT
id,
name,
endTime,
error,
startTime,
status
FROM azure.monitor.private_link_scope_operation_status
WHERE asyncOperationId = '{{ asyncOperationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```