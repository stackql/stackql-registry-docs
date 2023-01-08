---
title: catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs
  - recommendationengine
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
<tr><td><b>Name</b></td><td><code>catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recommendationengine.catalogs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Pagination token, if not returned indicates the last page. |
| `catalogs` | `array` | Output only. All the customer's catalogs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_catalogs_list` | `SELECT` | `locationsId, projectsId` | Lists all the catalog configurations associated with the project. |
| `projects_locations_catalogs_patch` | `EXEC` | `catalogsId, locationsId, projectsId` | Updates the catalog configuration. |
