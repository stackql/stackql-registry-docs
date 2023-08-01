---
title: extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions
  - visual_studio
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
<tr><td><b>Name</b></td><td><code>extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.visual_studio.extensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier of the resource. |
| `name` | `string` | Resource name. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `location` | `string` | Resource location. |
| `plan` | `object` | Plan data for an extension resource. |
| `properties` | `object` | Resource properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Extensions_Get` | `SELECT` | `accountResourceName, extensionResourceName, resourceGroupName, subscriptionId` | Gets the details of an extension associated with a Visual Studio Team Services account resource. |
| `Extensions_ListByAccount` | `SELECT` | `accountResourceName, resourceGroupName, subscriptionId` | Gets the details of the extension resources created within the resource group. |
| `Extensions_Create` | `INSERT` | `accountResourceName, extensionResourceName, resourceGroupName, subscriptionId` | Registers the extension with a Visual Studio Team Services account. |
| `Extensions_Delete` | `DELETE` | `accountResourceName, extensionResourceName, resourceGroupName, subscriptionId` | Removes an extension resource registration for a Visual Studio Team Services account. |
| `Extensions_Update` | `EXEC` | `accountResourceName, extensionResourceName, resourceGroupName, subscriptionId` | Updates an existing extension registration for the Visual Studio Team Services account. |
