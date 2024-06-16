---
title: user_sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - user_sessions
  - desktop_virtualization
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
<tr><td><b>Name</b></td><td><code>user_sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.user_sessions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Schema for UserSession properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, sessionHostName, subscriptionId, userSessionId" /> | Get a userSession. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, sessionHostName, subscriptionId" /> | List userSessions. |
| <CopyableCode code="list_by_host_pool" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | List userSessions. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hostPoolName, resourceGroupName, sessionHostName, subscriptionId, userSessionId" /> | Remove a userSession. |
| <CopyableCode code="disconnect" /> | `EXEC` | <CopyableCode code="hostPoolName, resourceGroupName, sessionHostName, subscriptionId, userSessionId" /> | Disconnect a userSession. |
| <CopyableCode code="send_message" /> | `EXEC` | <CopyableCode code="hostPoolName, resourceGroupName, sessionHostName, subscriptionId, userSessionId" /> | Send a message to a user. |
