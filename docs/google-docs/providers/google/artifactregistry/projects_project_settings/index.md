---
title: projects_project_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - projects_project_settings
  - artifactregistry
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects_project_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.artifactregistry.projects_project_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the project's settings. Always of the form: projects/{project-id}/projectSettings In update request: never set In response: always set |
| `legacyRedirectionState` | `string` | The redirection state of the legacy repositories in this project. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_getProjectSettings` | `SELECT` | `projectsId` |
