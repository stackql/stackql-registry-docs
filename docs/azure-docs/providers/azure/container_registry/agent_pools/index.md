---
title: agent_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pools
  - container_registry
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.agent_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. This cannot be changed after the resource is created. |
| <CopyableCode code="properties" /> | `object` | The properties of agent pool. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="agentPoolName, registryName, resourceGroupName, subscriptionId" /> | Gets the detailed information for a given agent pool. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all the agent pools for a specified container registry. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="agentPoolName, registryName, resourceGroupName, subscriptionId" /> | Creates an agent pool for a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="agentPoolName, registryName, resourceGroupName, subscriptionId" /> | Deletes a specified agent pool resource. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="agentPoolName, registryName, resourceGroupName, subscriptionId" /> | Updates an agent pool with the specified parameters. |
