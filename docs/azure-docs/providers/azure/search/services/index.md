---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - search
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.search.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the search service. |
| `sku` | `object` | The resource model definition representing SKU |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, searchServiceName, subscriptionId` | Gets the search service with the given name in the given resource group. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of all Search services in the given resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets a list of all Search services in the given subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, searchServiceName, subscriptionId` | Creates or updates a search service in the given resource group. If the search service already exists, all properties will be updated with the given values. |
| `delete` | `DELETE` | `resourceGroupName, searchServiceName, subscriptionId` | Deletes a search service in the given resource group, along with its associated resources. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets a list of all Search services in the given resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets a list of all Search services in the given subscription. |
| `check_name_availability` | `EXEC` | `subscriptionId, data__name, data__type` | Checks whether or not the given search service name is available for use. Search service names must be globally unique since they are part of the service URI (https://&lt;name&gt;.search.windows.net). |
| `update` | `EXEC` | `resourceGroupName, searchServiceName, subscriptionId` | Updates an existing search service in the given resource group. |
