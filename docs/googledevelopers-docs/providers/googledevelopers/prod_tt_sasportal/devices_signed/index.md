---
title: devices_signed
hide_title: false
hide_table_of_contents: false
keywords:
  - devices_signed
  - prod_tt_sasportal
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices_signed</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.prod_tt_sasportal.devices_signed</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `customers_deployments_devices_createSigned` | `INSERT` | `customersId, deploymentsId` |
| `customers_devices_createSigned` | `INSERT` | `customersId` |
| `customers_nodes_devices_createSigned` | `INSERT` | `customersId, nodesId` |
| `nodes_deployments_devices_createSigned` | `INSERT` | `deploymentsId, nodesId` |
| `nodes_devices_createSigned` | `INSERT` | `nodesId` |
| `nodes_nodes_devices_createSigned` | `INSERT` | `nodesId, nodesId1` |
