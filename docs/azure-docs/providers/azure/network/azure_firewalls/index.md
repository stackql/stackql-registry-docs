---
title: azure_firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_firewalls
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
<tr><td><b>Name</b></td><td><code>azure_firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.azure_firewalls</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of the Azure Firewall. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `zones` | `array` | A list of availability zones denoting where the resource needs to come from. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `azureFirewallName, resourceGroupName, subscriptionId` | Gets the specified Azure Firewall. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Azure Firewalls in a resource group. |
| `create_or_update` | `INSERT` | `azureFirewallName, resourceGroupName, subscriptionId` | Creates or updates the specified Azure Firewall. |
| `delete` | `DELETE` | `azureFirewallName, resourceGroupName, subscriptionId` | Deletes the specified Azure Firewall. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all Azure Firewalls in a resource group. |
| `packet_capture` | `EXEC` | `azureFirewallName, resourceGroupName, subscriptionId` | Runs a packet capture on AzureFirewall. |
