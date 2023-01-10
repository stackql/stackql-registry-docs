---
title: scripts
hide_title: false
hide_table_of_contents: false
keywords:
  - scripts
  - kusto
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
<tr><td><b>Name</b></td><td><code>scripts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.kusto.scripts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | A class representing database script property. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Scripts_Get` | `SELECT` | `clusterName, databaseName, resourceGroupName, scriptName, subscriptionId` | Gets a Kusto cluster database script. |
| `Scripts_ListByDatabase` | `SELECT` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Returns the list of database scripts for given database. |
| `Scripts_CreateOrUpdate` | `INSERT` | `clusterName, databaseName, resourceGroupName, scriptName, subscriptionId` | Creates a Kusto database script. |
| `Scripts_Delete` | `DELETE` | `clusterName, databaseName, resourceGroupName, scriptName, subscriptionId` | Deletes a Kusto principalAssignment. |
| `Scripts_CheckNameAvailability` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId, data__name, data__type` | Checks that the script name is valid and is not already in use. |
| `Scripts_Update` | `EXEC` | `clusterName, databaseName, resourceGroupName, scriptName, subscriptionId` | Updates a database script. |
