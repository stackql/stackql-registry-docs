---
title: recommended_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - recommended_actions
  - mysql
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
<tr><td><b>Name</b></td><td><code>recommended_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mysql.recommended_actions</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `RecommendedActions_Get` | `SELECT` | `advisorName, recommendedActionName, resourceGroupName, serverName, subscriptionId` |
| `RecommendedActions_ListByServer` | `SELECT` | `advisorName, resourceGroupName, serverName, subscriptionId` |
