---
title: firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls
  - paloaltonetworks
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.paloaltonetworks.firewalls</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | The properties of the managed service identities assigned to this resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties specific to the Firewall resource deployment. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `firewallName, resourceGroupName, subscriptionId` | Get a FirewallResource |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List FirewallResource resources by resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List FirewallResource resources by subscription ID |
| `create_or_update` | `INSERT` | `firewallName, resourceGroupName, subscriptionId, data__properties` | Create a FirewallResource |
| `delete` | `DELETE` | `firewallName, resourceGroupName, subscriptionId` | Delete a FirewallResource |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List FirewallResource resources by resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List FirewallResource resources by subscription ID |
| `save_log_profile` | `EXEC` | `firewallName, resourceGroupName, subscriptionId` | Log Profile for Firewall |
| `update` | `EXEC` | `firewallName, resourceGroupName, subscriptionId` | Update a FirewallResource |
