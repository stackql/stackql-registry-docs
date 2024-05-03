---
title: sql_virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_virtual_machines
  - sql_vm
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
<tr><td><b>Name</b></td><td><code>sql_virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql_vm.sql_virtual_machines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Azure Active Directory identity configuration for a resource. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The SQL virtual machine properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlVirtualMachineName, subscriptionId" /> | Gets a SQL virtual machine. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all SQL virtual machines in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all SQL virtual machines in a resource group. |
| <CopyableCode code="list_by_sql_vm_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlVirtualMachineGroupName, subscriptionId" /> | Gets the list of sql virtual machines in a SQL virtual machine group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, sqlVirtualMachineName, subscriptionId, data__location" /> | Creates or updates a SQL virtual machine. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sqlVirtualMachineName, subscriptionId" /> | Deletes a SQL virtual machine. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Gets all SQL virtual machines in a subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all SQL virtual machines in a resource group. |
| <CopyableCode code="_list_by_sql_vm_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlVirtualMachineGroupName, subscriptionId" /> | Gets the list of sql virtual machines in a SQL virtual machine group. |
| <CopyableCode code="redeploy" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlVirtualMachineName, subscriptionId" /> | Uninstalls and reinstalls the SQL IaaS Extension. |
| <CopyableCode code="start_assessment" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlVirtualMachineName, subscriptionId" /> | Starts SQL best practices Assessment on SQL virtual machine. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlVirtualMachineName, subscriptionId" /> | Updates a SQL virtual machine. |
