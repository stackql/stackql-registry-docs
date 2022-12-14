---
title: virtual_network_links
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_links
  - private_dns
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
<tr><td><b>Name</b></td><td><code>virtual_network_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.private_dns.virtual_network_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | The ETag of the virtual network link. |
| `location` | `string` | The Azure Region where the resource lives |
| `properties` | `object` | Represents the properties of the Private DNS zone. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualNetworkLinks_Get` | `SELECT` | `privateZoneName, resourceGroupName, subscriptionId, virtualNetworkLinkName` | Gets a virtual network link to the specified Private DNS zone. |
| `VirtualNetworkLinks_List` | `SELECT` | `privateZoneName, resourceGroupName, subscriptionId` | Lists the virtual network links to the specified Private DNS zone. |
| `VirtualNetworkLinks_CreateOrUpdate` | `INSERT` | `privateZoneName, resourceGroupName, subscriptionId, virtualNetworkLinkName` | Creates or updates a virtual network link to the specified Private DNS zone. |
| `VirtualNetworkLinks_Delete` | `DELETE` | `privateZoneName, resourceGroupName, subscriptionId, virtualNetworkLinkName` | Deletes a virtual network link to the specified Private DNS zone. WARNING: In case of a registration virtual network, all auto-registered DNS records in the zone for the virtual network will also be deleted. This operation cannot be undone. |
| `VirtualNetworkLinks_Update` | `EXEC` | `privateZoneName, resourceGroupName, subscriptionId, virtualNetworkLinkName` | Updates a virtual network link to the specified Private DNS zone. |
