---
title: express_route_links
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_links
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
<tr><td><b>Name</b></td><td><code>express_route_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.express_route_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Name of child port resource that is unique among child port resources of the parent. |
| `properties` | `object` | Properties specific to ExpressRouteLink resources. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ExpressRouteLinks_Get` | `SELECT` | `expressRoutePortName, linkName, resourceGroupName, subscriptionId` | Retrieves the specified ExpressRouteLink resource. |
| `ExpressRouteLinks_List` | `SELECT` | `expressRoutePortName, resourceGroupName, subscriptionId` | Retrieve the ExpressRouteLink sub-resources of the specified ExpressRoutePort resource. |
