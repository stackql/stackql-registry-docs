---
title: restore_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_plans
  - gkebackup
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
<tr><td><b>Name</b></td><td><code>restore_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkebackup.restore_plans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `restorePlans` | `array` | The list of RestorePlans matching the given criteria. |
| `unreachable` | `array` | Locations that could not be reached. |
| `nextPageToken` | `string` | A token which may be sent as page_token in a subsequent `ListRestorePlans` call to retrieve the next page of results. If this field is omitted or empty, then there are no more results to return. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, restorePlansId` | Retrieve the details of a single RestorePlan. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists RestorePlans in a given location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new RestorePlan in a given location. |
| `delete` | `DELETE` | `locationsId, projectsId, restorePlansId` | Deletes an existing RestorePlan. |
| `patch` | `EXEC` | `locationsId, projectsId, restorePlansId` | Update a RestorePlan. |
