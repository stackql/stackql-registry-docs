---
title: routers_router_status
hide_title: false
hide_table_of_contents: false
keywords:
  - routers_router_status
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
<tr><td><b>Name</b></td><td><code>routers_router_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.routers_router_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Type of resource. |
| `result` | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `routers_getRouterStatus` | `SELECT` | `project, region, router` |
