---
title: provider_share_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_share_subscriptions
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
<tr><td><b>Name</b></td><td><code>provider_share_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.provider_share_subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id of the azure resource |
| <CopyableCode code="name" /> | `string` | Name of the azure resource |
| <CopyableCode code="properties" /> | `object` | Provider share subscription properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of the azure resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_share" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, shareName, subscriptionId" /> | List share subscriptions in a provider share |
| <CopyableCode code="adjust" /> | `EXEC` | <CopyableCode code="accountName, api-version, providerShareSubscriptionId, resourceGroupName, shareName, subscriptionId" /> | Adjust a share subscription's expiration date in a provider share |
| <CopyableCode code="get_by_share" /> | `EXEC` | <CopyableCode code="accountName, api-version, providerShareSubscriptionId, resourceGroupName, shareName, subscriptionId" /> | Get share subscription in a provider share |
| <CopyableCode code="reinstate" /> | `EXEC` | <CopyableCode code="accountName, api-version, providerShareSubscriptionId, resourceGroupName, shareName, subscriptionId" /> | Reinstate share subscription in a provider share |
| <CopyableCode code="revoke" /> | `EXEC` | <CopyableCode code="accountName, api-version, providerShareSubscriptionId, resourceGroupName, shareName, subscriptionId" /> | Revoke share subscription in a provider share |
