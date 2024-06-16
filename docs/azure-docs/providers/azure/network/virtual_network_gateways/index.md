---
title: virtual_network_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateways
  - network
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
<tr><td><b>Name</b></td><td><code>virtual_network_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_network_gateways" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation complex type. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | VirtualNetworkGateway properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Gets the specified virtual network gateway by resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all virtual network gateways by resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName, data__properties" /> | Creates or updates a virtual network gateway in the specified resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Deletes the specified virtual network gateway. |
| <CopyableCode code="disconnect_virtual_network_gateway_vpn_connections" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Disconnect vpn connections of virtual network gateway in the specified resource group. |
| <CopyableCode code="reset" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Resets the primary of the virtual network gateway in the specified resource group. |
| <CopyableCode code="reset_vpn_client_shared_key" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Resets the VPN client shared key of the virtual network gateway in the specified resource group. |
| <CopyableCode code="set_vpnclient_ipsec_parameters" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName, data__dhGroup, data__ikeEncryption, data__ikeIntegrity, data__ipsecEncryption, data__ipsecIntegrity, data__pfsGroup, data__saDataSizeKilobytes, data__saLifeTimeSeconds" /> | The Set VpnclientIpsecParameters operation sets the vpnclient ipsec policy for P2S client of virtual network gateway in the specified resource group through Network resource provider. |
