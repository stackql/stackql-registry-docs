---
title: replication_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_jobs
  - recovery_services_site_recovery
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
<tr><td><b>Name</b></td><td><code>replication_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replication_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `location` | `string` | Resource Location |
| `properties` | `object` | Job custom data details. |
| `type` | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReplicationJobs_Get` | `SELECT` | `api-version, jobName, resourceGroupName, resourceName, subscriptionId` | Get the details of an Azure Site Recovery job. |
| `ReplicationJobs_List` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Gets the list of Azure Site Recovery Jobs for the vault. |
| `ReplicationJobs_Cancel` | `EXEC` | `api-version, jobName, resourceGroupName, resourceName, subscriptionId` | The operation to cancel an Azure Site Recovery job. |
| `ReplicationJobs_Export` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | The operation to export the details of the Azure Site Recovery jobs of the vault. |
| `ReplicationJobs_Restart` | `EXEC` | `api-version, jobName, resourceGroupName, resourceName, subscriptionId` | The operation to restart an Azure Site Recovery job. |
| `ReplicationJobs_Resume` | `EXEC` | `api-version, jobName, resourceGroupName, resourceName, subscriptionId` | The operation to resume an Azure Site Recovery job. |
