---
title: providers
hide_title: false
hide_table_of_contents: false
keywords:
  - providers
  - eventarc
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
<tr><td><b>Name</b></td><td><code>providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.eventarc.providers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. In `projects/&#123;project&#125;/locations/&#123;location&#125;/providers/&#123;provider_id&#125;` format. |
| `displayName` | `string` | Output only. Human friendly name for the Provider. For example "Cloud Storage". |
| `eventTypes` | `array` | Output only. Event types for this provider. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, providersId` | Get a single Provider. |
| `list` | `SELECT` | `locationsId, projectsId` | List providers. |
| `_list` | `EXEC` | `locationsId, projectsId` | List providers. |
