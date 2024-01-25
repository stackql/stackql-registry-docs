---
title: vpn_sites
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_sites
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
<tr><td><b>Name</b></td><td><code>vpn_sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.vpn_sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Parameters for VpnSite. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, vpnSiteName` | Retrieves the details of a VPN site. |
| `list` | `SELECT` | `subscriptionId` | Lists all the VpnSites in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the vpnSites in a resource group. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, vpnSiteName, data__location` | Creates a VpnSite resource if it doesn't exist else updates the existing VpnSite. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, vpnSiteName` | Deletes a VpnSite. |
| `_list` | `EXEC` | `subscriptionId` | Lists all the VpnSites in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the vpnSites in a resource group. |
