---
title: job_steps
hide_title: false
hide_table_of_contents: false
keywords:
  - job_steps
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
<tr><td><b>Name</b></td><td><code>job_steps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.job_steps" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobAgentName, jobName, resourceGroupName, serverName, stepName, subscriptionId" /> | Gets a job step in a job's current version. |
| <CopyableCode code="list_by_job" /> | `SELECT` | <CopyableCode code="jobAgentName, jobName, resourceGroupName, serverName, subscriptionId" /> | Gets all job steps for a job's current version. |
| <CopyableCode code="list_by_version" /> | `SELECT` | <CopyableCode code="jobAgentName, jobName, jobVersion, resourceGroupName, serverName, subscriptionId" /> | Gets all job steps in the specified job version. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="jobAgentName, jobName, resourceGroupName, serverName, stepName, subscriptionId" /> | Creates or updates a job step. This will implicitly create a new job version. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobAgentName, jobName, resourceGroupName, serverName, stepName, subscriptionId" /> | Deletes a job step. This will implicitly create a new job version. |
| <CopyableCode code="get_by_version" /> | `EXEC` | <CopyableCode code="jobAgentName, jobName, jobVersion, resourceGroupName, serverName, stepName, subscriptionId" /> | Gets the specified version of a job step. |
