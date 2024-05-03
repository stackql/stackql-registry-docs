---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.jobs" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobAgentName, jobName, resourceGroupName, serverName, subscriptionId" /> | Gets a job. |
| <CopyableCode code="list_by_agent" /> | `SELECT` | <CopyableCode code="jobAgentName, resourceGroupName, serverName, subscriptionId" /> | Gets a list of jobs. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="jobAgentName, jobName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates a job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobAgentName, jobName, resourceGroupName, serverName, subscriptionId" /> | Deletes a job. |
| <CopyableCode code="_list_by_agent" /> | `EXEC` | <CopyableCode code="jobAgentName, resourceGroupName, serverName, subscriptionId" /> | Gets a list of jobs. |
