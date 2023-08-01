---
title: devices_signed
hide_title: false
hide_table_of_contents: false
keywords:
  - devices_signed
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
<tr><td><b>Name</b></td><td><code>devices_signed</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.prod_tt_sasportal.devices_signed</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `customers_deployments_devices_create_signed` | `INSERT` | `customersId, deploymentsId` | Creates a signed device under a node or customer. |
| `customers_devices_create_signed` | `INSERT` | `customersId` | Creates a signed device under a node or customer. |
| `customers_nodes_devices_create_signed` | `INSERT` | `customersId, nodesId` | Creates a signed device under a node or customer. |
| `nodes_deployments_devices_create_signed` | `INSERT` | `deploymentsId, nodesId` | Creates a signed device under a node or customer. |
| `nodes_devices_create_signed` | `INSERT` | `nodesId` | Creates a signed device under a node or customer. |
| `nodes_nodes_devices_create_signed` | `INSERT` | `nodesId, nodesId1` | Creates a signed device under a node or customer. |
| `customers_devices_update_signed` | `EXEC` | `customersId, devicesId` | Updates a signed device. |
| `deployments_devices_update_signed` | `EXEC` | `deploymentsId, devicesId` | Updates a signed device. |
| `nodes_devices_update_signed` | `EXEC` | `devicesId, nodesId` | Updates a signed device. |
