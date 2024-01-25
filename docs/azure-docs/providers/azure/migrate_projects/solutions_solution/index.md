---
title: solutions_solution
hide_title: false
hide_table_of_contents: false
keywords:
  - solutions_solution
  - migrate_projects
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
<tr><td><b>Name</b></td><td><code>solutions_solution</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.migrate_projects.solutions_solution</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets the relative URL to get to this REST resource. |
| `name` | `string` | Gets the name of this REST resource. |
| `etag` | `string` | Gets or sets the ETAG for optimistic concurrency control. |
| `properties` | `object` | Class for solution properties. |
| `type` | `string` | Gets the type of this REST resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, migrateProjectName, resourceGroupName, solutionName, subscriptionId` |  |
| `delete` | `DELETE` | `api-version, migrateProjectName, resourceGroupName, solutionName, subscriptionId` | Delete the solution. Deleting non-existent project is a no-operation. |
