---
title: agent_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pools
  - aks
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
<tr><td><b>Name</b></td><td><code>agent_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aks.agent_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="properties" /> | `object` | Properties for the container service agent pool profile. |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="agentPoolName, resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="agentPoolName, resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="agentPoolName, resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="abort_latest_operation" /> | `EXEC` | <CopyableCode code="agentPoolName, resourceGroupName, resourceName, subscriptionId" /> | Aborts the currently running operation on the agent pool. The Agent Pool will be moved to a Canceling state and eventually to a Canceled state when cancellation finishes. If the operation completes before cancellation can take place, an error is returned. |
| <CopyableCode code="upgrade_node_image_version" /> | `EXEC` | <CopyableCode code="agentPoolName, resourceGroupName, resourceName, subscriptionId" /> | Upgrading the node image version of an agent pool applies the newest OS and runtime updates to the nodes. AKS provides one new image per week with the latest updates. For more details on node image versions, see: https://docs.microsoft.com/azure/aks/node-image-upgrade |
