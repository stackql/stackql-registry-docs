---
title: hubs_spokes
hide_title: false
hide_table_of_contents: false
keywords:
  - hubs_spokes
  - networkconnectivity
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
<tr><td><b>Name</b></td><td><code>hubs_spokes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkconnectivity.hubs_spokes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The token for the next page of the response. To see more results, use this value as the page_token for your next request. If this value is empty, there are no more results. |
| `spokes` | `array` | The requested spokes. The spoke fields can be partially populated based on the `view` field in the request message. |
| `unreachable` | `array` | Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_spokes` | `SELECT` | `hubsId, projectsId` |
