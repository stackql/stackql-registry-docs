---
title: tracks
hide_title: false
hide_table_of_contents: false
keywords:
  - tracks
  - androidpublisher
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
<tr><td><b>Name</b></td><td><code>tracks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidpublisher.tracks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `releases` | `array` | In a read request, represents all active releases in the track. In an update request, represents desired changes. |
| `track` | `string` | Identifier of the track. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `edits_tracks_get` | `SELECT` | `editId, packageName, track` | Gets a track. |
| `edits_tracks_list` | `SELECT` | `editId, packageName` | Lists all tracks. |
| `edits_tracks_patch` | `EXEC` | `editId, packageName, track` | Patches a track. |
| `edits_tracks_update` | `EXEC` | `editId, packageName, track` | Updates a track. |
