---
title: cloud_service_role_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_service_role_instances
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
<tr><td><b>Name</b></td><td><code>cloud_service_role_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.cloud_service_role_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name. |
| `location` | `string` | Resource Location. |
| `properties` | `object` | Role instance properties. |
| `sku` | `object` | The role instance SKU. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource Type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `cloudServiceName, resourceGroupName, roleInstanceName, subscriptionId` | Gets a role instance from a cloud service. |
| `list` | `SELECT` | `cloudServiceName, resourceGroupName, subscriptionId` | Gets the list of all role instances in a cloud service. Use nextLink property in the response to get the next page of role instances. Do this till nextLink is null to fetch all the role instances. |
| `delete` | `DELETE` | `cloudServiceName, resourceGroupName, roleInstanceName, subscriptionId` | Deletes a role instance from a cloud service. |
| `_list` | `EXEC` | `cloudServiceName, resourceGroupName, subscriptionId` | Gets the list of all role instances in a cloud service. Use nextLink property in the response to get the next page of role instances. Do this till nextLink is null to fetch all the role instances. |
| `rebuild` | `EXEC` | `cloudServiceName, resourceGroupName, roleInstanceName, subscriptionId` | The Rebuild Role Instance asynchronous operation reinstalls the operating system on instances of web roles or worker roles and initializes the storage resources that are used by them. If you do not want to initialize storage resources, you can use Reimage Role Instance. |
| `reimage` | `EXEC` | `cloudServiceName, resourceGroupName, roleInstanceName, subscriptionId` | The Reimage Role Instance asynchronous operation reinstalls the operating system on instances of web roles or worker roles. |
| `restart` | `EXEC` | `cloudServiceName, resourceGroupName, roleInstanceName, subscriptionId` | The Reboot Role Instance asynchronous operation requests a reboot of a role instance in the cloud service. |
