---
title: job
hide_title: false
hide_table_of_contents: false
keywords:
  - job
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>job</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.job" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, serviceName, subscriptionId" /> | Get a Job and its properties. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="jobName, resourceGroupName, serviceName, subscriptionId" /> | Create a new Job or update an exiting Job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobName, resourceGroupName, serviceName, subscriptionId" /> | Operation to delete a Job. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, serviceName, subscriptionId" /> |  |
