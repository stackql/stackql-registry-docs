---
title: groups_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - groups_operations
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
<tr><td><b>Name</b></td><td><code>groups_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.migrate.groups_operations</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `groupName, projectName, resourceGroupName, subscriptionId` | Get a Group |
| `list_by_assessment_project` | `SELECT` | `projectName, resourceGroupName, subscriptionId` | List Group resources by AssessmentProject |
| `create` | `INSERT` | `groupName, projectName, resourceGroupName, subscriptionId` | Create a Group |
| `delete` | `DELETE` | `groupName, projectName, resourceGroupName, subscriptionId` | Delete a Group |
| `_list_by_assessment_project` | `EXEC` | `projectName, resourceGroupName, subscriptionId` | List Group resources by AssessmentProject |
