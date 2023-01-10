---
title: contacts
hide_title: false
hide_table_of_contents: false
keywords:
  - contacts
  - orbital
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
<tr><td><b>Name</b></td><td><code>contacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.orbital.contacts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Properties of the Contact Resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Contacts_Get` | `SELECT` | `contactName, resourceGroupName, spacecraftName, subscriptionId` | Gets the specified contact in a specified resource group. |
| `Contacts_List` | `SELECT` | `resourceGroupName, spacecraftName, subscriptionId` | Returns list of contacts by spacecraftName. |
| `Contacts_Create` | `INSERT` | `contactName, resourceGroupName, spacecraftName, subscriptionId` | Creates a contact. |
| `Contacts_Delete` | `DELETE` | `contactName, resourceGroupName, spacecraftName, subscriptionId` | Deletes a specified contact. |
