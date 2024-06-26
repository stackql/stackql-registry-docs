---
title: share_subscriptions_synchronizations
hide_title: false
hide_table_of_contents: false
keywords:
  - share_subscriptions_synchronizations
  - data_share
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




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
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId" /> |
