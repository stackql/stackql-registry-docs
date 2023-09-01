---
title: routers_nat_mapping_info
hide_title: false
hide_table_of_contents: false
keywords:
  - routers_nat_mapping_info
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
<tr><td><b>Name</b></td><td><code>routers_nat_mapping_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.routers_nat_mapping_info</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `interfaceNatMappings` | `array` |  |
| `instanceName` | `string` | Name of the VM instance which the endpoint belongs to |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_nat_mapping_info` | `SELECT` | `project, region, router` |
| `_get_nat_mapping_info` | `EXEC` | `project, region, router` |
