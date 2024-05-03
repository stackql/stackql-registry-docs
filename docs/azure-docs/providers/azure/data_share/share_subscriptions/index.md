---
title: share_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - share_subscriptions
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
<tr><td><b>Name</b></td><td><code>share_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.share_subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id of the azure resource |
| <CopyableCode code="name" /> | `string` | Name of the azure resource |
| <CopyableCode code="properties" /> | `object` | Share subscription property bag. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of the azure resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId" /> | Get a shareSubscription in an account |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | List share subscriptions in an account |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId, data__properties" /> | Create a shareSubscription in an account |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId" /> | Delete a shareSubscription in an account |
| <CopyableCode code="_list_by_account" /> | `EXEC` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | List share subscriptions in an account |
| <CopyableCode code="cancel_synchronization" /> | `EXEC` | <CopyableCode code="accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId, data__synchronizationId" /> | Request to cancel a synchronization. |
| <CopyableCode code="synchronize" /> | `EXEC` | <CopyableCode code="accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId" /> | Initiate a copy |
