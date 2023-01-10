---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - migrate
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
<tr><td><b>Id</b></td><td><code>azure_extras.migrate.projects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Path reference to this project /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Migrate/assessmentProjects/&#123;projectName&#125; |
| `name` | `string` | Name of the project. |
| `eTag` | `string` | For optimistic concurrency control. |
| `location` | `string` | Azure location in which project is created. |
| `properties` | `object` | Properties of a project. |
| `tags` | `object` | Tags provided by Azure Tagging service. |
| `type` | `string` | Type of the object = [Microsoft.Migrate/assessmentProjects]. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Projects_Get` | `SELECT` | `api-version, projectName, resourceGroupName, subscriptionId` | Get the project with the specified name. |
| `Projects_List` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Get all the projects in the resource group. |
| `Projects_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | Get all the projects in the subscription. |
| `Projects_Create` | `INSERT` | `api-version, projectName, resourceGroupName, subscriptionId` | Create a project with specified name. If a project already exists, update it. |
| `Projects_Delete` | `DELETE` | `api-version, projectName, resourceGroupName, subscriptionId` | Delete the project. Deleting non-existent project is a no-operation. |
| `Projects_AssessmentOptions` | `EXEC` | `api-version, assessmentOptionsName, projectName, resourceGroupName, subscriptionId` | Get all available options for the properties of an assessment on a project. |
| `Projects_AssessmentOptionsList` | `EXEC` | `api-version, projectName, resourceGroupName, subscriptionId` | Gets list of all available options for the properties of an assessment on a project. |
| `Projects_Update` | `EXEC` | `api-version, projectName, resourceGroupName, subscriptionId` | Update a project with specified name. Supports partial updates, for example only tags can be provided. |
