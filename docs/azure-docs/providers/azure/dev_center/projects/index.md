---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - dev_center
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
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dev_center.projects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of a project. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `projectName, resourceGroupName, subscriptionId` | Gets a specific project. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all projects in the resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all projects in the subscription. |
| `create_or_update` | `INSERT` | `projectName, resourceGroupName, subscriptionId` | Creates or updates a project. |
| `delete` | `DELETE` | `projectName, resourceGroupName, subscriptionId` | Deletes a project resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all projects in the resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all projects in the subscription. |
| `update` | `EXEC` | `projectName, resourceGroupName, subscriptionId` | Partially updates a project. |
