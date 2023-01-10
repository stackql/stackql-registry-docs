---
title: labs
hide_title: false
hide_table_of_contents: false
keywords:
  - labs
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
<tr><td><b>Name</b></td><td><code>labs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.lab_services.labs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of a lab resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Labs_Get` | `SELECT` |  | Returns the properties of a lab resource. |
| `Labs_ListByResourceGroup` | `SELECT` |  | Returns a list of all labs in a resource group. |
| `Labs_ListBySubscription` | `SELECT` |  | Returns a list of all labs for a subscription. |
| `Labs_CreateOrUpdate` | `INSERT` | `data__properties` | Operation to create or update a lab resource. |
| `Labs_Delete` | `DELETE` |  | Operation to delete a lab resource. |
| `Labs_Publish` | `EXEC` |  | Publish or re-publish a lab. This will create or update all lab resources, such as virtual machines. |
| `Labs_SyncGroup` | `EXEC` |  | Action used to manually kick off an AAD group sync job. |
| `Labs_Update` | `EXEC` |  | Operation to update a lab resource. |
