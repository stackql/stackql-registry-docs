---
title: network_fabrics_topology
hide_title: false
hide_table_of_contents: false
keywords:
  - network_fabrics_topology
  - managed_network_fabric
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
<tr><td><b>Name</b></td><td><code>network_fabrics_topology</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.network_fabrics_topology</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `configurationState` | `string` | Configuration state for the resource. |
| `error` | `object` | The error detail. |
| `url` | `string` | URL for the details of the response. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `networkFabricName, resourceGroupName, subscriptionId` |
