---
title: resource_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_pools
  - connected_vsphere
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
<tr><td><b>Name</b></td><td><code>resource_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.connected_vsphere.resource_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the Id. |
| `name` | `string` | Gets or sets the name. |
| `type` | `string` | Gets or sets the type of the resource. |
| `location` | `string` | Gets or sets the location. |
| `extendedLocation` | `object` | The extended location. |
| `kind` | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| `properties` | `object` | Defines the resource properties. |
| `tags` | `object` | Gets or sets the Resource tags. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ResourcePools_Get` | `SELECT` | `api-version, resourceGroupName, resourcePoolName, subscriptionId` | Implements resourcePool GET method. |
| `ResourcePools_List` | `SELECT` | `api-version, subscriptionId` | List of resourcePools in a subscription. |
| `ResourcePools_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List of resourcePools in a resource group. |
| `ResourcePools_Create` | `INSERT` | `api-version, resourceGroupName, resourcePoolName, subscriptionId, data__location, data__properties` | Create Or Update resourcePool. |
| `ResourcePools_Delete` | `DELETE` | `api-version, resourceGroupName, resourcePoolName, subscriptionId` | Implements resourcePool DELETE method. |
| `ResourcePools_Update` | `EXEC` | `api-version, resourceGroupName, resourcePoolName, subscriptionId` | API to update certain properties of the resourcePool resource. |
