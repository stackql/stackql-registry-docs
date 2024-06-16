---
title: virtual_machine_scale_set_vm_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_set_vm_extensions
  - azurefleet
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
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_set_vm_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azurefleet.virtual_machine_scale_set_vm_extensions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | The name of the extension. |
| <CopyableCode code="location" /> | `string` | The location of the extension. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Virtual Machine Extension. |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmExtensionName, vmScaleSetName" /> | The operation to get the VMSS VM extension. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | The operation to get all extensions of an instance in Virtual Machine Scaleset. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmExtensionName, vmScaleSetName" /> | The operation to create or update the VMSS VM extension. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmExtensionName, vmScaleSetName" /> | The operation to delete the VMSS VM extension. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmExtensionName, vmScaleSetName" /> | The operation to update the VMSS VM extension. |
