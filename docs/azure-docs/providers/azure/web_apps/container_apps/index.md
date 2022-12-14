---
title: container_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - container_apps
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
<tr><td><b>Name</b></td><td><code>container_apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_apps.container_apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `type` | `string` | Resource type. |
| `kind` | `string` | Kind of resource. |
| `location` | `string` | Resource Location. |
| `properties` | `object` | ContainerApp resource specific properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ContainerApps_Get` | `SELECT` | `name, resourceGroupName, subscriptionId` |  |
| `ContainerApps_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |  |
| `ContainerApps_ListBySubscription` | `SELECT` | `subscriptionId` |  |
| `ContainerApps_CreateOrUpdate` | `INSERT` | `name, resourceGroupName, subscriptionId` | Description for Create or update a Container App. |
| `ContainerApps_Delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Description for Delete a Container App. |
| `ContainerApps_ListSecrets` | `EXEC` | `name, subscriptionId` |  |
