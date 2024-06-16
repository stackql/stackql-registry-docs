---
title: devices_failover_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - devices_failover_targets
  - storsimple_8000_series
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>devices_failover_targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.devices_failover_targets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="availableLocalStorageInBytes" /> | `integer` | The amount of free local storage available on the device in bytes. |
| <CopyableCode code="availableTieredStorageInBytes" /> | `integer` | The amount of free tiered storage available for the device in bytes. |
| <CopyableCode code="dataContainersCount" /> | `integer` | The count of data containers on the device. |
| <CopyableCode code="deviceId" /> | `string` | The path ID of the device. |
| <CopyableCode code="deviceLocation" /> | `string` | The geo location (applicable only for cloud appliances) of the device. |
| <CopyableCode code="deviceSoftwareVersion" /> | `string` | The software version of the device. |
| <CopyableCode code="deviceStatus" /> | `string` | The status of the device. |
| <CopyableCode code="eligibilityResult" /> | `object` | The eligibility result of device, as a failover target device. |
| <CopyableCode code="friendlyDeviceSoftwareVersion" /> | `string` | The friendly name for the current version of software on the device. |
| <CopyableCode code="modelDescription" /> | `string` | The model number of the device. |
| <CopyableCode code="volumesCount" /> | `integer` | The count of volumes on the device. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, sourceDeviceName, subscriptionId" /> |
