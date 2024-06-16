---
title: virtual_machine_scale_sets_instance_view
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_sets_instance_view
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
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_sets_instance_view</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azurefleet.virtual_machine_scale_sets_instance_view" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extensions" /> | `array` | The extensions information. |
| <CopyableCode code="orchestrationServices" /> | `array` | The orchestration services information. |
| <CopyableCode code="statuses" /> | `array` | The resource status information. |
| <CopyableCode code="virtualMachine" /> | `object` | Instance view statuses summary for virtual machines of a virtual machine scale set. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> |
