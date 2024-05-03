---
title: file_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - file_shares
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
<tr><td><b>Name</b></td><td><code>file_shares</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.file_shares" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="properties" /> | `object` | The File Share. |
| <CopyableCode code="type" /> | `string` | The type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, fileServerName, managerName, resourceGroupName, shareName, subscriptionId" /> | Returns the properties of the specified file share name. |
| <CopyableCode code="list_by_device" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the file shares in a device. |
| <CopyableCode code="list_by_file_server" /> | `SELECT` | <CopyableCode code="deviceName, fileServerName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the file shares in a file server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deviceName, fileServerName, managerName, resourceGroupName, shareName, subscriptionId, data__properties" /> | Creates or updates the file share. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceName, fileServerName, managerName, resourceGroupName, shareName, subscriptionId" /> | Deletes the file share. |
| <CopyableCode code="_list_by_device" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the file shares in a device. |
| <CopyableCode code="_list_by_file_server" /> | `EXEC` | <CopyableCode code="deviceName, fileServerName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the file shares in a file server. |
