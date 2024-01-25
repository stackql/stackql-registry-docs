---
title: virtual_machine_images
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_images
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
<tr><td><b>Name</b></td><td><code>virtual_machine_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machine_images</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the resource. |
| `extendedLocation` | `object` | The complex type of the extended location. |
| `location` | `string` | The supported Azure location of the resource. |
| `properties` | `object` | Describes the properties of a Virtual Machine Image. |
| `tags` | `object` | Specifies the tags that are assigned to the virtual machine. For more information about using tags, see [Using tags to organize your Azure resources](https://docs.microsoft.com/azure/azure-resource-manager/resource-group-using-tags.md). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `location, offer, publisherName, skus, subscriptionId, version` | Gets a virtual machine image. |
| `list` | `SELECT` | `location, offer, publisherName, skus, subscriptionId` | Gets a list of all virtual machine image versions for the specified location, publisher, offer, and SKU. |
| `list_by_edge_zone` | `SELECT` | `edgeZone, location, subscriptionId` | Gets a list of all virtual machine image versions for the specified edge zone |
| `_list_by_edge_zone` | `EXEC` | `edgeZone, location, subscriptionId` | Gets a list of all virtual machine image versions for the specified edge zone |
