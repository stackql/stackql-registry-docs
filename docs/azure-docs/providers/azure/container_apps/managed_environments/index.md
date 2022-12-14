---
title: managed_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_environments
  - container_apps
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
<tr><td><b>Name</b></td><td><code>managed_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_apps.managed_environments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Managed environment resource specific properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedEnvironments_Get` | `SELECT` | `environmentName, resourceGroupName, subscriptionId` | Get the properties of a Managed Environment used to host container apps. |
| `ManagedEnvironments_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Get all the Managed Environments in a resource group. |
| `ManagedEnvironments_ListBySubscription` | `SELECT` | `subscriptionId` | Get all Managed Environments for a subscription. |
| `ManagedEnvironments_CreateOrUpdate` | `INSERT` | `environmentName, resourceGroupName, subscriptionId` | Creates or updates a Managed Environment used to host container apps. |
| `ManagedEnvironments_Delete` | `DELETE` | `environmentName, resourceGroupName, subscriptionId` | Delete a Managed Environment if it does not have any container apps. |
| `ManagedEnvironments_Update` | `EXEC` | `environmentName, resourceGroupName, subscriptionId` | Patches a Managed Environment using JSON Merge Patch |
