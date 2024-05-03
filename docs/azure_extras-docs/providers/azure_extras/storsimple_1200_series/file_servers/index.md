---
title: file_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - file_servers
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
<tr><td><b>Name</b></td><td><code>file_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.file_servers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="properties" /> | `object` | The file server properties. |
| <CopyableCode code="type" /> | `string` | The type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, fileServerName, managerName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified file server name. |
| <CopyableCode code="list_by_device" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the file servers in a device. |
| <CopyableCode code="list_by_manager" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Retrieves all the file servers in a manager. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deviceName, fileServerName, managerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates the file server. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceName, fileServerName, managerName, resourceGroupName, subscriptionId" /> | Deletes the file server. |
| <CopyableCode code="_list_by_device" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the file servers in a device. |
| <CopyableCode code="_list_by_manager" /> | `EXEC` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Retrieves all the file servers in a manager. |
| <CopyableCode code="backup_now" /> | `EXEC` | <CopyableCode code="deviceName, fileServerName, managerName, resourceGroupName, subscriptionId" /> | Backup the file server now. |
