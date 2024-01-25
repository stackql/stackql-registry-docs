---
title: sql_collector_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_collector_operations
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
<tr><td><b>Name</b></td><td><code>sql_collector_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.migrate.sql_collector_operations</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `collectorName, projectName, resourceGroupName, subscriptionId` | Get a SqlCollector |
| `list_by_assessment_project` | `SELECT` | `projectName, resourceGroupName, subscriptionId` | List SqlCollector resources by AssessmentProject |
| `create` | `INSERT` | `collectorName, projectName, resourceGroupName, subscriptionId` | Create a SqlCollector |
| `delete` | `DELETE` | `collectorName, projectName, resourceGroupName, subscriptionId` | Delete a SqlCollector |
| `_list_by_assessment_project` | `EXEC` | `projectName, resourceGroupName, subscriptionId` | List SqlCollector resources by AssessmentProject |
