---
title: os_images
hide_title: false
hide_table_of_contents: false
keywords:
  - os_images
  - baremetalsolution
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
<tr><td><b>Name</b></td><td><code>os_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.baremetalsolution.os_images</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. OS Image's unique name. |
| `description` | `string` | OS Image description. |
| `applicableInstanceTypes` | `array` | Instance types this image is applicable to. [Available types](https://cloud.google.com/bare-metal/docs/bms-planning#server_configurations) |
| `code` | `string` | OS Image code. |
| `supportedNetworkTemplates` | `array` | Network templates that can be used with this OS Image. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `locationsId, projectsId` |
| `_list` | `EXEC` | `locationsId, projectsId` |
