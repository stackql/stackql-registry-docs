---
title: resource_health_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_health_metadata
  - web_apps
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
<tr><td><b>Name</b></td><td><code>resource_health_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_apps.resource_health_metadata</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `properties` | `object` | ResourceHealthMetadata resource specific properties |
| `type` | `string` | Resource type. |
| `kind` | `string` | Kind of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ResourceHealthMetadata_List` | `SELECT` | `subscriptionId` | Description for List all ResourceHealthMetadata for all sites in the subscription. |
| `ResourceHealthMetadata_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Description for List all ResourceHealthMetadata for all sites in the resource group in the subscription. |
| `ResourceHealthMetadata_ListBySite` | `SELECT` | `name, resourceGroupName, subscriptionId` | Description for Gets the category of ResourceHealthMetadata to use for the given site as a collection |
| `ResourceHealthMetadata_ListBySiteSlot` | `SELECT` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the category of ResourceHealthMetadata to use for the given site as a collection |
| `ResourceHealthMetadata_GetBySite` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the category of ResourceHealthMetadata to use for the given site |
| `ResourceHealthMetadata_GetBySiteSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the category of ResourceHealthMetadata to use for the given site |
