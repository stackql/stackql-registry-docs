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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.storagetransfer.agent_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Specifies a unique string that identifies the agent pool. Format: `projects/&#123;project_id&#125;/agentPools/&#123;agent_pool_id&#125;` |
| `displayName` | `string` | Specifies the client-specified AgentPool description. |
| `state` | `string` | Output only. Specifies the state of the AgentPool. |
| `bandwidthLimit` | `object` | Specifies a bandwidth limit for an agent pool. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_agentPools_get` | `SELECT` | `agentPoolsId, projectsId` | Gets an agent pool. |
| `projects_agentPools_list` | `SELECT` | `projectsId` | Lists agent pools. |
| `projects_agentPools_create` | `INSERT` | `projectsId` | Creates an agent pool resource. |
| `projects_agentPools_delete` | `DELETE` | `agentPoolsId, projectsId` | Deletes an agent pool. |
| `projects_agentPools_patch` | `EXEC` | `agentPoolsId, projectsId` | Updates an existing agent pool resource. |
