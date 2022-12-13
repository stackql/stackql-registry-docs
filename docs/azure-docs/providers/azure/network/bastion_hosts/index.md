---
title: bastion_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - bastion_hosts
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
<tr><td><b>Name</b></td><td><code>bastion_hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.bastion_hosts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | Properties of the Bastion Host. |
| `sku` | `object` | The sku of this Bastion Host. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BastionHosts_Get` | `SELECT` | `bastionHostName, resourceGroupName, subscriptionId` | Gets the specified Bastion Host. |
| `BastionHosts_List` | `SELECT` | `subscriptionId` | Lists all Bastion Hosts in a subscription. |
| `BastionHosts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Bastion Hosts in a resource group. |
| `BastionHosts_CreateOrUpdate` | `INSERT` | `bastionHostName, resourceGroupName, subscriptionId` | Creates or updates the specified Bastion Host. |
| `BastionHosts_Delete` | `DELETE` | `bastionHostName, resourceGroupName, subscriptionId` | Deletes the specified Bastion Host. |
| `BastionHosts_UpdateTags` | `EXEC` | `bastionHostName, resourceGroupName, subscriptionId` | Updates Tags for BastionHost resource |
| `DeleteBastionShareableLink` | `EXEC` | `bastionHostName, resourceGroupName, subscriptionId` | Deletes the Bastion Shareable Links for all the VMs specified in the request. |
| `DisconnectActiveSessions` | `EXEC` | `bastionHostName, resourceGroupName, subscriptionId` | Returns the list of currently active sessions on the Bastion. |
| `GetActiveSessions` | `EXEC` | `bastionHostName, resourceGroupName, subscriptionId` | Returns the list of currently active sessions on the Bastion. |
| `GetBastionShareableLink` | `EXEC` | `bastionHostName, resourceGroupName, subscriptionId` | Return the Bastion Shareable Links for all the VMs specified in the request. |
| `PutBastionShareableLink` | `EXEC` | `bastionHostName, resourceGroupName, subscriptionId` | Creates a Bastion Shareable Links for all the VMs specified in the request. |
