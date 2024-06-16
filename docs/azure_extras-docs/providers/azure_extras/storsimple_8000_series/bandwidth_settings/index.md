---
title: bandwidth_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - bandwidth_settings
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
<tr><td><b>Name</b></td><td><code>bandwidth_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.bandwidth_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The name of the object. |
| <CopyableCode code="kind" /> | `string` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="properties" /> | `object` | The properties of the bandwidth setting. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bandwidthSettingName, managerName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified bandwidth setting name. |
| <CopyableCode code="list_by_manager" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Retrieves all the bandwidth setting in a manager. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="bandwidthSettingName, managerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates the bandwidth setting |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bandwidthSettingName, managerName, resourceGroupName, subscriptionId" /> | Deletes the bandwidth setting |
