---
title: global_network_endpoint_groups__network_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - global_network_endpoint_groups__network_endpoints
  - compute
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
<tr><td><b>Name</b></td><td><code>global_network_endpoint_groups__network_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.global_network_endpoint_groups__network_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `healths` | `array` | [Output only] The health status of network endpoint; |
| `networkEndpoint` | `object` | The network endpoint. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `globalNetworkEndpointGroups_listNetworkEndpoints` | `SELECT` | `networkEndpointGroup, project` |
