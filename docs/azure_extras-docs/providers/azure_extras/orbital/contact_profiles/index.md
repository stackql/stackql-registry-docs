---
title: contact_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_profiles
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
<tr><td><b>Name</b></td><td><code>contact_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.orbital.contact_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of the contact profile resource. |
| `tags` | `object` | Resource tags. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ContactProfiles_Get` | `SELECT` | `contactProfileName, resourceGroupName, subscriptionId` | Gets the specified contact Profile in a specified resource group. |
| `ContactProfiles_List` | `SELECT` | `resourceGroupName, subscriptionId` | Returns list of contact profiles by Resource Group. |
| `ContactProfiles_ListBySubscription` | `SELECT` | `subscriptionId` | Returns list of contact profiles by Subscription. |
| `ContactProfiles_CreateOrUpdate` | `INSERT` | `contactProfileName, resourceGroupName, subscriptionId` | Creates or updates a contact profile. |
| `ContactProfiles_Delete` | `DELETE` | `contactProfileName, resourceGroupName, subscriptionId` | Deletes a specified contact profile resource. |
| `ContactProfiles_UpdateTags` | `EXEC` | `contactProfileName, resourceGroupName, subscriptionId` | Updates the specified contact profile tags. |
