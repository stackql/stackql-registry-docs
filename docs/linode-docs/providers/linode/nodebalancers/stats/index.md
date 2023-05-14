---
title: stats
hide_title: false
hide_table_of_contents: false
keywords:
  - stats
  - nodebalancers
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
<tr><td><b>Name</b></td><td><code>stats</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.nodebalancers.stats</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `connections` | `array` | An array of key/value pairs representing unix timestamp and reading for connections to this NodeBalancer.<br /> |
| `traffic` | `object` | Traffic statistics for this NodeBalancer.<br /> |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_nodebalancers__nodeBalancerId_stats` | `SELECT` | `nodeBalancerId` |
| `_get_nodebalancers__nodeBalancerId_stats` | `EXEC` | `nodeBalancerId` |
