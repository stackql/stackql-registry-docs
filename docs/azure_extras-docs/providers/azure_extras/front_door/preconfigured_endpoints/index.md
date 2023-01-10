---
title: preconfigured_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - preconfigured_endpoints
  - front_door
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
<tr><td><b>Name</b></td><td><code>preconfigured_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.front_door.preconfigured_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | Defines the properties of a preconfigured endpoint |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `PreconfiguredEndpoints_List` | `SELECT` | `profileName, resourceGroupName, subscriptionId` |
