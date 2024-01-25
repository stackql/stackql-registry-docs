---
title: schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - schedules
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
<tr><td><b>Name</b></td><td><code>schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.lab_services.schedules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Schedule resource properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` |  | Returns the properties of a lab Schedule. |
| `list_by_lab` | `SELECT` |  | Returns a list of all schedules for a lab. |
| `create_or_update` | `INSERT` | `data__properties` | Operation to create or update a lab schedule. |
| `delete` | `DELETE` |  | Operation to delete a schedule resource. |
| `_list_by_lab` | `EXEC` |  | Returns a list of all schedules for a lab. |
| `update` | `EXEC` |  | Operation to update a lab schedule. |
