---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
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
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.devices" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The name of the object. |
| <CopyableCode code="kind" /> | `string` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="properties" /> | `object` | The properties of the StorSimple device. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified device. |
| <CopyableCode code="list_by_manager" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Returns the list of devices for the specified manager. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Deletes the device. |
| <CopyableCode code="authorize_for_service_encryption_key_rollover" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Authorizes the specified device for service data encryption key rollover. |
| <CopyableCode code="configure" /> | `EXEC` | <CopyableCode code="managerName, resourceGroupName, subscriptionId, data__properties" /> | Complete minimal setup before using the device. |
| <CopyableCode code="deactivate" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Deactivates the device. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="managerName, resourceGroupName, sourceDeviceName, subscriptionId" /> | Failovers a set of volume containers from a specified source device to a target device. |
| <CopyableCode code="install_updates" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Downloads and installs the updates on the device. |
| <CopyableCode code="scan_for_updates" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Scans for updates on the device. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId, data__properties" /> | Patches the device. |
