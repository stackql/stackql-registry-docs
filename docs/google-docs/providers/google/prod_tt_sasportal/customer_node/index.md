---
title: customer_node
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_node
  - prod_tt_sasportal
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customer_node</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.prod_tt_sasportal.customer_node</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name. |
| `sasUserIds` | `array` | User ids used by the devices belonging to this node. |
| `displayName` | `string` | The node's display name. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `customers_nodes_get` | `SELECT` | `customersId, nodesId` |
