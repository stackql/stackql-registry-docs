---
title: clusters_api_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_api_endpoints
  - lke
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_api_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.lke.clusters_api_endpoints</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getLKEClusterAPIEndpoints` | `SELECT` | `clusterId` |
| `_getLKEClusterAPIEndpoints` | `EXEC` | `clusterId` |
