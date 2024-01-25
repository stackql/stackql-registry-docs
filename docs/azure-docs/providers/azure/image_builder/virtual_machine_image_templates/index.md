---
title: virtual_machine_image_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_image_templates
  - image_builder
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
<tr><td><b>Id</b></td><td><code>azure.image_builder.virtual_machine_image_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity for the image template. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Describes the properties of an image template |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `imageTemplateName, resourceGroupName, subscriptionId` | Get information about a virtual machine image template |
| `list` | `SELECT` | `subscriptionId` | Gets information about the VM image templates associated with the subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets information about the VM image templates associated with the specified resource group. |
| `create_or_update` | `INSERT` | `imageTemplateName, resourceGroupName, subscriptionId, data__identity` | Create or update a virtual machine image template |
| `delete` | `DELETE` | `imageTemplateName, resourceGroupName, subscriptionId` | Delete a virtual machine image template |
| `_list` | `EXEC` | `subscriptionId` | Gets information about the VM image templates associated with the subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets information about the VM image templates associated with the specified resource group. |
| `cancel` | `EXEC` | `imageTemplateName, resourceGroupName, subscriptionId` | Cancel the long running image build based on the image template |
| `run` | `EXEC` | `imageTemplateName, resourceGroupName, subscriptionId` | Create artifacts from a existing image template |
| `update` | `EXEC` | `imageTemplateName, resourceGroupName, subscriptionId` | Update the tags for this Virtual Machine Image Template |
