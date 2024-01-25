---
title: custom_resource_provider
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_resource_provider
  - custom_providers
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
<tr><td><b>Name</b></td><td><code>custom_resource_provider</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.custom_providers.custom_resource_provider</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `location` | `string` | Resource location |
| `properties` | `object` | The manifest for the custom resource provider |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, resourceProviderName, subscriptionId` | Gets the custom resource provider manifest. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the custom resource providers within a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets all the custom resource providers within a subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, resourceProviderName, subscriptionId` | Creates or updates the custom resource provider. |
| `delete` | `DELETE` | `resourceGroupName, resourceProviderName, subscriptionId` | Deletes the custom resource provider. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all the custom resource providers within a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets all the custom resource providers within a subscription. |
| `update` | `EXEC` | `resourceGroupName, resourceProviderName, subscriptionId` | Updates an existing custom resource provider. The only value that can be updated via PATCH currently is the tags. |
