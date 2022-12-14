---
title: virtual_machine_image_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_image_templates
  - virtual_machine_images
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
<tr><td><b>Name</b></td><td><code>virtual_machine_image_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.virtual_machine_images.virtual_machine_image_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Describes the properties of an image template |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Identity for the image template. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachineImageTemplates_Get` | `SELECT` | `imageTemplateName, resourceGroupName, subscriptionId` | Get information about a virtual machine image template |
| `VirtualMachineImageTemplates_List` | `SELECT` | `subscriptionId` | Gets information about the VM image templates associated with the subscription. |
| `VirtualMachineImageTemplates_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets information about the VM image templates associated with the specified resource group. |
| `VirtualMachineImageTemplates_CreateOrUpdate` | `INSERT` | `imageTemplateName, resourceGroupName, subscriptionId, data__identity` | Create or update a virtual machine image template |
| `VirtualMachineImageTemplates_Delete` | `DELETE` | `imageTemplateName, resourceGroupName, subscriptionId` | Delete a virtual machine image template |
| `VirtualMachineImageTemplates_Cancel` | `EXEC` | `imageTemplateName, resourceGroupName, subscriptionId` | Cancel the long running image build based on the image template |
| `VirtualMachineImageTemplates_GetRunOutput` | `EXEC` | `imageTemplateName, resourceGroupName, runOutputName, subscriptionId` | Get the specified run output for the specified image template resource |
| `VirtualMachineImageTemplates_ListRunOutputs` | `EXEC` | `imageTemplateName, resourceGroupName, subscriptionId` | List all run outputs for the specified Image Template resource |
| `VirtualMachineImageTemplates_Run` | `EXEC` | `imageTemplateName, resourceGroupName, subscriptionId` | Create artifacts from a existing image template |
| `VirtualMachineImageTemplates_Update` | `EXEC` | `imageTemplateName, resourceGroupName, subscriptionId` | Update the tags for this Virtual Machine Image Template |
