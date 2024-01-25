---
title: scripts
hide_title: false
hide_table_of_contents: false
keywords:
  - scripts
  - data_explorer
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
<tr><td><b>Name</b></td><td><code>scripts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_explorer.scripts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | A class representing database script property. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, databaseName, resourceGroupName, scriptName, subscriptionId` | Gets a Kusto cluster database script. |
| `list_by_database` | `SELECT` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Returns the list of database scripts for given database. |
| `create_or_update` | `INSERT` | `clusterName, databaseName, resourceGroupName, scriptName, subscriptionId` | Creates a Kusto database script. |
| `delete` | `DELETE` | `clusterName, databaseName, resourceGroupName, scriptName, subscriptionId` | Deletes a Kusto database script. |
| `_list_by_database` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Returns the list of database scripts for given database. |
| `check_name_availability` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId, data__name, data__type` | Checks that the script name is valid and is not already in use. |
| `update` | `EXEC` | `clusterName, databaseName, resourceGroupName, scriptName, subscriptionId` | Updates a database script. |
