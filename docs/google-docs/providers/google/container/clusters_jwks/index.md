---
title: clusters_jwks
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_jwks
  - container
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
<tr><td><b>Name</b></td><td><code>clusters_jwks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.container.clusters_jwks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `cacheHeader` | `object` | RFC-2616: cache control support |
| `keys` | `array` | The public component of the keys used by the cluster to sign token requests. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_clusters_getJwks` | `SELECT` | `clustersId, locationsId, projectsId` |
