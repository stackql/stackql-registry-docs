---
title: lab_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - lab_plans
  - lab_services
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
<tr><td><b>Name</b></td><td><code>lab_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.lab_services.lab_plans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Lab plan resource properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` |  | Retrieves the properties of a Lab Plan. |
| `list_by_resource_group` | `SELECT` |  | Returns a list of all lab plans for a subscription and resource group. |
| `list_by_subscription` | `SELECT` |  | Returns a list of all lab plans within a subscription |
| `create_or_update` | `INSERT` | `data__properties` | Operation to create or update a Lab Plan resource. |
| `delete` | `DELETE` |  | Operation to delete a Lab Plan resource. Deleting a lab plan does not delete labs associated with a lab plan, nor does it delete shared images added to a gallery via the lab plan permission container. |
| `_list_by_resource_group` | `EXEC` |  | Returns a list of all lab plans for a subscription and resource group. |
| `_list_by_subscription` | `EXEC` |  | Returns a list of all lab plans within a subscription |
| `save_image` | `EXEC` |  | Saves an image from a lab VM to the attached shared image gallery. |
| `update` | `EXEC` |  | Operation to update a Lab Plan resource. |
