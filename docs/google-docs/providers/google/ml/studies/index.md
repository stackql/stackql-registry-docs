---
title: studies
hide_title: false
hide_table_of_contents: false
keywords:
  - studies
  - ml
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
<tr><td><b>Name</b></td><td><code>studies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.ml.studies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The name of a study. |
| `inactiveReason` | `string` | Output only. A human readable reason why the Study is inactive. This should be empty if a study is ACTIVE or COMPLETED. |
| `state` | `string` | Output only. The detailed state of a study. |
| `studyConfig` | `object` | Represents configuration of a study. |
| `createTime` | `string` | Output only. Time at which the study was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_studies_get` | `SELECT` | `locationsId, projectsId, studiesId` | Gets a study. |
| `projects_locations_studies_list` | `SELECT` | `locationsId, projectsId` | Lists all the studies in a region for an associated project. |
| `projects_locations_studies_create` | `INSERT` | `locationsId, projectsId` | Creates a study. |
| `projects_locations_studies_delete` | `DELETE` | `locationsId, projectsId, studiesId` | Deletes a study. |
