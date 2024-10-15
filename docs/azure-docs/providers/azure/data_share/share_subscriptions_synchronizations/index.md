---
title: share_subscriptions_synchronizations
hide_title: false
hide_table_of_contents: false
keywords:
  - share_subscriptions_synchronizations
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

Creates, updates, deletes, gets or lists a <code>share_subscriptions_synchronizations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>share_subscriptions_synchronizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.share_subscriptions_synchronizations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="durationMs" /> | `integer` | Synchronization duration |
| <CopyableCode code="endTime" /> | `string` | End time of synchronization |
| <CopyableCode code="message" /> | `string` | message of Synchronization |
| <CopyableCode code="startTime" /> | `string` | start time of synchronization |
| <CopyableCode code="status" /> | `string` | Raw Status |
| <CopyableCode code="synchronizationId" /> | `string` | Synchronization id |
| <CopyableCode code="synchronizationMode" /> | `string` | Synchronization Mode |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, shareSubscriptionName, subscriptionId" /> | List synchronizations of a share subscription |

## `SELECT` examples

List synchronizations of a share subscription


```sql
SELECT
durationMs,
endTime,
message,
startTime,
status,
synchronizationId,
synchronizationMode
FROM azure.data_share.share_subscriptions_synchronizations
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND shareSubscriptionName = '{{ shareSubscriptionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```