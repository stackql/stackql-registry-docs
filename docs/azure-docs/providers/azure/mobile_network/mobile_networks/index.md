---
title: mobile_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - mobile_networks
  - mobile_network
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
<tr><td><b>Name</b></td><td><code>mobile_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.mobile_networks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Mobile network properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="mobileNetworkName, resourceGroupName, subscriptionId" /> | Gets information about the specified mobile network. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the mobile networks in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the mobile networks in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="mobileNetworkName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a mobile network. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="mobileNetworkName, resourceGroupName, subscriptionId" /> | Deletes the specified mobile network. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the mobile networks in a resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all the mobile networks in a subscription. |
