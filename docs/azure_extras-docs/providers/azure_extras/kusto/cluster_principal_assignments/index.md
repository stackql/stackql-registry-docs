---
title: cluster_principal_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_principal_assignments
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
<tr><td><b>Name</b></td><td><code>cluster_principal_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.kusto.cluster_principal_assignments</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ClusterPrincipalAssignments_Get` | `SELECT` | `clusterName, principalAssignmentName, resourceGroupName, subscriptionId` | Gets a Kusto cluster principalAssignment. |
| `ClusterPrincipalAssignments_List` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Lists all Kusto cluster principalAssignments. |
| `ClusterPrincipalAssignments_CreateOrUpdate` | `INSERT` | `clusterName, principalAssignmentName, resourceGroupName, subscriptionId` | Create a Kusto cluster principalAssignment. |
| `ClusterPrincipalAssignments_Delete` | `DELETE` | `clusterName, principalAssignmentName, resourceGroupName, subscriptionId` | Deletes a Kusto cluster principalAssignment. |
| `ClusterPrincipalAssignments_CheckNameAvailability` | `EXEC` | `clusterName, resourceGroupName, subscriptionId, data__name, data__type` | Checks that the principal assignment name is valid and is not already in use. |
