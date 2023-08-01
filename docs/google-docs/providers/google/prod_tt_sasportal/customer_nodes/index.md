---
title: customer_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_nodes
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
<tr><td><b>Name</b></td><td><code>customer_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.prod_tt_sasportal.customer_nodes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A pagination token returned from a previous call to ListNodes that indicates from where listing should continue. If the field is missing or empty, it means there is no more nodes. |
| `nodes` | `array` | The nodes that match the request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `customers_nodes_list` | `SELECT` | `customersId` | Lists nodes. |
| `customers_nodes_nodes_list` | `SELECT` | `customersId, nodesId` | Lists nodes. |
| `customers_nodes_create` | `INSERT` | `customersId` | Creates a new node. |
| `customers_nodes_nodes_create` | `INSERT` | `customersId, nodesId` | Creates a new node. |
| `customers_nodes_delete` | `DELETE` | `customersId, nodesId` | Deletes a node. |
