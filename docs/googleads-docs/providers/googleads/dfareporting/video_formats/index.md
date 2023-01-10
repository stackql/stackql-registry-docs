---
title: video_formats
hide_title: false
hide_table_of_contents: false
keywords:
  - video_formats
  - dfareporting
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
<tr><td><b>Name</b></td><td><code>video_formats</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.video_formats</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | ID of the video format. |
| `targetBitRate` | `integer` | The target bit rate of this video format. |
| `fileType` | `string` | File type of the video format. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#videoFormat". |
| `resolution` | `object` | Represents the dimensions of ads, placements, creatives, or creative assets. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `videoFormats_get` | `SELECT` | `id, profileId` | Gets one video format by ID. |
| `videoFormats_list` | `SELECT` | `profileId` | Lists available video formats. |
