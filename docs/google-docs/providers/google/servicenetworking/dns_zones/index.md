---
title: dns_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_zones
  - servicenetworking
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
<tr><td><b>Name</b></td><td><code>dns_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.servicenetworking.dns_zones</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `services_dnsZones_add` | `INSERT` | `servicesId` | Service producers can use this method to add private DNS zones in the shared producer host project and matching peering zones in the consumer project. |
| `services_dnsZones_remove` | `DELETE` | `servicesId` | Service producers can use this method to remove private DNS zones in the shared producer host project and matching peering zones in the consumer project. |
