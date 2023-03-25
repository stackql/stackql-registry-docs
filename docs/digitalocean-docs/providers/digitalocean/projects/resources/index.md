---
title: resources
hide_title: false
hide_table_of_contents: false
keywords:
  - resources
  - projects
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.projects.resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `links` | `object` | The links object contains the `self` object, which contains the resource relationship. |
| `status` | `string` | The status of assigning and fetching the resources. |
| `urn` | `string` | The uniform resource name (URN) for the resource in the format do:resource_type:resource_id. |
| `assigned_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the project was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_resources` | `SELECT` | `project_id` | To list all your resources in a project, send a GET request to `/v2/projects/$PROJECT_ID/resources`. |
| `_list_resources` | `EXEC` | `project_id` | To list all your resources in a project, send a GET request to `/v2/projects/$PROJECT_ID/resources`. |
| `assign_resources` | `EXEC` | `project_id` | To assign resources to a project, send a POST request to `/v2/projects/$PROJECT_ID/resources`. |
