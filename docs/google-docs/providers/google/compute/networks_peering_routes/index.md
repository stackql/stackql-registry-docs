---
title: networks_peering_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - networks_peering_routes
  - compute
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>networks_peering_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.networks_peering_routes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextHopRegion` | `string` | The region of peering route next hop, only applies to dynamic routes. |
| `priority` | `integer` | The priority of the peering route. |
| `type` | `string` | The type of the peering route. |
| `destRange` | `string` | The destination range of the route. |
| `imported` | `boolean` | True if the peering route has been imported from a peer. The actual import happens if the field networkPeering.importCustomRoutes is true for this network, and networkPeering.exportCustomRoutes is true for the peer network, and the import does not result in a route conflict. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `networks_listPeeringRoutes` | `SELECT` | `network, project` |
