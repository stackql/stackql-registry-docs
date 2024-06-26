---
title: devices_failover_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - devices_failover_sets
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
<tr><td><b>Name</b></td><td><code>devices_failover_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.devices_failover_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="eligibilityResult" /> | `object` | The eligibility result of failover set, for failover. |
| <CopyableCode code="volumeContainers" /> | `array` | The list of meta data of volume containers, which are part of the failover set. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> |
