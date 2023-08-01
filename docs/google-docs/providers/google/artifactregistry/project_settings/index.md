---
title: project_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - project_settings
  - artifactregistry
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
<tr><td><b>Name</b></td><td><code>project_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.artifactregistry.project_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the project's settings. Always of the form: projects/&#123;project-id&#125;/projectSettings In update request: never set In response: always set |
| `legacyRedirectionState` | `string` | The redirection state of the legacy repositories in this project. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_project_settings` | `SELECT` | `projectsId` | Retrieves the Settings for the Project. |
| `update_project_settings` | `EXEC` | `projectsId` | Updates the Settings for the Project. |
