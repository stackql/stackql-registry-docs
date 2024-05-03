---
title: agent_pool
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pool
  - hybrid_aks
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
<tr><td><b>Name</b></td><td><code>agent_pool</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_aks.agent_pool" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | Extended location pointing to the underlying infrastructure |
| <CopyableCode code="properties" /> | `object` | Properties of the agent pool resource |
| <CopyableCode code="tags" /> | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="agentPoolName, connectedClusterResourceUri" /> | Gets the specified agent pool in the provisioned cluster |
| <CopyableCode code="list_by_provisioned_cluster" /> | `SELECT` | <CopyableCode code="connectedClusterResourceUri" /> | Gets the list of agent pools in the specified provisioned cluster |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="agentPoolName, connectedClusterResourceUri" /> | Creates or updates the agent pool in the provisioned cluster |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="agentPoolName, connectedClusterResourceUri" /> | Deletes the specified agent pool in the provisioned cluster |
| <CopyableCode code="_list_by_provisioned_cluster" /> | `EXEC` | <CopyableCode code="connectedClusterResourceUri" /> | Gets the list of agent pools in the specified provisioned cluster |
