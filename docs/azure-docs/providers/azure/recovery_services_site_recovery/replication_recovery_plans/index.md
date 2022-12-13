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
| `type` | `string` | Resource Type |
| `location` | `string` | Resource Location |
| `properties` | `object` | Recovery plan properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReplicationRecoveryPlans_Get` | `SELECT` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId` | Gets the details of the recovery plan. |
| `ReplicationRecoveryPlans_List` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists the recovery plans in the vault. |
| `ReplicationRecoveryPlans_Create` | `INSERT` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to create a recovery plan. |
| `ReplicationRecoveryPlans_Delete` | `DELETE` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId` | Delete a recovery plan. |
| `ReplicationRecoveryPlans_FailoverCancel` | `EXEC` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId` | The operation to cancel the failover of a recovery plan. |
| `ReplicationRecoveryPlans_FailoverCommit` | `EXEC` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId` | The operation to commit the failover of a recovery plan. |
| `ReplicationRecoveryPlans_PlannedFailover` | `EXEC` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to start the planned failover of a recovery plan. |
| `ReplicationRecoveryPlans_Reprotect` | `EXEC` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId` | The operation to reprotect(reverse replicate) a recovery plan. |
| `ReplicationRecoveryPlans_TestFailover` | `EXEC` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to start the test failover of a recovery plan. |
| `ReplicationRecoveryPlans_TestFailoverCleanup` | `EXEC` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to cleanup test failover of a recovery plan. |
| `ReplicationRecoveryPlans_UnplannedFailover` | `EXEC` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to start the unplanned failover of a recovery plan. |
| `ReplicationRecoveryPlans_Update` | `EXEC` | `api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId` | The operation to update a recovery plan. |
