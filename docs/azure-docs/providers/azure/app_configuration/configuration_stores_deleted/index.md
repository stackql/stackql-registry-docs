---
title: configuration_stores_deleted
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_stores_deleted
  - app_configuration
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
<tr><td><b>Name</b></td><td><code>configuration_stores_deleted</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_configuration.configuration_stores_deleted</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID for the deleted configuration store. |
| `name` | `string` | The name of the configuration store. |
| `properties` | `object` | Properties of the deleted configuration store. |
| `type` | `string` | The resource type of the configuration store. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `configStoreName, location, subscriptionId` | Gets a deleted Azure app configuration store. |
| `list` | `SELECT` | `subscriptionId` | Gets information about the deleted configuration stores in a subscription. |
| `_list` | `EXEC` | `subscriptionId` | Gets information about the deleted configuration stores in a subscription. |
