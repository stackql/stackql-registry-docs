---
title: contacts
hide_title: false
hide_table_of_contents: false
keywords:
  - contacts
  - orbital
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
<tr><td><b>Name</b></td><td><code>contacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.orbital.contacts</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `contactName, resourceGroupName, spacecraftName, subscriptionId` | Gets the specified contact in a specified resource group. |
| `list` | `SELECT` | `resourceGroupName, spacecraftName, subscriptionId` | Returns list of contacts by spacecraftName. |
| `create` | `INSERT` | `contactName, resourceGroupName, spacecraftName, subscriptionId, data__properties` | Creates a contact. |
| `delete` | `DELETE` | `contactName, resourceGroupName, spacecraftName, subscriptionId` | Deletes a specified contact. |
| `_list` | `EXEC` | `resourceGroupName, spacecraftName, subscriptionId` | Returns list of contacts by spacecraftName. |
