---
title: zones
hide_title: false
hide_table_of_contents: false
keywords:
  - zones
  - dns
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
<tr><td><b>Name</b></td><td><code>zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dns.zones</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `type` | `string` | Resource type. |
| `etag` | `string` | The etag of the zone. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Represents the properties of the zone. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Zones_Get` | `SELECT` | `resourceGroupName, subscriptionId, zoneName` | Gets a DNS zone. Retrieves the zone properties, but not the record sets within the zone. |
| `Zones_List` | `SELECT` | `subscriptionId` | Lists the DNS zones in all resource groups in a subscription. |
| `Zones_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the DNS zones within a resource group. |
| `Zones_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, zoneName` | Creates or updates a DNS zone. Does not modify DNS records within the zone. |
| `Zones_Delete` | `DELETE` | `resourceGroupName, subscriptionId, zoneName` | Deletes a DNS zone. WARNING: All DNS records in the zone will also be deleted. This operation cannot be undone. |
| `Zones_Update` | `EXEC` | `resourceGroupName, subscriptionId, zoneName` | Updates a DNS zone. Does not modify DNS records within the zone. |
