---
title: agent_version
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_version
  - hybrid_compute
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_compute.agent_version</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `agentVersion` | `string` | Represents the agent version. |
| `downloadLink` | `string` | Represents the download link of specific agent version. |
| `osType` | `string` | Defines the os type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `osType, version` | Gets an Agent Version along with the download link currently present. |
| `list` | `SELECT` | `osType` | Gets all Agent Versions along with the download link currently present. |
| `_list` | `EXEC` | `osType` | Gets all Agent Versions along with the download link currently present. |
