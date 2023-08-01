---
title: sql_pool_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_usages
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
<tr><td><b>Name</b></td><td><code>sql_pool_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.sql_pool_usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the usage metric. |
| `resourceName` | `string` | The name of the resource. |
| `unit` | `string` | The units of the usage metric. |
| `currentValue` | `number` | The current value of the usage metric. |
| `displayName` | `string` | The usage metric display name. |
| `limit` | `number` | The current limit of the usage metric. |
| `nextResetTime` | `string` | The next reset time for the usage metric (ISO8601 format). |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `SqlPoolUsages_List` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` |
