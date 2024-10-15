---
title: devices_failover_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - devices_failover_targets
  - storsimple_8000_series
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>devices_failover_targets</code> resource.

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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, sourceDeviceName, subscriptionId" /> | Given a list of volume containers to be failed over from a source device, this method returns the eligibility result, as a failover target, for all devices under that resource. |

## `SELECT` examples

Given a list of volume containers to be failed over from a source device, this method returns the eligibility result, as a failover target, for all devices under that resource.


```sql
SELECT
availableLocalStorageInBytes,
availableTieredStorageInBytes,
dataContainersCount,
deviceId,
deviceLocation,
deviceSoftwareVersion,
deviceStatus,
eligibilityResult,
friendlyDeviceSoftwareVersion,
modelDescription,
volumesCount
FROM azure_extras.storsimple_8000_series.devices_failover_targets
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sourceDeviceName = '{{ sourceDeviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```