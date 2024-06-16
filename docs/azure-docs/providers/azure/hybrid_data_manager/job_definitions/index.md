---
title: job_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_definitions
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
<tr><td><b>Name</b></td><td><code>job_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_data_manager.job_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the object. |
| <CopyableCode code="name" /> | `string` | Name of the object. |
| <CopyableCode code="properties" /> | `object` | Job Definition |
| <CopyableCode code="type" /> | `string` | Type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataManagerName, dataServiceName, jobDefinitionName, resourceGroupName, subscriptionId" /> | This method gets job definition object by name. |
| <CopyableCode code="list_by_data_manager" /> | `SELECT` | <CopyableCode code="dataManagerName, resourceGroupName, subscriptionId" /> | This method gets all the job definitions of the given data manager resource. |
| <CopyableCode code="list_by_data_service" /> | `SELECT` | <CopyableCode code="dataManagerName, dataServiceName, resourceGroupName, subscriptionId" /> | This method gets all the job definitions of the given data service name. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataManagerName, dataServiceName, jobDefinitionName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a job definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataManagerName, dataServiceName, jobDefinitionName, resourceGroupName, subscriptionId" /> | This method deletes the given job definition. |
| <CopyableCode code="run" /> | `EXEC` | <CopyableCode code="dataManagerName, dataServiceName, jobDefinitionName, resourceGroupName, subscriptionId" /> | This method runs a job instance of the given job definition. |
