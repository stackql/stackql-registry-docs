---
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
  - customer_insights
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
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_insights.profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | The profile type definition. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `hubName, profileName, resourceGroupName, subscriptionId` | Gets information about the specified profile. |
| `list_by_hub` | `SELECT` | `hubName, resourceGroupName, subscriptionId` | Gets all profile in the hub. |
| `create_or_update` | `INSERT` | `hubName, profileName, resourceGroupName, subscriptionId` | Creates a profile within a Hub, or updates an existing profile. |
| `delete` | `DELETE` | `hubName, profileName, resourceGroupName, subscriptionId` | Deletes a profile within a hub |
| `_list_by_hub` | `EXEC` | `hubName, resourceGroupName, subscriptionId` | Gets all profile in the hub. |
