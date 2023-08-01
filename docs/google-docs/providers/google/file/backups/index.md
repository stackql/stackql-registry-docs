---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - file
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
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.file.backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The token you can use to retrieve the next page of results. Not returned if there are no more results in the list. |
| `unreachable` | `array` | Locations that could not be reached. |
| `backups` | `array` | A list of backups in the project for the specified location. If the `&#123;location&#125;` value in the request is "-", the response contains a list of backups from all locations. If any location is unreachable, the response will only return backups in reachable locations and the "unreachable" field will be populated with a list of unreachable locations. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupsId, locationsId, projectsId` | Gets the details of a specific backup. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists all backups in a project for either a specified location or for all locations. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a backup. |
| `delete` | `DELETE` | `backupsId, locationsId, projectsId` | Deletes a backup. |
| `patch` | `EXEC` | `backupsId, locationsId, projectsId` | Updates the settings of a specific backup. |
