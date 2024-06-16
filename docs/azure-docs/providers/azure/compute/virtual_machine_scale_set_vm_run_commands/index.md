---
title: virtual_machine_scale_set_vm_run_commands
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_set_vm_run_commands
  - compute
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
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_set_vm_run_commands</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_scale_set_vm_run_commands" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Virtual Machine run command. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instanceId, resourceGroupName, runCommandName, subscriptionId, vmScaleSetName" /> | The operation to get the VMSS VM run command. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | The operation to get all run commands of an instance in Virtual Machine Scaleset. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="instanceId, resourceGroupName, runCommandName, subscriptionId, vmScaleSetName" /> | The operation to create or update the VMSS VM run command. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instanceId, resourceGroupName, runCommandName, subscriptionId, vmScaleSetName" /> | The operation to delete the VMSS VM run command. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="instanceId, resourceGroupName, runCommandName, subscriptionId, vmScaleSetName" /> | The operation to update the VMSS VM run command. |
