---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - storage_import_export
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_import_export.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Specifies the resource identifier of the job. |
| `name` | `string` | Specifies the name of the job. |
| `identity` | `object` | Specifies the identity properties.  |
| `location` | `string` | Specifies the Azure location where the job is created. |
| `properties` | `object` | Specifies the job properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Specifies the tags that are assigned to the job. |
| `type` | `string` | Specifies the type of the job resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, jobName, resourceGroupName, subscriptionId` | Gets information about an existing job. |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Returns all active and completed jobs in a resource group. |
| `list_by_subscription` | `SELECT` | `api-version, subscriptionId` | Returns all active and completed jobs in a subscription. |
| `create` | `INSERT` | `api-version, jobName, resourceGroupName, subscriptionId` | Creates a new job or updates an existing job in the specified subscription. |
| `delete` | `DELETE` | `api-version, jobName, resourceGroupName, subscriptionId` | Deletes an existing job. Only jobs in the Creating or Completed states can be deleted. |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | Returns all active and completed jobs in a resource group. |
| `_list_by_subscription` | `EXEC` | `api-version, subscriptionId` | Returns all active and completed jobs in a subscription. |
| `update` | `EXEC` | `api-version, jobName, resourceGroupName, subscriptionId` | Updates specific properties of a job. You can call this operation to notify the Import/Export service that the hard drives comprising the import or export job have been shipped to the Microsoft data center. It can also be used to cancel an existing job. |
