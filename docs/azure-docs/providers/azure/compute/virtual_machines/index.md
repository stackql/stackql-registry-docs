---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
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
<tr><td><b>Name</b></td><td><code>virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `etag` | `string` | Etag is property returned in Create/Update/Get response of the VM, so that customer can supply it in the header to ensure optimistic updates. |
| `extendedLocation` | `object` | The complex type of the extended location. |
| `identity` | `object` | Identity for the virtual machine. |
| `location` | `string` | Resource location |
| `managedBy` | `string` | ManagedBy is set to Virtual Machine Scale Set(VMSS) flex ARM resourceID, if the VM is part of the VMSS. This property is used by platform for internal resource group delete optimization. |
| `plan` | `object` | Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started -&gt;**. Enter any required information and then click **Save**. |
| `properties` | `object` | Describes the properties of a Virtual Machine. |
| `resources` | `array` | The virtual machine child extension resources. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
| `zones` | `array` | The virtual machine zones. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, vmName` | Retrieves information about the model view or the instance view of a virtual machine. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the virtual machines in the specified resource group. Use the nextLink property in the response to get the next page of virtual machines. |
| `list_by_location` | `SELECT` | `location, subscriptionId` | Gets all the virtual machines under the specified subscription for the specified location. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, vmName` | The operation to create or update a virtual machine. Please note some properties can be set only during virtual machine creation. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, vmName` | The operation to delete a virtual machine. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all of the virtual machines in the specified resource group. Use the nextLink property in the response to get the next page of virtual machines. |
| `_list_by_location` | `EXEC` | `location, subscriptionId` | Gets all the virtual machines under the specified subscription for the specified location. |
