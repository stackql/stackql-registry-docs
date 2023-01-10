---
title: activations
hide_title: false
hide_table_of_contents: false
keywords:
  - activations
  - azure_bridge_admin
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
<tr><td><b>Name</b></td><td><code>activations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.azure_bridge_admin.activations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `properties` | `object` | Holds properties related to activation. |
| `tags` | `object` | List of key value pairs. |
| `type` | `string` | Type of resource. |
| `location` | `string` | Location of the resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Activations_Get` | `SELECT` | `activationName, resourceGroupName, subscriptionId` | Returns activation name. |
| `Activations_List` | `SELECT` | `resourceGroupName, subscriptionId` | Returns the list of activations. |
| `Activations_CreateOrUpdate` | `INSERT` | `activationName, resourceGroupName, subscriptionId` | Create a new activation. |
| `Activations_Delete` | `DELETE` | `activationName, resourceGroupName, subscriptionId` | Delete an activation. |
