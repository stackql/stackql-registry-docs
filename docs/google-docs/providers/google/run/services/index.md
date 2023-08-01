---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - run
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.run.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token indicating there are more items than page_size. Use it in the next ListServices request to continue. |
| `services` | `array` | The resulting list of Services. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, servicesId` | Gets information about a Service. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Services. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Service in a given project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, servicesId` | Deletes a Service. This will cause the Service to stop serving traffic and will delete all revisions. |
| `patch` | `EXEC` | `locationsId, projectsId, servicesId` | Updates a Service. |
