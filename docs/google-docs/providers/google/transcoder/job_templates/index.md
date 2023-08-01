---
title: job_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - job_templates
  - transcoder
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
<tr><td><b>Name</b></td><td><code>job_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.transcoder.job_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The pagination token. |
| `unreachable` | `array` | List of regions that could not be reached. |
| `jobTemplates` | `array` | List of job templates in the specified region. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobTemplatesId, locationsId, projectsId` | Returns the job template data. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists job templates in the specified region. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a job template in the specified region. |
| `delete` | `DELETE` | `jobTemplatesId, locationsId, projectsId` | Deletes a job template. |
