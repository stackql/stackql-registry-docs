---
title: backend_services__health
hide_title: false
hide_table_of_contents: false
keywords:
  - backend_services__health
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
<tr><td><b>Name</b></td><td><code>backend_services__health</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.backend_services__health</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `healthStatus` | `array` | Health state of the backend instances or endpoints in requested instance or network endpoint group, determined based on configured health checks. |
| `kind` | `string` | [Output Only] Type of resource. Always compute#backendServiceGroupHealth for the health of backend services. |
| `annotations` | `object` | Metadata defined as annotations on the network endpoint group. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `backendServices_getHealth` | `SELECT` | `backendService, project` |
