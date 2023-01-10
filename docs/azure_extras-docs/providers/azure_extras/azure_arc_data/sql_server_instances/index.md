---
title: sql_server_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_server_instances
  - azure_arc_data
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
<tr><td><b>Name</b></td><td><code>sql_server_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.azure_arc_data.sql_server_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of SqlServerInstance. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SqlServerInstances_Get` | `SELECT` | `api-version, resourceGroupName, sqlServerInstanceName, subscriptionId` | Retrieves a SQL Server Instance resource |
| `SqlServerInstances_List` | `SELECT` | `api-version, subscriptionId` |  |
| `SqlServerInstances_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Gets all sqlServerInstances in a resource group. |
| `SqlServerInstances_Create` | `INSERT` | `api-version, resourceGroupName, sqlServerInstanceName, subscriptionId` | Creates or replaces a SQL Server Instance resource |
| `SqlServerInstances_Delete` | `DELETE` | `api-version, resourceGroupName, sqlServerInstanceName, subscriptionId` | Deletes a SQL Server Instance resource |
| `SqlServerInstances_Update` | `EXEC` | `api-version, resourceGroupName, sqlServerInstanceName, subscriptionId` | Updates a SQL Server Instance resource |
