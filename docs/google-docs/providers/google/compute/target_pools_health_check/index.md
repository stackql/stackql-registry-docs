---
title: target_pools_health_check
hide_title: false
hide_table_of_contents: false
keywords:
  - target_pools_health_check
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
<tr><td><b>Name</b></td><td><code>target_pools_health_check</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.target_pools_health_check</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `targetPools_addHealthCheck` | `INSERT` | `project, region, targetPool` | Adds health check URLs to a target pool. |
| `targetPools_removeHealthCheck` | `DELETE` | `project, region, targetPool` | Removes health check URL from a target pool. |
