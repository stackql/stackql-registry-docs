---
title: targets
hide_title: false
hide_table_of_contents: false
keywords:
  - targets
  - clouddeploy
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
<tr><td><b>Name</b></td><td><code>targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.clouddeploy.targets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `targets` | `array` | The `Target` objects. |
| `unreachable` | `array` | Locations that could not be reached. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, targetsId` | Gets details of a single Target. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Targets in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Target in a given project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, targetsId` | Deletes a single Target. |
| `patch` | `EXEC` | `locationsId, projectsId, targetsId` | Updates the parameters of a single Target. |
