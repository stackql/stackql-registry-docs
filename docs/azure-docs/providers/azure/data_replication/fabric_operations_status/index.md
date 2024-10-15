---
title: fabric_operations_status
hide_title: false
hide_table_of_contents: false
keywords:
  - fabric_operations_status
  - data_replication
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

Creates, updates, deletes, gets or lists a <code>fabric_operations_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fabric_operations_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_replication.fabric_operations_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the Id. |
| <CopyableCode code="name" /> | `string` | Gets or sets the operation name. |
| <CopyableCode code="endTime" /> | `string` | Gets or sets the end time. |
| <CopyableCode code="startTime" /> | `string` | Gets or sets the start time. |
| <CopyableCode code="status" /> | `string` | Gets or sets the status of the operation. ARM expects the terminal status to be one of
Succeeded/ Failed/ Canceled. All other values imply that the operation is still running. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricName, operationId, resourceGroupName, subscriptionId" /> | Tracks the results of an asynchronous operation on the fabric. |

## `SELECT` examples

Tracks the results of an asynchronous operation on the fabric.


```sql
SELECT
id,
name,
endTime,
startTime,
status
FROM azure.data_replication.fabric_operations_status
WHERE fabricName = '{{ fabricName }}'
AND operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```