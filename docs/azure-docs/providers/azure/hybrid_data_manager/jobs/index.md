---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - hybrid_data_manager
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_data_manager.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the object. |
| <CopyableCode code="name" /> | `string` | Name of the object. |
| <CopyableCode code="endTime" /> | `string` | Time at which the job ended in UTC ISO 8601 format. |
| <CopyableCode code="error" /> | `object` | Top level error for the job. |
| <CopyableCode code="properties" /> | `object` | Job Properties |
| <CopyableCode code="startTime" /> | `string` | Time at which the job was started in UTC ISO 8601 format. |
| <CopyableCode code="status" /> | `string` | Status of the job. |
| <CopyableCode code="type" /> | `string` | Type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataManagerName, dataServiceName, jobDefinitionName, jobId, resourceGroupName, subscriptionId" /> | This method gets a data manager job given the jobId. |
| <CopyableCode code="list_by_data_manager" /> | `SELECT` | <CopyableCode code="dataManagerName, resourceGroupName, subscriptionId" /> | This method gets all the jobs at the data manager resource level. |
| <CopyableCode code="list_by_data_service" /> | `SELECT` | <CopyableCode code="dataManagerName, dataServiceName, resourceGroupName, subscriptionId" /> | This method gets all the jobs of a data service type in a given resource. |
| <CopyableCode code="list_by_job_definition" /> | `SELECT` | <CopyableCode code="dataManagerName, dataServiceName, jobDefinitionName, resourceGroupName, subscriptionId" /> | This method gets all the jobs of a given job definition. |
| <CopyableCode code="_list_by_data_manager" /> | `EXEC` | <CopyableCode code="dataManagerName, resourceGroupName, subscriptionId" /> | This method gets all the jobs at the data manager resource level. |
| <CopyableCode code="_list_by_data_service" /> | `EXEC` | <CopyableCode code="dataManagerName, dataServiceName, resourceGroupName, subscriptionId" /> | This method gets all the jobs of a data service type in a given resource. |
| <CopyableCode code="_list_by_job_definition" /> | `EXEC` | <CopyableCode code="dataManagerName, dataServiceName, jobDefinitionName, resourceGroupName, subscriptionId" /> | This method gets all the jobs of a given job definition. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="dataManagerName, dataServiceName, jobDefinitionName, jobId, resourceGroupName, subscriptionId" /> | Cancels the given job. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="dataManagerName, dataServiceName, jobDefinitionName, jobId, resourceGroupName, subscriptionId" /> | Resumes the given job. |
