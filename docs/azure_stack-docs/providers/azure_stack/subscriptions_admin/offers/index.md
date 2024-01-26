---
title: offers
hide_title: false
hide_table_of_contents: false
keywords:
  - offers
  - subscriptions_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>offers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.subscriptions_admin.offers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Location of the resource |
| `properties` | `object` | Represents an offering of services against which a subscription can be created. |
| `tags` | `object` | List of key-value pairs. |
| `type` | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `offer, resourceGroupName, subscriptionId` | Get the specified offer. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Get the list of offers under a resource group. |
| `create_or_update` | `INSERT` | `offer, resourceGroupName, subscriptionId` | Create or update the offer. |
| `delete` | `DELETE` | `offer, resourceGroupName, subscriptionId` | Delete the specified offer. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Get the list of offers under a resource group. |
| `link` | `EXEC` | `offer, resourceGroupName, subscriptionId` | Links a plan to an offer. |
| `unlink` | `EXEC` | `offer, resourceGroupName, subscriptionId` | Unlink a plan from an offer. |
