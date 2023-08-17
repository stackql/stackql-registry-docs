---
title: error_frames
hide_title: false
hide_table_of_contents: false
keywords:
  - error_frames
  - migrationcenter
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
<tr><td><b>Name</b></td><td><code>error_frames</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.migrationcenter.error_frames</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The identifier of the ErrorFrame. |
| `ingestionTime` | `string` | Output only. Frame ingestion time. |
| `originalFrame` | `object` | Contains data reported from an inventory source on an asset. |
| `violations` | `array` | Output only. All the violations that were detected for the frame. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `errorFramesId, locationsId, projectsId, sourcesId` | Gets the details of an error frame. |
| `list` | `SELECT` | `locationsId, projectsId, sourcesId` | Lists all error frames in a given source and location. |
| `_list` | `EXEC` | `locationsId, projectsId, sourcesId` | Lists all error frames in a given source and location. |
