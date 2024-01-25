---
title: sql_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_servers
  - azure_data
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
<tr><td><b>Name</b></td><td><code>sql_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.azure_data.sql_servers</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, sqlServerName, sqlServerRegistrationName, subscriptionId` | Gets a SQL Server. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, sqlServerRegistrationName, subscriptionId` | Gets all SQL Servers in a SQL Server Registration. |
| `create_or_update` | `INSERT` | `resourceGroupName, sqlServerName, sqlServerRegistrationName, subscriptionId` | Creates or updates a SQL Server. |
| `delete` | `DELETE` | `resourceGroupName, sqlServerName, sqlServerRegistrationName, subscriptionId` | Deletes a SQL Server. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, sqlServerRegistrationName, subscriptionId` | Gets all SQL Servers in a SQL Server Registration. |
