---
title: kusto_pool_database_principal_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pool_database_principal_assignments
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
<tr><td><b>Name</b></td><td><code>kusto_pool_database_principal_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.kusto_pool_database_principal_assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | A class representing database principal property. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databaseName, kustoPoolName, principalAssignmentName, resourceGroupName, subscriptionId, workspaceName` | Gets a Kusto pool database principalAssignment. |
| `list` | `SELECT` | `databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Lists all Kusto pool database principalAssignments. |
| `create_or_update` | `INSERT` | `databaseName, kustoPoolName, principalAssignmentName, resourceGroupName, subscriptionId, workspaceName` | Creates a Kusto pool database principalAssignment. |
| `delete` | `DELETE` | `databaseName, kustoPoolName, principalAssignmentName, resourceGroupName, subscriptionId, workspaceName` | Deletes a Kusto pool principalAssignment. |
| `_list` | `EXEC` | `databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Lists all Kusto pool database principalAssignments. |
| `check_name_availability` | `EXEC` | `databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__name, data__type` | Checks that the database principal assignment is valid and is not already in use. |
