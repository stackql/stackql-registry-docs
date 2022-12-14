---
title: database_recommended_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - database_recommended_actions
  - sql
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
<tr><td><b>Name</b></td><td><code>database_recommended_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.database_recommended_actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Resource kind. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties for a Database, Server or Elastic Pool Recommended Action. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DatabaseRecommendedActions_Get` | `SELECT` | `advisorName, databaseName, recommendedActionName, resourceGroupName, serverName, subscriptionId` | Gets a database recommended action. |
| `DatabaseRecommendedActions_ListByDatabaseAdvisor` | `SELECT` | `advisorName, databaseName, resourceGroupName, serverName, subscriptionId` | Gets list of Database Recommended Actions. |
| `DatabaseRecommendedActions_Update` | `EXEC` | `advisorName, databaseName, recommendedActionName, resourceGroupName, serverName, subscriptionId` | Updates a database recommended action. |
