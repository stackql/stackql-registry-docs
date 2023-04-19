---
title: default
hide_title: false
hide_table_of_contents: false
keywords:
  - default
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
<tr><td><b>Name</b></td><td><code>default</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.projects.default</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique universal identifier of this project. |
| `name` | `string` | The human-readable name for the project. The maximum length is 175 characters and the name must be unique. |
| `description` | `string` | The description of the project. The maximum length is 255 characters. |
| `purpose` | `string` | The purpose of the project. The maximum length is 255 characters. It can<br />have one of the following values:<br /><br />- Just trying out DigitalOcean<br />- Class project / Educational purposes<br />- Website or blog<br />- Web Application<br />- Service or API<br />- Mobile Application<br />- Machine learning / AI / Data processing<br />- IoT<br />- Operational / Developer tooling<br /><br />If another value for purpose is specified, for example, "your custom purpose",<br />your purpose will be stored as `Other: your custom purpose`.<br /> |
| `created_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the project was created. |
| `owner_uuid` | `string` | The unique universal identifier of the project owner. |
| `owner_id` | `integer` | The integer id of the project owner. |
| `updated_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the project was updated. |
| `is_default` | `boolean` | If true, all resources will be added to this project if no project is specified. |
| `environment` | `string` | The environment of the project's resources. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_default` | `SELECT` |  | To get your default project, send a GET request to `/v2/projects/default`. |
| `_get_default` | `EXEC` |  | To get your default project, send a GET request to `/v2/projects/default`. |
| `patch_default` | `EXEC` |  | To update only specific attributes of your default project, send a PATCH request to `/v2/projects/default`. At least one of the following attributes needs to be sent. |
| `update_default` | `EXEC` | `data__description, data__environment, data__is_default, data__name, data__purpose` | To update you default project, send a PUT request to `/v2/projects/default`. All of the following attributes must be sent. |
