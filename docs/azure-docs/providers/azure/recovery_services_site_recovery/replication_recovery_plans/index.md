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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_recovery_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_recovery_plans" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Recovery plan properties. |
| <CopyableCode code="type" /> | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of the recovery plan. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Lists the recovery plans in the vault. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to create a recovery plan. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId" /> | Delete a recovery plan. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Lists the recovery plans in the vault. |
| <CopyableCode code="failover_cancel" /> | `EXEC` | <CopyableCode code="api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId" /> | The operation to cancel the failover of a recovery plan. |
| <CopyableCode code="failover_commit" /> | `EXEC` | <CopyableCode code="api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId" /> | The operation to commit the failover of a recovery plan. |
| <CopyableCode code="planned_failover" /> | `EXEC` | <CopyableCode code="api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to start the planned failover of a recovery plan. |
| <CopyableCode code="reprotect" /> | `EXEC` | <CopyableCode code="api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId" /> | The operation to reprotect(reverse replicate) a recovery plan. |
| <CopyableCode code="test_failover" /> | `EXEC` | <CopyableCode code="api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to start the test failover of a recovery plan. |
| <CopyableCode code="test_failover_cleanup" /> | `EXEC` | <CopyableCode code="api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to cleanup test failover of a recovery plan. |
| <CopyableCode code="unplanned_failover" /> | `EXEC` | <CopyableCode code="api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to start the unplanned failover of a recovery plan. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, recoveryPlanName, resourceGroupName, resourceName, subscriptionId" /> | The operation to update a recovery plan. |
