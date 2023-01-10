---
title: schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - schedules
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
<tr><td><b>Name</b></td><td><code>schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.lab_services.schedules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Schedule resource properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Schedules_Get` | `SELECT` |  | Returns the properties of a lab Schedule. |
| `Schedules_ListByLab` | `SELECT` |  | Returns a list of all schedules for a lab. |
| `Schedules_CreateOrUpdate` | `INSERT` | `data__properties` | Operation to create or update a lab schedule. |
| `Schedules_Delete` | `DELETE` |  | Operation to delete a schedule resource. |
| `Schedules_Update` | `EXEC` |  | Operation to update a lab schedule. |
