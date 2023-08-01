---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - ml
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
<tr><td><b>Name</b></td><td><code>locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.ml.locations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Optional. Pass this token as the `page_token` field of the request for a subsequent call. |
| `locations` | `array` | Locations where at least one type of CMLE capability is available. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_get` | `SELECT` | `locationsId, projectsId` | Get the complete list of CMLE capabilities in a location, along with their location-specific properties. |
| `projects_locations_list` | `SELECT` | `projectsId` | List all locations that provides at least one type of CMLE capability. |
