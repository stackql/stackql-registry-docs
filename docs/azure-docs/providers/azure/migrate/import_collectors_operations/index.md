---
title: import_collectors_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - import_collectors_operations
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
<tr><td><b>Name</b></td><td><code>import_collectors_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.migrate.import_collectors_operations</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `importCollectorName, projectName, resourceGroupName, subscriptionId` | Get a ImportCollector |
| `list_by_assessment_project` | `SELECT` | `projectName, resourceGroupName, subscriptionId` | List ImportCollector resources by AssessmentProject |
| `create` | `INSERT` | `importCollectorName, projectName, resourceGroupName, subscriptionId` | Create a ImportCollector |
| `delete` | `DELETE` | `importCollectorName, projectName, resourceGroupName, subscriptionId` | Delete a ImportCollector |
| `_list_by_assessment_project` | `EXEC` | `projectName, resourceGroupName, subscriptionId` | List ImportCollector resources by AssessmentProject |
