---
title: preference_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - preference_sets
  - migrationcenter
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
<tr><td><b>Name</b></td><td><code>preference_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.migrationcenter.preference_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | Locations that could not be reached. |
| `nextPageToken` | `string` | A token identifying a page of results the server should return. |
| `preferenceSets` | `array` | The list of PreferenceSets |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, preferenceSetsId, projectsId` | Gets the details of a preference set. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists all the preference sets in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new preference set in a given project and location. |
| `delete` | `DELETE` | `locationsId, preferenceSetsId, projectsId` | Deletes a preference set. |
| `patch` | `EXEC` | `locationsId, preferenceSetsId, projectsId` | Updates the parameters of a preference set. |
