---
title: virtual_machine_run_commands
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_run_commands
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
<tr><td><b>Name</b></td><td><code>virtual_machine_run_commands</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_run_commands" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The VM run command id. |
| <CopyableCode code="description" /> | `string` | The VM run command description. |
| <CopyableCode code="$schema" /> | `string` | The VM run command schema. |
| <CopyableCode code="label" /> | `string` | The VM run command label. |
| <CopyableCode code="osType" /> | `string` | The Operating System type. |
| <CopyableCode code="parameters" /> | `array` | The parameters used by the script. |
| <CopyableCode code="script" /> | `array` | The script to be executed. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="commandId, location, subscriptionId" /> | Gets specific run command for a subscription in a location. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Lists all available run commands for a subscription in a location. |
| <CopyableCode code="list_by_virtual_machine" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to get all run commands of a Virtual Machine. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, runCommandName, subscriptionId, vmName" /> | The operation to create or update the run command. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, runCommandName, subscriptionId, vmName" /> | The operation to delete the run command. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Lists all available run commands for a subscription in a location. |
| <CopyableCode code="_list_by_virtual_machine" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to get all run commands of a Virtual Machine. |
| <CopyableCode code="get_by_virtual_machine" /> | `EXEC` | <CopyableCode code="resourceGroupName, runCommandName, subscriptionId, vmName" /> | The operation to get the run command. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, runCommandName, subscriptionId, vmName" /> | The operation to update the run command. |
