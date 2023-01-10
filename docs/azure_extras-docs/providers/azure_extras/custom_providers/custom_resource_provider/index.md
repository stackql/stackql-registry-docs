---
title: custom_resource_provider
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_resource_provider
  - custom_providers
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
<tr><td><b>Name</b></td><td><code>custom_resource_provider</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.custom_providers.custom_resource_provider</code></td></tr>
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
| `CustomResourceProvider_Get` | `SELECT` | `resourceGroupName, resourceProviderName, subscriptionId` | Gets the custom resource provider manifest. |
| `CustomResourceProvider_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the custom resource providers within a resource group. |
| `CustomResourceProvider_ListBySubscription` | `SELECT` | `subscriptionId` | Gets all the custom resource providers within a subscription. |
| `CustomResourceProvider_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceProviderName, subscriptionId` | Creates or updates the custom resource provider. |
| `CustomResourceProvider_Delete` | `DELETE` | `resourceGroupName, resourceProviderName, subscriptionId` | Deletes the custom resource provider. |
| `CustomResourceProvider_Update` | `EXEC` | `resourceGroupName, resourceProviderName, subscriptionId` | Updates an existing custom resource provider. The only value that can be updated via PATCH currently is the tags. |
