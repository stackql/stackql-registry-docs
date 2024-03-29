---
title: vpn_site_links
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_site_links
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
<tr><td><b>Name</b></td><td><code>vpn_site_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.vpn_site_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Parameters for VpnSite. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, vpnSiteLinkName, vpnSiteName` | Retrieves the details of a VPN site link. |
| `list_by_vpn_site` | `SELECT` | `resourceGroupName, subscriptionId, vpnSiteName` | Lists all the vpnSiteLinks in a resource group for a vpn site. |
| `_list_by_vpn_site` | `EXEC` | `resourceGroupName, subscriptionId, vpnSiteName` | Lists all the vpnSiteLinks in a resource group for a vpn site. |
