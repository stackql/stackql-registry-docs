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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_compute.agent_version" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="agentVersion" /> | `string` | Represents the agent version. |
| <CopyableCode code="downloadLink" /> | `string` | Represents the download link of specific agent version. |
| <CopyableCode code="osType" /> | `string` | Defines the os type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="osType, version" /> | Gets an Agent Version along with the download link currently present. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="osType" /> | Gets all Agent Versions along with the download link currently present. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="osType" /> | Gets all Agent Versions along with the download link currently present. |
