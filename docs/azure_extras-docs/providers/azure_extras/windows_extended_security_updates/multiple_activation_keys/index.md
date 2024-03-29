---
title: multiple_activation_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - multiple_activation_keys
  - windows_extended_security_updates
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>multiple_activation_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.windows_extended_security_updates.multiple_activation_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | MAK key specific properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `multipleActivationKeyName, resourceGroupName, subscriptionId` | Get a MAK key. |
| `list` | `SELECT` | `subscriptionId` | List all Multiple Activation Keys (MAK) created for a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all Multiple Activation Keys (MAK) in a resource group. |
| `create` | `INSERT` | `multipleActivationKeyName, resourceGroupName, subscriptionId` | Create a MAK key. |
| `delete` | `DELETE` | `multipleActivationKeyName, resourceGroupName, subscriptionId` | Delete a MAK key. |
| `_list` | `EXEC` | `subscriptionId` | List all Multiple Activation Keys (MAK) created for a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all Multiple Activation Keys (MAK) in a resource group. |
| `update` | `EXEC` | `multipleActivationKeyName, resourceGroupName, subscriptionId` | Update a MAK key. |
