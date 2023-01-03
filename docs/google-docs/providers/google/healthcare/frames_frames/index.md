---
title: frames_frames
hide_title: false
hide_table_of_contents: false
keywords:
  - frames_frames
  - healthcare
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>frames_frames</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.healthcare.frames_frames</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `data` | `string` | The HTTP request/response body as raw binary. |
| `extensions` | `array` | Application specific response metadata. Must be set in the first response for streaming APIs. |
| `contentType` | `string` | The HTTP Content-Type header value specifying the content type of the body. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_datasets_dicomStores_studies_series_instances_frames_retrieveFrames` | `SELECT` | `datasetsId, dicomStoresId, framesId, instancesId, locationsId, projectsId, seriesId, studiesId` |
