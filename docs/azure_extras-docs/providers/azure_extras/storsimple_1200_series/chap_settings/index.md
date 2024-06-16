---
title: chap_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - chap_settings
  - storsimple_1200_series
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
<tr><td><b>Name</b></td><td><code>chap_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.chap_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="properties" /> | `object` | Chap properties |
| <CopyableCode code="type" /> | `string` | The type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="chapUserName, deviceName, managerName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified chap setting name. |
| <CopyableCode code="list_by_device" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the chap settings in a device. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="chapUserName, deviceName, managerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates the chap setting. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="chapUserName, deviceName, managerName, resourceGroupName, subscriptionId" /> | Deletes the chap setting. |
