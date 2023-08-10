---
title: xpn_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - xpn_resources
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
<tr><td><b>Name</b></td><td><code>xpn_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.xpn_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the service resource. In the case of projects, this field supports project id (e.g., my-project-123) and project number (e.g. 12345678). |
| `type` | `string` | The type of the service resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_xpn_resources` | `SELECT` | `project` |
| `_get_xpn_resources` | `EXEC` | `project` |
