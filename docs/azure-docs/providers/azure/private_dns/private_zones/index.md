---
title: private_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - private_zones
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
<tr><td><b>Name</b></td><td><code>private_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.private_dns.private_zones</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `etag` | `string` | The ETag of the zone. |
| `location` | `string` | The Azure Region where the resource lives |
| `properties` | `object` | Represents the properties of the Private DNS zone. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateZones_Get` | `SELECT` | `privateZoneName, resourceGroupName, subscriptionId` | Gets a Private DNS zone. Retrieves the zone properties, but not the virtual networks links or the record sets within the zone. |
| `PrivateZones_List` | `SELECT` | `subscriptionId` | Lists the Private DNS zones in all resource groups in a subscription. |
| `PrivateZones_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the Private DNS zones within a resource group. |
| `PrivateZones_CreateOrUpdate` | `INSERT` | `privateZoneName, resourceGroupName, subscriptionId` | Creates or updates a Private DNS zone. Does not modify Links to virtual networks or DNS records within the zone. |
| `PrivateZones_Delete` | `DELETE` | `privateZoneName, resourceGroupName, subscriptionId` | Deletes a Private DNS zone. WARNING: All DNS records in the zone will also be deleted. This operation cannot be undone. Private DNS zone cannot be deleted unless all virtual network links to it are removed. |
| `PrivateZones_Update` | `EXEC` | `privateZoneName, resourceGroupName, subscriptionId` | Updates a Private DNS zone. Does not modify virtual network links or DNS records within the zone. |
