---
title: standby_virtual_machine_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - standby_virtual_machine_pools
  - standbypool
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
<tr><td><b>Name</b></td><td><code>standby_virtual_machine_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.standbypool.standby_virtual_machine_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Details of the StandbyVirtualMachinePool. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, standbyVirtualMachinePoolName, subscriptionId" /> | Get a StandbyVirtualMachinePoolResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List StandbyVirtualMachinePoolResource resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List StandbyVirtualMachinePoolResource resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, standbyVirtualMachinePoolName, subscriptionId" /> | Create a StandbyVirtualMachinePoolResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, standbyVirtualMachinePoolName, subscriptionId" /> | Delete a StandbyVirtualMachinePoolResource |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, standbyVirtualMachinePoolName, subscriptionId" /> | Update a StandbyVirtualMachinePoolResource |
