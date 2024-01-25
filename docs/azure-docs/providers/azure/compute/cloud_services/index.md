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
| `location` | `string` | Resource location. |
| `properties` | `object` | Cloud service properties |
| `systemData` | `object` | The system meta data relating to this resource. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `zones` | `array` | List of logical availability zone of the resource. List should contain only 1 zone where cloud service should be provisioned. This field is optional. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `cloudServiceName, resourceGroupName, subscriptionId` | Display information about a cloud service. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of all cloud services under a resource group. Use nextLink property in the response to get the next page of Cloud Services. Do this till nextLink is null to fetch all the Cloud Services. |
| `create_or_update` | `INSERT` | `cloudServiceName, resourceGroupName, subscriptionId, data__location` | Create or update a cloud service. Please note some properties can be set only during cloud service creation. |
| `delete` | `DELETE` | `cloudServiceName, resourceGroupName, subscriptionId` | Deletes a cloud service. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Gets a list of all cloud services under a resource group. Use nextLink property in the response to get the next page of Cloud Services. Do this till nextLink is null to fetch all the Cloud Services. |
| `power_off` | `EXEC` | `cloudServiceName, resourceGroupName, subscriptionId` | Power off the cloud service. Note that resources are still attached and you are getting charged for the resources. |
| `rebuild` | `EXEC` | `cloudServiceName, resourceGroupName, subscriptionId, data__roleInstances` | Rebuild Role Instances reinstalls the operating system on instances of web roles or worker roles and initializes the storage resources that are used by them. If you do not want to initialize storage resources, you can use Reimage Role Instances. |
| `reimage` | `EXEC` | `cloudServiceName, resourceGroupName, subscriptionId, data__roleInstances` | Reimage asynchronous operation reinstalls the operating system on instances of web roles or worker roles. |
| `restart` | `EXEC` | `cloudServiceName, resourceGroupName, subscriptionId, data__roleInstances` | Restarts one or more role instances in a cloud service. |
| `start` | `EXEC` | `cloudServiceName, resourceGroupName, subscriptionId` | Starts the cloud service. |
| `update` | `EXEC` | `cloudServiceName, resourceGroupName, subscriptionId` | Update a cloud service. |
