---
title: available_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - available_locations
  - firebase
  - firebase    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/firebase/stackql-firebase-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>available_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>firebase.firebase.available_locations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `locations` | `array` | One page of results from a call to `ListAvailableLocations`. |
| `nextPageToken` | `string` | If the result list is too large to fit in a single response, then a token is returned. If the string is empty, then this response is the last page of results and all available locations have been listed. This token can be used in a subsequent call to `ListAvailableLocations` to find more locations. Page tokens are short-lived and should not be persisted. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_availableLocations_list` | `SELECT` | `projectsId` |
