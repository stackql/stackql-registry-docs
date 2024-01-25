---
title: replication_recovery_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_recovery_plans
  - recovery_services_site_recovery
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
<tr><td><b>Name</b></td><td><code>replication_recovery_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replication_recovery_plans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `location` | `string` | Resource Location |
| `properties` | `object` | Recovery plan properties. |
| `type` | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId` | Gets the details of the recovery plan. |
| `list` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists the recovery plans in the vault. |
| `create` | `INSERT` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to create a recovery plan. |
| `delete` | `DELETE` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId` | Delete a recovery plan. |
| `_list` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists the recovery plans in the vault. |
| `failover_cancel` | `EXEC` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId` | The operation to cancel the failover of a recovery plan. |
| `failover_commit` | `EXEC` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId` | The operation to commit the failover of a recovery plan. |
| `planned_failover` | `EXEC` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to start the planned failover of a recovery plan. |
| `reprotect` | `EXEC` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId` | The operation to reprotect(reverse replicate) a recovery plan. |
| `test_failover` | `EXEC` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to start the test failover of a recovery plan. |
| `test_failover_cleanup` | `EXEC` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to cleanup test failover of a recovery plan. |
| `unplanned_failover` | `EXEC` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to start the unplanned failover of a recovery plan. |
| `update` | `EXEC` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId` | The operation to update a recovery plan. |
