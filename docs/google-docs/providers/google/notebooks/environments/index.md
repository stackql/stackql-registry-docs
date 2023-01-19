---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - notebooks
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
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.notebooks.environments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of this environment. Format: `projects/&#123;project_id&#125;/locations/&#123;location&#125;/environments/&#123;environment_id&#125;` |
| `description` | `string` | A brief description of this environment. |
| `postStartupScript` | `string` | Path to a Bash script that automatically runs after a notebook instance fully boots up. The path must be a URL or Cloud Storage path. Example: `"gs://path-to-file/file-name"` |
| `vmImage` | `object` | Definition of a custom Compute Engine virtual machine image for starting a notebook instance with the environment installed directly on the VM. |
| `containerImage` | `object` | Definition of a container image for starting a notebook instance with the environment installed in a container. |
| `createTime` | `string` | Output only. The time at which this environment was created. |
| `displayName` | `string` | Display name of this environment for the UI. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_environments_get` | `SELECT` | `environmentsId, locationsId, projectsId` | Gets details of a single Environment. |
| `projects_locations_environments_list` | `SELECT` | `locationsId, projectsId` | Lists environments in a project. |
| `projects_locations_environments_create` | `INSERT` | `locationsId, projectsId` | Creates a new Environment. |
| `projects_locations_environments_delete` | `DELETE` | `environmentsId, locationsId, projectsId` | Deletes a single Environment. |
