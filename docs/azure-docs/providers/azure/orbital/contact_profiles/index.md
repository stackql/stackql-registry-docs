---
title: contact_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_profiles
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
<tr><td><b>Name</b></td><td><code>contact_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.orbital.contact_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the contact profile resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `contactProfileName, resourceGroupName, subscriptionId` | Gets the specified contact Profile in a specified resource group. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Returns list of contact profiles by Resource Group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Returns list of contact profiles by Subscription. |
| `create_or_update` | `INSERT` | `contactProfileName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a contact profile. |
| `delete` | `DELETE` | `contactProfileName, resourceGroupName, subscriptionId` | Deletes a specified contact profile resource. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Returns list of contact profiles by Resource Group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Returns list of contact profiles by Subscription. |
