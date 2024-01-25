---
title: server_collectors_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - server_collectors_operations
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
<tr><td><b>Name</b></td><td><code>server_collectors_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.migrate.server_collectors_operations</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `projectName, resourceGroupName, serverCollectorName, subscriptionId` | Get a ServerCollector |
| `list_by_assessment_project` | `SELECT` | `projectName, resourceGroupName, subscriptionId` | List ServerCollector resources by AssessmentProject |
| `create` | `INSERT` | `projectName, resourceGroupName, serverCollectorName, subscriptionId` | Create a ServerCollector |
| `delete` | `DELETE` | `projectName, resourceGroupName, serverCollectorName, subscriptionId` | Delete a ServerCollector |
| `_list_by_assessment_project` | `EXEC` | `projectName, resourceGroupName, subscriptionId` | List ServerCollector resources by AssessmentProject |
