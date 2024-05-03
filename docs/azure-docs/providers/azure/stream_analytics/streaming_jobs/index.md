---
title: streaming_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_jobs
  - stream_analytics
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
<tr><td><b>Name</b></td><td><code>streaming_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.stream_analytics.streaming_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Describes how identity is verified |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties that are associated with a streaming job. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Gets details about the specified streaming job. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the streaming jobs in the given subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the streaming jobs in the specified resource group. |
| <CopyableCode code="create_or_replace" /> | `INSERT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Creates a streaming job or replaces an already existing streaming job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Deletes a streaming job. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all of the streaming jobs in the given subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the streaming jobs in the specified resource group. |
| <CopyableCode code="scale" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Scales a streaming job when the job is running. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Starts a streaming job. Once a job is started it will start processing input events and produce output. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Stops a running streaming job. This will cause a running streaming job to stop processing input events and producing output. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Updates an existing streaming job. This can be used to partially update (ie. update one or two properties) a streaming job without affecting the rest the job definition. |
