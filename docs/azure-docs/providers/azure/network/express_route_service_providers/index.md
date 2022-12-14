---
title: express_route_service_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_service_providers
  - network
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
<tr><td><b>Name</b></td><td><code>express_route_service_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.express_route_service_providers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | Properties of ExpressRouteServiceProvider. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ExpressRouteServiceProviders_List` | `SELECT` | `subscriptionId` |
