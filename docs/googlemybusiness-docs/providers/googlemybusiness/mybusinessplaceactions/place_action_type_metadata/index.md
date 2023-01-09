---
title: place_action_type_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - place_action_type_metadata
  - mybusinessplaceactions
  - googlemybusiness    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googlemybusiness/stackql-googlemybusiness-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>place_action_type_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googlemybusiness.mybusinessplaceactions.place_action_type_metadata</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `placeActionTypeMetadata` | `array` | A collection of metadata for the available place action types. |
| `nextPageToken` | `string` | If the number of action types exceeded the requested page size, this field will be populated with a token to fetch the next page on a subsequent call to `placeActionTypeMetadata.list`. If there are no more results, this field will not be present in the response. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `placeActionTypeMetadata_list` | `SELECT` |  |
