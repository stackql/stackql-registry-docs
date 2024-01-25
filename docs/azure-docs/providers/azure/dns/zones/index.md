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
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `etag` | `string` | The etag of the zone. |
| `properties` | `object` | Represents the properties of the zone. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, zoneName` | Gets a DNS zone. Retrieves the zone properties, but not the record sets within the zone. |
| `list` | `SELECT` | `subscriptionId` | Lists the DNS zones in all resource groups in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the DNS zones within a resource group. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, zoneName` | Creates or updates a DNS zone. Does not modify DNS records within the zone. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, zoneName` | Deletes a DNS zone. WARNING: All DNS records in the zone will also be deleted. This operation cannot be undone. |
| `_list` | `EXEC` | `subscriptionId` | Lists the DNS zones in all resource groups in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists the DNS zones within a resource group. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, zoneName` | Updates a DNS zone. Does not modify DNS records within the zone. |
