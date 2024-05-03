---
title: agent_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pools
  - storagetransfer
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.storagetransfer.agent_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Specifies a unique string that identifies the agent pool. Format: `projects/&#123;project_id&#125;/agentPools/&#123;agent_pool_id&#125;` |
| <CopyableCode code="bandwidthLimit" /> | `object` | Specifies a bandwidth limit for an agent pool. |
| <CopyableCode code="displayName" /> | `string` | Specifies the client-specified AgentPool description. |
| <CopyableCode code="state" /> | `string` | Output only. Specifies the state of the AgentPool. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="agentPoolsId, projectsId" /> | Gets an agent pool. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists agent pools. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates an agent pool resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="agentPoolsId, projectsId" /> | Deletes an agent pool. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Lists agent pools. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="agentPoolsId, projectsId" /> | Updates an existing agent pool resource. |
