---
title: operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_status
  - storage_sync
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_sync.operation_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Operation Id |
| <CopyableCode code="endTime" /> | `string` | End time of the operation |
| <CopyableCode code="error" /> | `object` | Error type |
| <CopyableCode code="startTime" /> | `string` | Start time of the operation |
| <CopyableCode code="status" /> | `string` | Operation status |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationName, operationId, resourceGroupName, subscriptionId, workflowId" /> | Get Operation status |

## `SELECT` examples

Get Operation status


```sql
SELECT
name,
endTime,
error,
startTime,
status
FROM azure.storage_sync.operation_status
WHERE locationName = '{{ locationName }}'
AND operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workflowId = '{{ workflowId }}';
```