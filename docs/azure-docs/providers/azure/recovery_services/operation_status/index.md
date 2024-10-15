---
title: operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_status
  - recovery_services
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services.operation_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | It should match what is used to GET the operation result |
| <CopyableCode code="name" /> | `string` | It must match the last segment of the "id" field, and will typically be a GUID / system generated value |
| <CopyableCode code="endTime" /> | `string` | End time of the operation |
| <CopyableCode code="error" /> | `object` | The resource management error response. |
| <CopyableCode code="startTime" /> | `string` | Start time of the operation |
| <CopyableCode code="status" /> | `string` | The status of the operation. (InProgress/Success/Failed/Cancelled) |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationId, resourceGroupName, subscriptionId, vaultName" /> | Gets the operation status for a resource. |

## `SELECT` examples

Gets the operation status for a resource.


```sql
SELECT
id,
name,
endTime,
error,
startTime,
status
FROM azure.recovery_services.operation_status
WHERE operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```