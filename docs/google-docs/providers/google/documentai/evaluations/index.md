---
title: evaluations
hide_title: false
hide_table_of_contents: false
keywords:
  - evaluations
  - documentai
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
<tr><td><b>Name</b></td><td><code>evaluations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.documentai.evaluations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `evaluations` | `array` | The evaluations requested. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_processors_processor_versions_evaluations_list` | `SELECT` | `locationsId, processorVersionsId, processorsId, projectsId` | Retrieves a set of evaluations for a given processor version. |
| `projects_locations_processors_processor_versions_evaluations_get` | `EXEC` | `evaluationsId, locationsId, processorVersionsId, processorsId, projectsId` | Retrieves a specific evaluation. |
