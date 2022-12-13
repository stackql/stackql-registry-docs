---
title: service_objectives
hide_title: false
hide_table_of_contents: false
keywords:
  - service_objectives
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
<tr><td><b>Name</b></td><td><code>service_objectives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.service_objectives</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServiceObjectives_Get` | `SELECT` | `resourceGroupName, serverName, serviceObjectiveName, subscriptionId` | Gets a database service objective. |
| `ServiceObjectives_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Returns database service objectives. |
