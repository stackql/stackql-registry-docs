---
title: urlchannels
hide_title: false
hide_table_of_contents: false
keywords:
  - urlchannels
  - adsensehost
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>urlchannels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adsensehost.urlchannels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier of this URL channel. This should be considered an opaque identifier; it is not safe to rely on it being in any particular format. |
| `kind` | `string` | Kind of resource this is, in this case adsensehost#urlChannel. |
| `urlPattern` | `string` | URL Pattern of this URL channel. Does not include "http://" or "https://". Example: www.example.com/home |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `adClientId` | List all host URL channels in the host AdSense account. |
| `insert` | `INSERT` | `adClientId` | Add a new URL channel to the host AdSense account. |
| `delete` | `DELETE` | `adClientId, urlChannelId` | Delete a URL channel from the host AdSense account. |
