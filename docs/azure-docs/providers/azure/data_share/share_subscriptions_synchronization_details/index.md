---
title: share_subscriptions_synchronization_details
hide_title: false
hide_table_of_contents: false
keywords:
  - share_subscriptions_synchronization_details
  - data_share
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

Creates, updates, deletes, gets or lists a <code>share_subscriptions_synchronization_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>share_subscriptions_synchronization_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.share_subscriptions_synchronization_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the data set |
| <CopyableCode code="dataSetId" /> | `string` | Id of data set |
| <CopyableCode code="dataSetType" /> | `string` | Type of the data set |
| <CopyableCode code="durationMs" /> | `integer` | Duration of data set level copy |
| <CopyableCode code="endTime" /> | `string` | End time of data set level copy |
| <CopyableCode code="filesRead" /> | `integer` | The number of files read from the source data set |
| <CopyableCode code="filesWritten" /> | `integer` | The number of files written into the sink data set |
| <CopyableCode code="message" /> | `string` | Error message if any |
| <CopyableCode code="rowsCopied" /> | `integer` | The number of files copied into the sink data set |
| <CopyableCode code="rowsRead" /> | `integer` | The number of rows read from the source data set. |
| <CopyableCode code="sizeRead" /> | `integer` | The size of the data read from the source data set in bytes |
| <CopyableCode code="sizeWritten" /> | `integer` | The size of the data written into the sink data set in bytes |
| <CopyableCode code="startTime" /> | `string` | Start time of data set level copy |
| <CopyableCode code="status" /> | `string` | Raw Status |
| <CopyableCode code="vCore" /> | `integer` | The vCore units consumed for the data set synchronization |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, shareSubscriptionName, subscriptionId, data__synchronizationId" /> | List synchronization details |

## `SELECT` examples

List synchronization details


```sql
SELECT
name,
dataSetId,
dataSetType,
durationMs,
endTime,
filesRead,
filesWritten,
message,
rowsCopied,
rowsRead,
sizeRead,
sizeWritten,
startTime,
status,
vCore
FROM azure.data_share.share_subscriptions_synchronization_details
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND shareSubscriptionName = '{{ shareSubscriptionName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__synchronizationId = '{{ data__synchronizationId }}';
```