---
title: connected_environments_storages
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_environments_storages
  - container_apps
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
<tr><td><b>Name</b></td><td><code>connected_environments_storages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.connected_environments_storages" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, storageName, subscriptionId" /> | Get storage for a connectedEnvironment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, subscriptionId" /> | Get all storages for a connectedEnvironment. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, storageName, subscriptionId" /> | Create or update storage for a connectedEnvironment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, storageName, subscriptionId" /> | Delete storage for a connectedEnvironment. |
