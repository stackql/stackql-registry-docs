---
title: triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - triggers
  - eventarc
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
<tr><td><b>Name</b></td><td><code>triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.eventarc.triggers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `triggers` | `array` | The requested triggers, up to the number specified in `page_size`. |
| `unreachable` | `array` | Unreachable resources, if any. |
| `nextPageToken` | `string` | A page token that can be sent to `ListTriggers` to request the next page. If this is empty, then there are no more pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, triggersId` | Get a single trigger. |
| `list` | `SELECT` | `locationsId, projectsId` | List triggers. |
| `create` | `INSERT` | `locationsId, projectsId` | Create a new trigger in a particular project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, triggersId` | Delete a single trigger. |
| `patch` | `EXEC` | `locationsId, projectsId, triggersId` | Update a single trigger. |
