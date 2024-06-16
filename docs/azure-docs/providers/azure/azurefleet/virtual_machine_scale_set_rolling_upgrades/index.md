---
title: virtual_machine_scale_set_rolling_upgrades
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_set_rolling_upgrades
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
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_set_rolling_upgrades</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azurefleet.virtual_machine_scale_set_rolling_upgrades" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Cancels the current virtual machine scale set rolling upgrade. |
| <CopyableCode code="start_extension_upgrade" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Starts a rolling upgrade to move all extensions for all virtual machine scale set instances to the latest available extension version. Instances which are already running the latest extension versions are not affected. |
| <CopyableCode code="start_os_upgrade" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Starts a rolling upgrade to move all virtual machine scale set instances to the latest available Platform Image OS version. Instances which are already running the latest available OS version are not affected. |
