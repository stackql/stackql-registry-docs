---
title: job_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - job_collections
  - scheduler
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
<tr><td><b>Name</b></td><td><code>job_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.scheduler.job_collections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets the job collection resource identifier. |
| <CopyableCode code="name" /> | `string` | Gets or sets the job collection resource name. |
| <CopyableCode code="location" /> | `string` | Gets or sets the storage account location. |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Gets or sets the tags. |
| <CopyableCode code="type" /> | `string` | Gets the job collection resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, jobCollectionName, resourceGroupName, subscriptionId" /> | Gets a job collection. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Gets all job collections under specified resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | Gets all job collections under specified subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, jobCollectionName, resourceGroupName, subscriptionId" /> | Provisions a new job collection or updates an existing job collection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, jobCollectionName, resourceGroupName, subscriptionId" /> | Deletes a job collection. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Gets all job collections under specified resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> | Gets all job collections under specified subscription. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="api-version, jobCollectionName, resourceGroupName, subscriptionId" /> | Disables all of the jobs in the job collection. |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="api-version, jobCollectionName, resourceGroupName, subscriptionId" /> | Enables all of the jobs in the job collection. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="api-version, jobCollectionName, resourceGroupName, subscriptionId" /> | Patches an existing job collection. |
