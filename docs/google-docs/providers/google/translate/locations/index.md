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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | Resource name for the location, which may vary between implementations. For example: `"projects/example-project/locations/us-east1"` |
| `labels` | `object` | Cross-service attributes for the location. For example {"cloud.googleapis.com/region": "us-east1"} |
| `locationId` | `string` | The canonical id for this location. For example: `"us-east1"`. |
| `metadata` | `object` | Service-specific metadata. For example the available capacity at the given location. |
| `displayName` | `string` | The friendly name for this location, typically a nearby city name. For example, "Tokyo". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_get` | `SELECT` | `locationsId, projectsId` | Gets information about a location. |
| `projects_locations_list` | `SELECT` | `projectsId` | Lists information about the supported locations for this service. |
| `projects_locations_batchTranslateDocument` | `EXEC` | `locationsId, projectsId` | Translates a large volume of document in asynchronous batch mode. This function provides real-time output as the inputs are being processed. If caller cancels a request, the partial results (for an input file, it's all or nothing) may still be available on the specified output location. This call returns immediately and you can use google.longrunning.Operation.name to poll the status of the call. |
| `projects_locations_batchTranslateText` | `EXEC` | `locationsId, projectsId` | Translates a large volume of text in asynchronous batch mode. This function provides real-time output as the inputs are being processed. If caller cancels a request, the partial results (for an input file, it's all or nothing) may still be available on the specified output location. This call returns immediately and you can use google.longrunning.Operation.name to poll the status of the call. |
| `projects_locations_detectLanguage` | `EXEC` | `locationsId, projectsId` | Detects the language of text within a request. |
| `projects_locations_translateDocument` | `EXEC` | `locationsId, projectsId` | Translates documents in synchronous mode. |
| `projects_locations_translateText` | `EXEC` | `locationsId, projectsId` | Translates input text and returns translated text. |
