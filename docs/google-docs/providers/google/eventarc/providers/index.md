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
| `providers` | `array` | The requested providers, up to the number specified in `page_size`. |
| `unreachable` | `array` | Unreachable resources, if any. |
| `nextPageToken` | `string` | A page token that can be sent to `ListProviders` to request the next page. If this is empty, then there are no more pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, providersId` | Get a single Provider. |
| `list` | `SELECT` | `locationsId, projectsId` | List providers. |
