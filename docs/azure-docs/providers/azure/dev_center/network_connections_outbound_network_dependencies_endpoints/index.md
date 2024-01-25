---
title: network_connections_outbound_network_dependencies_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - network_connections_outbound_network_dependencies_endpoints
  - dev_center
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
<tr><td><b>Name</b></td><td><code>network_connections_outbound_network_dependencies_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dev_center.network_connections_outbound_network_dependencies_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `category` | `string` | The type of service that the agent connects to. |
| `endpoints` | `array` | The endpoints for this service for which the agent requires outbound access. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |
| `_list` | `EXEC` |  |
