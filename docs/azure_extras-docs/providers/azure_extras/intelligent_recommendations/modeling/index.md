---
title: modeling
hide_title: false
hide_table_of_contents: false
keywords:
  - modeling
  - intelligent_recommendations
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
<tr><td><b>Id</b></td><td><code>azure_extras.intelligent_recommendations.modeling</code></td></tr>
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
| `get` | `SELECT` | `accountName, modelingName, resourceGroupName, subscriptionId` | Returns Modeling resources for a given name. |
| `list_by_account_resource` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Returns list of Modeling resources for a given Account name. |
| `create_or_update` | `INSERT` | `accountName, modelingName, resourceGroupName, subscriptionId` | Creates or updates Modeling resource. |
| `delete` | `DELETE` | `accountName, modelingName, resourceGroupName, subscriptionId` | Deletes Modeling resources of a given name. |
| `_list_by_account_resource` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Returns list of Modeling resources for a given Account name. |
| `update` | `EXEC` | `accountName, modelingName, resourceGroupName, subscriptionId` | Updates Modeling resource details. |
