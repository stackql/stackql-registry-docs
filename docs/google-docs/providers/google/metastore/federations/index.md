---
title: federations
hide_title: false
hide_table_of_contents: false
keywords:
  - federations
  - metastore
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
<tr><td><b>Name</b></td><td><code>federations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.metastore.federations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token that can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `unreachable` | `array` | Locations that could not be reached. |
| `federations` | `array` | The services in the specified location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `federationsId, locationsId, projectsId` | Gets the details of a single federation. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists federations in a project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a metastore federation in a project and location. |
| `delete` | `DELETE` | `federationsId, locationsId, projectsId` | Deletes a single federation. |
| `patch` | `EXEC` | `federationsId, locationsId, projectsId` | Updates the fields of a federation. |
