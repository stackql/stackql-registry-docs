---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - translate
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
<tr><td><b>Id</b></td><td><code>google.translate.locations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `locations` | `array` | A list of locations that matches the specified filter in the request. |
| `nextPageToken` | `string` | The standard List next-page token. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_list` | `SELECT` | `projectsId` | Lists information about the supported locations for this service. |
| `projects_locations_batch_translate_document` | `EXEC` | `locationsId, projectsId` | Translates a large volume of document in asynchronous batch mode. This function provides real-time output as the inputs are being processed. If caller cancels a request, the partial results (for an input file, it's all or nothing) may still be available on the specified output location. This call returns immediately and you can use google.longrunning.Operation.name to poll the status of the call. |
| `projects_locations_batch_translate_text` | `EXEC` | `locationsId, projectsId` | Translates a large volume of text in asynchronous batch mode. This function provides real-time output as the inputs are being processed. If caller cancels a request, the partial results (for an input file, it's all or nothing) may still be available on the specified output location. This call returns immediately and you can use google.longrunning.Operation.name to poll the status of the call. |
| `projects_locations_detect_language` | `EXEC` | `locationsId, projectsId` | Detects the language of text within a request. |
| `projects_locations_get` | `EXEC` | `locationsId, projectsId` | Gets information about a location. |
| `projects_locations_romanize_text` | `EXEC` | `locationsId, projectsId` | Romanize input text written in non-Latin scripts to Latin text. |
| `projects_locations_translate_document` | `EXEC` | `locationsId, projectsId` | Translates documents in synchronous mode. |
| `projects_locations_translate_text` | `EXEC` | `locationsId, projectsId` | Translates input text and returns translated text. |
