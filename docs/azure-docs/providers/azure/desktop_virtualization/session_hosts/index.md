---
title: session_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - session_hosts
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
<tr><td><b>Name</b></td><td><code>session_hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.session_hosts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Schema for SessionHost properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, sessionHostName, subscriptionId" /> | Get a session host. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | List sessionHosts. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hostPoolName, resourceGroupName, sessionHostName, subscriptionId" /> | Remove a SessionHost. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | List sessionHosts. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="hostPoolName, resourceGroupName, sessionHostName, subscriptionId" /> | Update a session host. |
