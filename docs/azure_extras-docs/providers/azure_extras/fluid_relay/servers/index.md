---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - fluid_relay
  - azure_extras    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.fluid_relay.servers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of a Fluid Relay Service resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `FluidRelayServers_Get` | `SELECT` | `fluidRelayServerName, resourceGroup, subscriptionId` |
| `FluidRelayServers_ListByResourceGroup` | `SELECT` | `resourceGroup, subscriptionId` |
| `FluidRelayServers_ListBySubscription` | `SELECT` | `subscriptionId` |
| `FluidRelayServers_CreateOrUpdate` | `INSERT` | `fluidRelayServerName, resourceGroup, subscriptionId` |
| `FluidRelayServers_Delete` | `DELETE` | `fluidRelayServerName, resourceGroup, subscriptionId` |
| `FluidRelayServers_ListKeys` | `EXEC` | `fluidRelayServerName, resourceGroup, subscriptionId` |
| `FluidRelayServers_RegenerateKey` | `EXEC` | `fluidRelayServerName, resourceGroup, subscriptionId, data__keyName` |
| `FluidRelayServers_Update` | `EXEC` | `fluidRelayServerName, resourceGroup, subscriptionId` |
