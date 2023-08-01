---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - data_box
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_box.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Id of the object. |
| `name` | `string` | Name of the object. |
| `sku` | `object` | The Sku. |
| `location` | `string` | The location of the resource. This will be one of the supported and registered Azure Regions (e.g. West US, East US, Southeast Asia, etc.). The region of a resource cannot be changed once it is created, but if an identical region is specified on update the request will succeed. |
| `tags` | `object` | The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). |
| `systemData` | `object` | Provides details about resource creation and update time |
| `type` | `string` | Type of the object. |
| `identity` | `object` | Msi identity details of the resource |
| `properties` | `object` | Job Properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Jobs_Get` | `SELECT` | `jobName, resourceGroupName, subscriptionId` | Gets information about the specified job. |
| `Jobs_List` | `SELECT` | `subscriptionId` | Lists all the jobs available under the subscription. |
| `Jobs_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the jobs available under the given resource group. |
| `Jobs_Create` | `INSERT` | `jobName, resourceGroupName, subscriptionId, data__properties` | Creates a new job with the specified parameters. Existing job cannot be updated with this API and should instead be updated with the Update job API. |
| `Jobs_Delete` | `DELETE` | `jobName, resourceGroupName, subscriptionId` | Deletes a job. |
| `Jobs_BookShipmentPickUp` | `EXEC` | `jobName, resourceGroupName, subscriptionId, data__endTime, data__shipmentLocation, data__startTime` | Book shipment pick up. |
| `Jobs_Cancel` | `EXEC` | `jobName, resourceGroupName, subscriptionId, data__reason` | CancelJob. |
| `Jobs_ListCredentials` | `EXEC` | `jobName, resourceGroupName, subscriptionId` | This method gets the unencrypted secrets related to the job. |
| `Jobs_MarkDevicesShipped` | `EXEC` | `jobName, resourceGroupName, subscriptionId, data__deliverToDcPackageDetails` | Request to mark devices for a given job as shipped |
| `Jobs_Update` | `EXEC` | `jobName, resourceGroupName, subscriptionId` | Updates the properties of an existing job. |
| `Mitigate` | `EXEC` | `jobName, resourceGroupName, subscriptionId, data__customerResolutionCode` | Request to mitigate for a given job |
