---
title: customer_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_nodes
  - sasportal
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
<tr><td><b>Id</b></td><td><code>google.sasportal.customer_nodes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name. |
| `displayName` | `string` | The node's display name. |
| `sasUserIds` | `array` | User ids used by the devices belonging to this node. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `customers_nodes_list` | `SELECT` | `customersId` | Lists nodes. |
| `customers_nodes_nodes_list` | `SELECT` | `customersId, nodesId` | Lists nodes. |
| `customers_nodes_create` | `INSERT` | `customersId` | Creates a new node. |
| `customers_nodes_nodes_create` | `INSERT` | `customersId, nodesId` | Creates a new node. |
| `customers_nodes_delete` | `DELETE` | `customersId, nodesId` | Deletes a node. |
| `_customers_nodes_list` | `EXEC` | `customersId` | Lists nodes. |
| `_customers_nodes_nodes_list` | `EXEC` | `customersId, nodesId` | Lists nodes. |
