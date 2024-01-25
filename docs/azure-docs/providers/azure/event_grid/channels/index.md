---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
  - event_grid
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
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.channels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties of the Channel. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `channelName, partnerNamespaceName, resourceGroupName, subscriptionId` | Get properties of a channel. |
| `list_by_partner_namespace` | `SELECT` | `partnerNamespaceName, resourceGroupName, subscriptionId` | List all the channels in a partner namespace. |
| `create_or_update` | `INSERT` | `channelName, partnerNamespaceName, resourceGroupName, subscriptionId` | Synchronously creates or updates a new channel with the specified parameters. |
| `delete` | `DELETE` | `channelName, partnerNamespaceName, resourceGroupName, subscriptionId` | Delete an existing channel. |
| `_list_by_partner_namespace` | `EXEC` | `partnerNamespaceName, resourceGroupName, subscriptionId` | List all the channels in a partner namespace. |
| `update` | `EXEC` | `channelName, partnerNamespaceName, resourceGroupName, subscriptionId` | Synchronously updates a channel with the specified parameters. |
