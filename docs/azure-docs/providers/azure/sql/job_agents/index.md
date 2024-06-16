---
title: job_agents
hide_title: false
hide_table_of_contents: false
keywords:
  - job_agents
  - sql
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
<tr><td><b>Name</b></td><td><code>job_agents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.job_agents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of a job agent. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobAgentName, resourceGroupName, serverName, subscriptionId" /> | Gets a job agent. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of job agents in a server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="jobAgentName, resourceGroupName, serverName, subscriptionId, data__location" /> | Creates or updates a job agent. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobAgentName, resourceGroupName, serverName, subscriptionId" /> | Deletes a job agent. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="jobAgentName, resourceGroupName, serverName, subscriptionId" /> | Updates a job agent. |
