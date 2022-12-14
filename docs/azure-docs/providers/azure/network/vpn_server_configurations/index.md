---
title: vpn_server_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_server_configurations
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_server_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.vpn_server_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | Parameters for VpnServerConfiguration. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VpnServerConfigurations_Get` | `SELECT` | `resourceGroupName, subscriptionId, vpnServerConfigurationName` | Retrieves the details of a VpnServerConfiguration. |
| `VpnServerConfigurations_List` | `SELECT` | `subscriptionId` | Lists all the VpnServerConfigurations in a subscription. |
| `VpnServerConfigurations_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the vpnServerConfigurations in a resource group. |
| `VpnServerConfigurations_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, vpnServerConfigurationName` | Creates a VpnServerConfiguration resource if it doesn't exist else updates the existing VpnServerConfiguration. |
| `VpnServerConfigurations_Delete` | `DELETE` | `resourceGroupName, subscriptionId, vpnServerConfigurationName` | Deletes a VpnServerConfiguration. |
| `VpnServerConfigurations_UpdateTags` | `EXEC` | `resourceGroupName, subscriptionId, vpnServerConfigurationName` | Updates VpnServerConfiguration tags. |
