---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - data_box
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
<tr><td><b>Id</b></td><td><code>azure.data_box.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Id of the object. |
| `name` | `string` | Name of the object. |
| `identity` | `object` | Msi identity details of the resource |
| `location` | `string` | The location of the resource. This will be one of the supported and registered Azure Regions (e.g. West US, East US, Southeast Asia, etc.). The region of a resource cannot be changed once it is created, but if an identical region is specified on update the request will succeed. |
| `properties` | `object` | Job Properties |
| `sku` | `object` | The Sku. |
| `systemData` | `object` | Provides details about resource creation and update time |
| `tags` | `object` | The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). |
| `type` | `string` | Type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobName, resourceGroupName, subscriptionId` | Gets information about the specified job. |
| `list` | `SELECT` | `subscriptionId` | Lists all the jobs available under the subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the jobs available under the given resource group. |
| `create` | `INSERT` | `jobName, resourceGroupName, subscriptionId, data__properties` | Creates a new job with the specified parameters. Existing job cannot be updated with this API and should instead be updated with the Update job API. |
| `delete` | `DELETE` | `jobName, resourceGroupName, subscriptionId` | Deletes a job. |
| `_list` | `EXEC` | `subscriptionId` | Lists all the jobs available under the subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the jobs available under the given resource group. |
| `book_shipment_pick_up` | `EXEC` | `jobName, resourceGroupName, subscriptionId, data__endTime, data__shipmentLocation, data__startTime` | Book shipment pick up. |
| `cancel` | `EXEC` | `jobName, resourceGroupName, subscriptionId, data__reason` | CancelJob. |
| `jobs` | `EXEC` | `jobName, resourceGroupName, subscriptionId` | Request to mitigate for a given job |
| `mark_devices_shipped` | `EXEC` | `jobName, resourceGroupName, subscriptionId, data__deliverToDcPackageDetails` | Request to mark devices for a given job as shipped |
| `update` | `EXEC` | `jobName, resourceGroupName, subscriptionId` | Updates the properties of an existing job. |
