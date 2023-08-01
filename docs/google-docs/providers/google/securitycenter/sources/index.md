---
title: sources
hide_title: false
hide_table_of_contents: false
keywords:
  - sources
  - securitycenter
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
<tr><td><b>Id</b></td><td><code>google.securitycenter.sources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results. |
| `sources` | `array` | Sources belonging to the requested parent. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_sources_list` | `SELECT` | `foldersId` | Lists all sources belonging to an organization. |
| `organizations_sources_get` | `SELECT` | `organizationsId, sourcesId` | Gets a source. |
| `organizations_sources_list` | `SELECT` | `organizationsId` | Lists all sources belonging to an organization. |
| `projects_sources_list` | `SELECT` | `projectsId` | Lists all sources belonging to an organization. |
| `organizations_sources_create` | `INSERT` | `organizationsId` | Creates a source. |
| `organizations_sources_patch` | `EXEC` | `organizationsId, sourcesId` | Updates a source. |
