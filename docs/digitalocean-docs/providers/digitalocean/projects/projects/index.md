---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.projects.projects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique universal identifier of this project. |
| <CopyableCode code="name" /> | `string` | The human-readable name for the project. The maximum length is 175 characters and the name must be unique. |
| <CopyableCode code="description" /> | `string` | The description of the project. The maximum length is 255 characters. |
| <CopyableCode code="created_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the project was created. |
| <CopyableCode code="environment" /> | `string` | The environment of the project's resources. |
| <CopyableCode code="is_default" /> | `boolean` | If true, all resources will be added to this project if no project is specified. |
| <CopyableCode code="owner_id" /> | `integer` | The integer id of the project owner. |
| <CopyableCode code="owner_uuid" /> | `string` | The unique universal identifier of the project owner. |
| <CopyableCode code="purpose" /> | `string` | The purpose of the project. The maximum length is 255 characters. It can<br />have one of the following values:<br /><br />- Just trying out DigitalOcean<br />- Class project / Educational purposes<br />- Website or blog<br />- Web Application<br />- Service or API<br />- Mobile Application<br />- Machine learning / AI / Data processing<br />- IoT<br />- Operational / Developer tooling<br /><br />If another value for purpose is specified, for example, "your custom purpose",<br />your purpose will be stored as `Other: your custom purpose`.<br /> |
| <CopyableCode code="updated_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the project was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project_id" /> | To get a project, send a GET request to `/v2/projects/$PROJECT_ID`. |
| <CopyableCode code="list" /> | `SELECT` |  | To list all your projects, send a GET request to `/v2/projects`. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="data__name, data__purpose" /> | To create a project, send a POST request to `/v2/projects`. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project_id" /> | To delete a project, send a DELETE request to `/v2/projects/$PROJECT_ID`. To<br />be deleted, a project must not have any resources assigned to it. Any existing<br />resources must first be reassigned or destroyed, or you will receive a 412 error.<br /><br />A successful request will receive a 204 status code with no body in response.<br />This indicates that the request was processed successfully.<br /> |
| <CopyableCode code="_get" /> | `EXEC` | <CopyableCode code="project_id" /> | To get a project, send a GET request to `/v2/projects/$PROJECT_ID`. |
| <CopyableCode code="_list" /> | `EXEC` |  | To list all your projects, send a GET request to `/v2/projects`. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="project_id" /> | To update only specific attributes of a project, send a PATCH request to `/v2/projects/$PROJECT_ID`. At least one of the following attributes needs to be sent. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="project_id, data__description, data__environment, data__is_default, data__name, data__purpose" /> | To update a project, send a PUT request to `/v2/projects/$PROJECT_ID`. All of the following attributes must be sent. |
