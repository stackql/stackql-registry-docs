---
title: assessment_projects_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - assessment_projects_operations
  - migrate
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
<tr><td><b>Name</b></td><td><code>assessment_projects_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.migrate.assessment_projects_operations</code></td></tr>
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
| `get` | `SELECT` | `projectName, resourceGroupName, subscriptionId` | Get a AssessmentProject |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List AssessmentProject resources by resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List AssessmentProject resources by subscription ID |
| `create` | `INSERT` | `projectName, resourceGroupName, subscriptionId` | Create a AssessmentProject |
| `delete` | `DELETE` | `projectName, resourceGroupName, subscriptionId` | Delete a AssessmentProject |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List AssessmentProject resources by resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List AssessmentProject resources by subscription ID |
| `update` | `EXEC` | `projectName, resourceGroupName, subscriptionId` | Update a AssessmentProject |
