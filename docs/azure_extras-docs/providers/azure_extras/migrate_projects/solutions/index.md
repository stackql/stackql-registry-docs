---
title: solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - solutions
  - migrate_projects
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
<tr><td><b>Name</b></td><td><code>solutions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.migrate_projects.solutions</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Solutions_CleanupSolutionData` | `EXEC` | `api-version, migrateProjectName, resourceGroupName, solutionName, subscriptionId` |  |
| `Solutions_DeleteSolution` | `EXEC` | `api-version, migrateProjectName, resourceGroupName, solutionName, subscriptionId` | Delete the solution. Deleting non-existent project is a no-operation. |
| `Solutions_EnumerateSolutions` | `EXEC` | `api-version, migrateProjectName, resourceGroupName, subscriptionId` |  |
| `Solutions_GetConfig` | `EXEC` | `api-version, migrateProjectName, resourceGroupName, solutionName, subscriptionId` |  |
| `Solutions_GetSolution` | `EXEC` | `api-version, migrateProjectName, resourceGroupName, solutionName, subscriptionId` |  |
| `Solutions_PatchSolution` | `EXEC` | `api-version, migrateProjectName, resourceGroupName, solutionName, subscriptionId` | Update a solution with specified name. Supports partial updates, for example only tags can be provided. |
| `Solutions_PutSolution` | `EXEC` | `api-version, migrateProjectName, resourceGroupName, solutionName, subscriptionId` |  |
