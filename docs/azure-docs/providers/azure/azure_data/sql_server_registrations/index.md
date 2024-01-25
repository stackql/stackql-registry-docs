---
title: sql_server_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_server_registrations
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
<tr><td><b>Name</b></td><td><code>sql_server_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.azure_data.sql_server_registrations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The SQL server Registration properties. |
| `systemData` | `object` | Read only system data |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, sqlServerRegistrationName, subscriptionId` | Gets a SQL Server registration. |
| `list` | `SELECT` | `subscriptionId` | Gets all SQL Server registrations in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all SQL Server registrations in a resource group. |
| `create_or_update` | `INSERT` | `resourceGroupName, sqlServerRegistrationName, subscriptionId, data__location` | Creates or updates a SQL Server registration. |
| `delete` | `DELETE` | `resourceGroupName, sqlServerRegistrationName, subscriptionId` | Deletes a SQL Server registration. |
| `_list` | `EXEC` | `subscriptionId` | Gets all SQL Server registrations in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all SQL Server registrations in a resource group. |
| `update` | `EXEC` | `resourceGroupName, sqlServerRegistrationName, subscriptionId` | Updates SQL Server Registration tags. |
