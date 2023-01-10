---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - lab_services
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.lab_services.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `properties` | `object` | User resource properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Users_Get` | `SELECT` |  | Returns the properties of a lab user. |
| `Users_ListByLab` | `SELECT` |  | Returns a list of all users for a lab. |
| `Users_CreateOrUpdate` | `INSERT` | `data__properties` | Operation to create or update a lab user. |
| `Users_Delete` | `DELETE` |  | Operation to delete a user resource. |
| `Users_Invite` | `EXEC` |  | Operation to invite a user to a lab. |
| `Users_Update` | `EXEC` |  | Operation to update a lab user. |
