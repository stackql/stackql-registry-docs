---
title: sources
hide_title: false
hide_table_of_contents: false
keywords:
  - sources
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
<tr><td><b>Name</b></td><td><code>sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.migrationcenter.sources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | Locations that could not be reached. |
| `nextPageToken` | `string` | A token identifying a page of results the server should return. |
| `sources` | `array` | The list of sources. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, sourcesId` | Gets the details of a source. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists all the sources in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new source in a given project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, sourcesId` | Deletes a source. |
| `patch` | `EXEC` | `locationsId, projectsId, sourcesId` | Updates the parameters of a source. |
