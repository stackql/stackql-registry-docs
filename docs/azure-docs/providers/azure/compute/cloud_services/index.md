---
title: cloud_services
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_services
  - compute
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
<tr><td><b>Name</b></td><td><code>cloud_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.cloud_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Cloud service properties |
| `systemData` | `object` | The system meta data relating to this resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CloudServices_Get` | `SELECT` | `cloudServiceName, resourceGroupName, subscriptionId` | Display information about a cloud service. |
| `CloudServices_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of all cloud services under a resource group. Use nextLink property in the response to get the next page of Cloud Services. Do this till nextLink is null to fetch all the Cloud Services. |
| `CloudServices_ListAll` | `SELECT` | `subscriptionId` | Gets a list of all cloud services in the subscription, regardless of the associated resource group. Use nextLink property in the response to get the next page of Cloud Services. Do this till nextLink is null to fetch all the Cloud Services. |
| `CloudServices_CreateOrUpdate` | `INSERT` | `cloudServiceName, resourceGroupName, subscriptionId, data__location` | Create or update a cloud service. Please note some properties can be set only during cloud service creation. |
| `CloudServices_Delete` | `DELETE` | `cloudServiceName, resourceGroupName, subscriptionId` | Deletes a cloud service. |
| `CloudServices_DeleteInstances` | `EXEC` | `cloudServiceName, resourceGroupName, subscriptionId, data__roleInstances` | Deletes role instances in a cloud service. |
| `CloudServices_GetInstanceView` | `EXEC` | `cloudServiceName, resourceGroupName, subscriptionId` | Gets the status of a cloud service. |
| `CloudServices_PowerOff` | `EXEC` | `cloudServiceName, resourceGroupName, subscriptionId` | Power off the cloud service. Note that resources are still attached and you are getting charged for the resources. |
| `CloudServices_Rebuild` | `EXEC` | `cloudServiceName, resourceGroupName, subscriptionId, data__roleInstances` | Rebuild Role Instances reinstalls the operating system on instances of web roles or worker roles and initializes the storage resources that are used by them. If you do not want to initialize storage resources, you can use Reimage Role Instances. |
| `CloudServices_Reimage` | `EXEC` | `cloudServiceName, resourceGroupName, subscriptionId, data__roleInstances` | Reimage asynchronous operation reinstalls the operating system on instances of web roles or worker roles. |
| `CloudServices_Restart` | `EXEC` | `cloudServiceName, resourceGroupName, subscriptionId, data__roleInstances` | Restarts one or more role instances in a cloud service. |
| `CloudServices_Start` | `EXEC` | `cloudServiceName, resourceGroupName, subscriptionId` | Starts the cloud service. |
| `CloudServices_Update` | `EXEC` | `cloudServiceName, resourceGroupName, subscriptionId` | Update a cloud service. |
