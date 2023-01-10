---
title: sql_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_servers
  - azure_data
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.azure_data.sql_servers</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SqlServers_Get` | `SELECT` | `resourceGroupName, sqlServerName, sqlServerRegistrationName, subscriptionId` | Gets a SQL Server. |
| `SqlServers_ListByResourceGroup` | `SELECT` | `resourceGroupName, sqlServerRegistrationName, subscriptionId` | Gets all SQL Servers in a SQL Server Registration. |
| `SqlServers_CreateOrUpdate` | `INSERT` | `resourceGroupName, sqlServerName, sqlServerRegistrationName, subscriptionId` | Creates or updates a SQL Server. |
| `SqlServers_Delete` | `DELETE` | `resourceGroupName, sqlServerName, sqlServerRegistrationName, subscriptionId` | Deletes a SQL Server. |
