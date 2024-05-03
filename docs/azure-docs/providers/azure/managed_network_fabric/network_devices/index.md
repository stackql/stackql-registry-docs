---
title: network_devices
hide_title: false
hide_table_of_contents: false
keywords:
  - network_devices
  - managed_network_fabric
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
<tr><td><b>Name</b></td><td><code>network_devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_devices" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network Device Properties defines the properties of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkDeviceName, resourceGroupName, subscriptionId" /> | Gets the Network Device resource details. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the Network Device resources in a given resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the Network Device resources in a given subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="networkDeviceName, resourceGroupName, subscriptionId, data__properties" /> | Create a Network Device resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkDeviceName, resourceGroupName, subscriptionId" /> | Delete the Network Device resource. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the Network Device resources in a given resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List all the Network Device resources in a given subscription. |
| <CopyableCode code="reboot" /> | `EXEC` | <CopyableCode code="networkDeviceName, resourceGroupName, subscriptionId" /> | Reboot the Network Device. |
| <CopyableCode code="refresh_configuration" /> | `EXEC` | <CopyableCode code="networkDeviceName, resourceGroupName, subscriptionId" /> | Refreshes the configuration the Network Device. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="networkDeviceName, resourceGroupName, subscriptionId" /> | Update certain properties of the Network Device resource. |
| <CopyableCode code="upgrade" /> | `EXEC` | <CopyableCode code="networkDeviceName, resourceGroupName, subscriptionId" /> | Upgrades the version of the Network Device. |
