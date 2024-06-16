---
title: job_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - job_credentials
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
<tr><td><b>Name</b></td><td><code>job_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.job_credentials" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="credentialName, jobAgentName, resourceGroupName, serverName, subscriptionId" /> | Gets a jobs credential. |
| <CopyableCode code="list_by_agent" /> | `SELECT` | <CopyableCode code="jobAgentName, resourceGroupName, serverName, subscriptionId" /> | Gets a list of jobs credentials. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="credentialName, jobAgentName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates a job credential. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="credentialName, jobAgentName, resourceGroupName, serverName, subscriptionId" /> | Deletes a job credential. |
