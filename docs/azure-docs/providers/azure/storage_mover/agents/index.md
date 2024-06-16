---
title: agents
hide_title: false
hide_table_of_contents: false
keywords:
  - agents
  - storage_mover
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
<tr><td><b>Name</b></td><td><code>agents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_mover.agents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="agentName, resourceGroupName, storageMoverName, subscriptionId" /> | Gets an Agent resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageMoverName, subscriptionId" /> | Lists all Agents in a Storage Mover. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="agentName, resourceGroupName, storageMoverName, subscriptionId, data__properties" /> | Creates or updates an Agent resource, which references a hybrid compute machine that can run jobs. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="agentName, resourceGroupName, storageMoverName, subscriptionId" /> | Deletes an Agent resource. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="agentName, resourceGroupName, storageMoverName, subscriptionId" /> | Creates or updates an Agent resource. |
