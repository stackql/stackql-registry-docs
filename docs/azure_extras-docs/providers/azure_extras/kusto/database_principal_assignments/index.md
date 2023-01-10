---
title: database_principal_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - database_principal_assignments
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
<tr><td><b>Name</b></td><td><code>database_principal_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.kusto.database_principal_assignments</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DatabasePrincipalAssignments_Get` | `SELECT` | `clusterName, databaseName, principalAssignmentName, resourceGroupName, subscriptionId` | Gets a Kusto cluster database principalAssignment. |
| `DatabasePrincipalAssignments_List` | `SELECT` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Lists all Kusto cluster database principalAssignments. |
| `DatabasePrincipalAssignments_CreateOrUpdate` | `INSERT` | `clusterName, databaseName, principalAssignmentName, resourceGroupName, subscriptionId` | Creates a Kusto cluster database principalAssignment. |
| `DatabasePrincipalAssignments_Delete` | `DELETE` | `clusterName, databaseName, principalAssignmentName, resourceGroupName, subscriptionId` | Deletes a Kusto principalAssignment. |
| `DatabasePrincipalAssignments_CheckNameAvailability` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId, data__name, data__type` | Checks that the database principal assignment is valid and is not already in use. |
