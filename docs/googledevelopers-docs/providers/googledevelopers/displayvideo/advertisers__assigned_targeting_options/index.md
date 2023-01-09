---
title: advertisers__assigned_targeting_options
hide_title: false
hide_table_of_contents: false
keywords:
  - advertisers__assigned_targeting_options
  - displayvideo
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>advertisers__assigned_targeting_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.advertisers__assigned_targeting_options</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `assignedTargetingOptions` | `array` | The list of assigned targeting options. This list will be absent if empty. |
| `nextPageToken` | `string` | A token identifying the next page of results. This value should be specified as the pageToken in a subsequent BulkListAdvertiserAssignedTargetingOptionsRequest to fetch the next page of results. This token will be absent if there are no more assigned_targeting_options to return. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `advertisers_listAssignedTargetingOptions` | `SELECT` | `advertisersId` |
