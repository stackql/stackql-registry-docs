---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - dev_center
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
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_center.projects</code></td></tr>
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
| `Projects_Get` | `SELECT` | `projectName, resourceGroupName, subscriptionId` | Gets a specific project. |
| `Projects_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all projects in the resource group. |
| `Projects_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all projects in the subscription. |
| `Projects_CreateOrUpdate` | `INSERT` | `projectName, resourceGroupName, subscriptionId` | Creates or updates a project. |
| `Projects_Delete` | `DELETE` | `projectName, resourceGroupName, subscriptionId` | Deletes a project resource. |
| `Projects_Update` | `EXEC` | `projectName, resourceGroupName, subscriptionId` | Partially updates a project. |
