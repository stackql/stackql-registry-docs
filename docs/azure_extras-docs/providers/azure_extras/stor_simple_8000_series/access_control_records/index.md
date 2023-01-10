---
title: access_control_records
hide_title: false
hide_table_of_contents: false
keywords:
  - access_control_records
  - stor_simple_8000_series
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
<tr><td><b>Name</b></td><td><code>access_control_records</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.stor_simple_8000_series.access_control_records</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The name of the object. |
| `properties` | `object` | The properties of access control record. |
| `type` | `string` | The hierarchical type of the object. |
| `kind` | `string` | The Kind of the object. Currently only Series8000 is supported |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AccessControlRecords_Get` | `SELECT` | `accessControlRecordName, managerName, resourceGroupName, subscriptionId` | Returns the properties of the specified access control record name. |
| `AccessControlRecords_ListByManager` | `SELECT` | `managerName, resourceGroupName, subscriptionId` | Retrieves all the access control records in a manager. |
| `AccessControlRecords_CreateOrUpdate` | `INSERT` | `accessControlRecordName, managerName, resourceGroupName, subscriptionId, data__properties` | Creates or Updates an access control record. |
| `AccessControlRecords_Delete` | `DELETE` | `accessControlRecordName, managerName, resourceGroupName, subscriptionId` | Deletes the access control record. |
