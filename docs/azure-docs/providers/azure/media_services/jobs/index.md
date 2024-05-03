---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - media_services
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of the Job. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, api-version, jobName, resourceGroupName, subscriptionId, transformName" /> | Gets a Job. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId, transformName" /> | Lists all of the Jobs for the Transform. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, api-version, jobName, resourceGroupName, subscriptionId, transformName" /> | Creates a Job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, api-version, jobName, resourceGroupName, subscriptionId, transformName" /> | Deletes a Job. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId, transformName" /> | Lists all of the Jobs for the Transform. |
| <CopyableCode code="cancel_job" /> | `EXEC` | <CopyableCode code="accountName, api-version, jobName, resourceGroupName, subscriptionId, transformName" /> | Cancel a Job. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, api-version, jobName, resourceGroupName, subscriptionId, transformName" /> | Update is only supported for description and priority. Updating Priority will take effect when the Job state is Queued or Scheduled and depending on the timing the priority update may be ignored. |
