---
title: modeling
hide_title: false
hide_table_of_contents: false
keywords:
  - modeling
  - recommendations_service
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
<tr><td><b>Name</b></td><td><code>modeling</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.recommendations_service.modeling</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Modeling resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Modeling_Get` | `SELECT` | `accountName, modelingName, resourceGroupName, subscriptionId` | Returns Modeling resources for a given name. |
| `Modeling_ListByAccountResource` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Returns list of Modeling resources for a given Account name. |
| `Modeling_CreateOrUpdate` | `INSERT` | `accountName, modelingName, resourceGroupName, subscriptionId` | Creates or updates Modeling resource. |
| `Modeling_Delete` | `DELETE` | `accountName, modelingName, resourceGroupName, subscriptionId` | Deletes Modeling resources of a given name. |
| `Modeling_Update` | `EXEC` | `accountName, modelingName, resourceGroupName, subscriptionId` | Updates Modeling resource details. |
