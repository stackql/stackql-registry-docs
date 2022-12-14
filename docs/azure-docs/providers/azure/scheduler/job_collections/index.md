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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.scheduler.job_collections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets the job collection resource identifier. |
| `name` | `string` | Gets or sets the job collection resource name. |
| `location` | `string` | Gets or sets the storage account location. |
| `properties` | `object` |  |
| `tags` | `object` | Gets or sets the tags. |
| `type` | `string` | Gets the job collection resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `JobCollections_Get` | `SELECT` | `api-version, jobCollectionName, resourceGroupName, subscriptionId` | Gets a job collection. |
| `JobCollections_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Gets all job collections under specified resource group. |
| `JobCollections_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | Gets all job collections under specified subscription. |
| `JobCollections_CreateOrUpdate` | `INSERT` | `api-version, jobCollectionName, resourceGroupName, subscriptionId` | Provisions a new job collection or updates an existing job collection. |
| `JobCollections_Delete` | `DELETE` | `api-version, jobCollectionName, resourceGroupName, subscriptionId` | Deletes a job collection. |
| `JobCollections_Disable` | `EXEC` | `api-version, jobCollectionName, resourceGroupName, subscriptionId` | Disables all of the jobs in the job collection. |
| `JobCollections_Enable` | `EXEC` | `api-version, jobCollectionName, resourceGroupName, subscriptionId` | Enables all of the jobs in the job collection. |
| `JobCollections_Patch` | `EXEC` | `api-version, jobCollectionName, resourceGroupName, subscriptionId` | Patches an existing job collection. |
