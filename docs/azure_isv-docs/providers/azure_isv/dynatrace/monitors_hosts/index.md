---
title: monitors_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors_hosts
  - dynatrace
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>monitors_hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.dynatrace.monitors_hosts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="autoUpdateSetting" /> | `string` | Update settings of OneAgent. |
| <CopyableCode code="availabilityState" /> | `string` | The availability state of OneAgent. |
| <CopyableCode code="hostGroup" /> | `string` | The name of the host group |
| <CopyableCode code="hostName" /> | `string` | The name of the host |
| <CopyableCode code="logModule" /> | `string` | Tells whether log modules are enabled or not |
| <CopyableCode code="monitoringType" /> | `string` | The monitoring mode of OneAgent |
| <CopyableCode code="resourceId" /> | `string` | Azure VM resource ID |
| <CopyableCode code="updateStatus" /> | `string` | The current update status of OneAgent. |
| <CopyableCode code="version" /> | `string` | Version of the Dynatrace agent installed on the VM. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |
