---
title: sql_server_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_server_instances
  - azure_arc_data
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
<tr><td><b>Name</b></td><td><code>sql_server_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.azure_arc_data.sql_server_instances</code></td></tr>
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
| `get` | `SELECT` | `api-version, resourceGroupName, sqlServerInstanceName, subscriptionId` | Retrieves a SQL Server Instance resource |
| `list` | `SELECT` | `api-version, subscriptionId` |  |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Gets all sqlServerInstances in a resource group. |
| `create` | `INSERT` | `api-version, resourceGroupName, sqlServerInstanceName, subscriptionId` | Creates or replaces a SQL Server Instance resource |
| `delete` | `DELETE` | `api-version, resourceGroupName, sqlServerInstanceName, subscriptionId` | Deletes a SQL Server Instance resource |
| `_list` | `EXEC` | `api-version, subscriptionId` |  |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | Gets all sqlServerInstances in a resource group. |
| `update` | `EXEC` | `api-version, resourceGroupName, sqlServerInstanceName, subscriptionId` | Updates a SQL Server Instance resource |
