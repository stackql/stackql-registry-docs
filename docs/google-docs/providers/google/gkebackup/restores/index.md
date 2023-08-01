---
title: restores
hide_title: false
hide_table_of_contents: false
keywords:
  - restores
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
<tr><td><b>Name</b></td><td><code>restores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkebackup.restores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | Locations that could not be reached. |
| `nextPageToken` | `string` | A token which may be sent as page_token in a subsequent `ListRestores` call to retrieve the next page of results. If this field is omitted or empty, then there are no more results to return. |
| `restores` | `array` | The list of Restores matching the given criteria. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, restorePlansId, restoresId` | Retrieves the details of a single Restore. |
| `list` | `SELECT` | `locationsId, projectsId, restorePlansId` | Lists the Restores for a given RestorePlan. |
| `create` | `INSERT` | `locationsId, projectsId, restorePlansId` | Creates a new Restore for the given RestorePlan. |
| `delete` | `DELETE` | `locationsId, projectsId, restorePlansId, restoresId` | Deletes an existing Restore. |
| `patch` | `EXEC` | `locationsId, projectsId, restorePlansId, restoresId` | Update a Restore. |
