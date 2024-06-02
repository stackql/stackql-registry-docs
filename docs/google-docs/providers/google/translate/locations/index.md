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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="translate.locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name for the location, which may vary between implementations. For example: `"projects/example-project/locations/us-east1"` |
| <CopyableCode code="displayName" /> | `string` | The friendly name for this location, typically a nearby city name. For example, "Tokyo". |
| <CopyableCode code="labels" /> | `object` | Cross-service attributes for the location. For example &#123;"cloud.googleapis.com/region": "us-east1"&#125; |
| <CopyableCode code="locationId" /> | `string` | The canonical id for this location. For example: `"us-east1"`. |
| <CopyableCode code="metadata" /> | `object` | Service-specific metadata. For example the available capacity at the given location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Gets information about a location. |
| <CopyableCode code="projects_locations_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists information about the supported locations for this service. |
| <CopyableCode code="_projects_locations_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Lists information about the supported locations for this service. |
| <CopyableCode code="projects_locations_adaptive_mt_translate" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Translate text using Adaptive MT. |
| <CopyableCode code="projects_locations_batch_translate_document" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Translates a large volume of document in asynchronous batch mode. This function provides real-time output as the inputs are being processed. If caller cancels a request, the partial results (for an input file, it's all or nothing) may still be available on the specified output location. This call returns immediately and you can use google.longrunning.Operation.name to poll the status of the call. |
| <CopyableCode code="projects_locations_batch_translate_text" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Translates a large volume of text in asynchronous batch mode. This function provides real-time output as the inputs are being processed. If caller cancels a request, the partial results (for an input file, it's all or nothing) may still be available on the specified output location. This call returns immediately and you can use google.longrunning.Operation.name to poll the status of the call. |
| <CopyableCode code="projects_locations_detect_language" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Detects the language of text within a request. |
| <CopyableCode code="projects_locations_romanize_text" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Romanize input text written in non-Latin scripts to Latin text. |
| <CopyableCode code="projects_locations_translate_document" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Translates documents in synchronous mode. |
| <CopyableCode code="projects_locations_translate_text" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Translates input text and returns translated text. |
