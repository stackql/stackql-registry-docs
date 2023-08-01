---
title: sources
hide_title: false
hide_table_of_contents: false
keywords:
  - sources
  - vmmigration
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
<tr><td><b>Name</b></td><td><code>sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vmmigration.sources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Output only. A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `sources` | `array` | Output only. The list of sources response. |
| `unreachable` | `array` | Output only. Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, sourcesId` | Gets details of a single Source. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Sources in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Source in a given project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, sourcesId` | Deletes a single Source. |
| `patch` | `EXEC` | `locationsId, projectsId, sourcesId` | Updates the parameters of a single Source. |
