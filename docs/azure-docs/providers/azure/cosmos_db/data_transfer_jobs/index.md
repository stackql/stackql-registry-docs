---
title: data_transfer_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - data_transfer_jobs
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>data_transfer_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.data_transfer_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique resource identifier of the database account. |
| `name` | `string` | The name of the database account. |
| `properties` | `object` | The properties of a DataTransfer Job |
| `type` | `string` | The type of Azure resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DataTransferJobs_Get` | `SELECT` | `accountName, jobName, resourceGroupName, subscriptionId` | Get a Data Transfer Job. |
| `DataTransferJobs_ListByDatabaseAccount` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Get a list of Data Transfer jobs. |
| `DataTransferJobs_Create` | `INSERT` | `accountName, jobName, resourceGroupName, subscriptionId, data__properties` | Creates a Data Transfer Job. |
| `DataTransferJobs_Cancel` | `EXEC` | `accountName, jobName, resourceGroupName, subscriptionId` | Cancels a Data Transfer Job. |
| `DataTransferJobs_Pause` | `EXEC` | `accountName, jobName, resourceGroupName, subscriptionId` | Pause a Data Transfer Job. |
| `DataTransferJobs_Resume` | `EXEC` | `accountName, jobName, resourceGroupName, subscriptionId` | Resumes a Data Transfer Job. |
