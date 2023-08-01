---
title: experiments
hide_title: false
hide_table_of_contents: false
keywords:
  - experiments
  - chaos
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>experiments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.chaos.experiments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Model that represents the Experiment properties model. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | The managed identity of a resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Experiments_Get` | `SELECT` | `api-version, experimentName, resourceGroupName, subscriptionId` | Get a Experiment resource. |
| `Experiments_List` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Get a list of Experiment resources in a resource group. |
| `Experiments_ListAll` | `SELECT` | `api-version, subscriptionId` | Get a list of Experiment resources in a subscription. |
| `Experiments_CreateOrUpdate` | `INSERT` | `api-version, experimentName, resourceGroupName, subscriptionId, data__properties` | Create or update a Experiment resource. |
| `Experiments_Delete` | `DELETE` | `api-version, experimentName, resourceGroupName, subscriptionId` | Delete a Experiment resource. |
| `Experiments_Cancel` | `EXEC` | `api-version, experimentName, resourceGroupName, subscriptionId` | Cancel a running Experiment resource. |
| `Experiments_GetExecutionDetails` | `EXEC` | `api-version, executionDetailsId, experimentName, resourceGroupName, subscriptionId` | Get an execution detail of a Experiment resource. |
| `Experiments_GetStatus` | `EXEC` | `api-version, experimentName, resourceGroupName, statusId, subscriptionId` | Get a status of a Experiment resource. |
| `Experiments_ListAllStatuses` | `EXEC` | `api-version, experimentName, resourceGroupName, subscriptionId` | Get a list of statuses of a Experiment resource. |
| `Experiments_ListExecutionDetails` | `EXEC` | `api-version, experimentName, resourceGroupName, subscriptionId` | Get a list of execution details of a Experiment resource. |
| `Experiments_Start` | `EXEC` | `api-version, experimentName, resourceGroupName, subscriptionId` | Start a Experiment resource. |
