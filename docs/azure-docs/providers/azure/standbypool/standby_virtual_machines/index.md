---
title: standby_virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - standby_virtual_machines
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
<tr><td><b>Name</b></td><td><code>standby_virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.standbypool.standby_virtual_machines" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, standbyVirtualMachineName, standbyVirtualMachinePoolName, subscriptionId" /> | Get a StandbyVirtualMachineResource |
| <CopyableCode code="list_by_standby_virtual_machine_pool_resource" /> | `SELECT` | <CopyableCode code="resourceGroupName, standbyVirtualMachinePoolName, subscriptionId" /> | List StandbyVirtualMachineResource resources by StandbyVirtualMachinePoolResource |
