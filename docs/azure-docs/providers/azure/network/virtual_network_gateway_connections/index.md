---
title: virtual_network_gateway_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateway_connections
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
<tr><td><b>Name</b></td><td><code>virtual_network_gateway_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_network_gateway_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | VirtualNetworkGatewayConnection properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName" /> | Gets the specified virtual network gateway connection by resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The List VirtualNetworkGatewayConnections operation retrieves all the virtual network gateways connections created. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName, data__properties" /> | Creates or updates a virtual network gateway connection in the specified resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName" /> | Deletes the specified virtual network Gateway connection. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The List VirtualNetworkGatewayConnections operation retrieves all the virtual network gateways connections created. |
| <CopyableCode code="reset_connection" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName" /> | Resets the virtual network gateway connection specified. |
| <CopyableCode code="reset_shared_key" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName, data__keyLength" /> | The VirtualNetworkGatewayConnectionResetSharedKey operation resets the virtual network gateway connection shared key for passed virtual network gateway connection in the specified resource group through Network resource provider. |
| <CopyableCode code="set_shared_key" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName, data__value" /> | The Put VirtualNetworkGatewayConnectionSharedKey operation sets the virtual network gateway connection shared key for passed virtual network gateway connection in the specified resource group through Network resource provider. |
