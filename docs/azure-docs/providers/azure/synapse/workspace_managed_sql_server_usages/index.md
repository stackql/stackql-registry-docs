---
title: workspace_managed_sql_server_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_managed_sql_server_usages
  - synapse
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
<tr><td><b>Name</b></td><td><code>workspace_managed_sql_server_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.workspace_managed_sql_server_usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the server usage metric. |
| `nextResetTime` | `string` | The next reset time for the metric (ISO8601 format). |
| `resourceName` | `string` | The name of the resource. |
| `unit` | `string` | The units of the metric. |
| `currentValue` | `number` | The current value of the metric. |
| `displayName` | `string` | The metric display name. |
| `limit` | `number` | The current limit of the metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `WorkspaceManagedSqlServerUsages_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
