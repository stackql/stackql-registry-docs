---
title: virtual_machine_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_templates
  - connected_vsphere
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
<tr><td><b>Name</b></td><td><code>virtual_machine_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.connected_vsphere.virtual_machine_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the Id. |
| `name` | `string` | Gets or sets the name. |
| `properties` | `object` | Defines the resource properties. |
| `location` | `string` | Gets or sets the location. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Gets or sets the Resource tags. |
| `extendedLocation` | `object` | The extended location. |
| `type` | `string` | Gets or sets the type of the resource. |
| `kind` | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachineTemplates_Get` | `SELECT` | `api-version, resourceGroupName, subscriptionId, virtualMachineTemplateName` | Implements virtual machine template GET method. |
| `VirtualMachineTemplates_List` | `SELECT` | `api-version, subscriptionId` | List of virtualMachineTemplates in a subscription. |
| `VirtualMachineTemplates_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List of virtualMachineTemplates in a resource group. |
| `VirtualMachineTemplates_Create` | `INSERT` | `api-version, resourceGroupName, subscriptionId, virtualMachineTemplateName, data__location, data__properties` | Create Or Update virtual machine template. |
| `VirtualMachineTemplates_Delete` | `DELETE` | `api-version, resourceGroupName, subscriptionId, virtualMachineTemplateName` | Implements virtual machine template DELETE method. |
| `VirtualMachineTemplates_Update` | `EXEC` | `api-version, resourceGroupName, subscriptionId, virtualMachineTemplateName` | API to update certain properties of the virtual machine template resource. |
