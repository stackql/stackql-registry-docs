---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - search
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.search.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `sku` | `object` | The resource model definition representing SKU |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the search service. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Services_Get` | `SELECT` | `resourceGroupName, searchServiceName, subscriptionId` | Gets the search service with the given name in the given resource group. |
| `Services_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of all search services in the given resource group. |
| `Services_ListBySubscription` | `SELECT` | `subscriptionId` | Gets a list of all search services in the given subscription. |
| `Services_CreateOrUpdate` | `INSERT` | `resourceGroupName, searchServiceName, subscriptionId` | Creates or updates a search service in the given resource group. If the search service already exists, all properties will be updated with the given values. |
| `Services_Delete` | `DELETE` | `resourceGroupName, searchServiceName, subscriptionId` | Deletes a search service in the given resource group, along with its associated resources. |
| `Services_CheckNameAvailability` | `EXEC` | `subscriptionId, data__name, data__type` | Checks whether or not the given search service name is available for use. Search service names must be globally unique since they are part of the service URI (https://&lt;name&gt;.search.windows.net). |
| `Services_Update` | `EXEC` | `resourceGroupName, searchServiceName, subscriptionId` | Updates an existing search service in the given resource group. |
