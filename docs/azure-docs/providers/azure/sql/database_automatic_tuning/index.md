---
title: database_automatic_tuning
hide_title: false
hide_table_of_contents: false
keywords:
  - database_automatic_tuning
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
<tr><td><b>Name</b></td><td><code>database_automatic_tuning</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.database_automatic_tuning</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DatabaseAutomaticTuning_Get` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets a database's automatic tuning. |
| `DatabaseAutomaticTuning_Update` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Update automatic tuning properties for target database. |
