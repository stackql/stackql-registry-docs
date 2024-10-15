---
title: shares_synchronizations
hide_title: false
hide_table_of_contents: false
keywords:
  - shares_synchronizations
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

Creates, updates, deletes, gets or lists a <code>shares_synchronizations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>shares_synchronizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.shares_synchronizations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="consumerEmail" /> | `string` | Email of the user who created the synchronization |
| <CopyableCode code="consumerName" /> | `string` | Name of the user who created the synchronization |
| <CopyableCode code="consumerTenantName" /> | `string` | Tenant name of the consumer who created the synchronization |
| <CopyableCode code="durationMs" /> | `integer` | synchronization duration |
| <CopyableCode code="endTime" /> | `string` | End time of synchronization |
| <CopyableCode code="message" /> | `string` | message of synchronization |
| <CopyableCode code="startTime" /> | `string` | start time of synchronization |
| <CopyableCode code="status" /> | `string` | Raw Status |
| <CopyableCode code="synchronizationId" /> | `string` | Synchronization id |
| <CopyableCode code="synchronizationMode" /> | `string` | Synchronization mode |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, shareName, subscriptionId" /> | List synchronizations of a share |

## `SELECT` examples

List synchronizations of a share


```sql
SELECT
consumerEmail,
consumerName,
consumerTenantName,
durationMs,
endTime,
message,
startTime,
status,
synchronizationId,
synchronizationMode
FROM azure.data_share.shares_synchronizations
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND shareName = '{{ shareName }}'
AND subscriptionId = '{{ subscriptionId }}';
```