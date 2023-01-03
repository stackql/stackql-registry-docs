---
title: states
hide_title: false
hide_table_of_contents: false
keywords:
  - states
  - cloudiot
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>states</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudiot.states</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `binaryData` | `string` | The device state data. |
| `updateTime` | `string` | [Output only] The time at which this state version was updated in Cloud IoT Core. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_registries_devices_states_list` | `SELECT` | `devicesId, locationsId, projectsId, registriesId` |
