---
title: accelerator_types
hide_title: false
hide_table_of_contents: false
keywords:
  - accelerator_types
  - tpu
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
<tr><td><b>Name</b></td><td><code>accelerator_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.tpu.accelerator_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name. |
| `type` | `string` | The accelerator type. |
| `acceleratorConfigs` | `array` | The accelerator config. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `acceleratorTypesId, locationsId, projectsId` | Gets AcceleratorType. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists accelerator types supported by this API. |
