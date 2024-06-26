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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>default</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.projects.default" /></td></tr>
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
| <CopyableCode code="get_default" /> | `SELECT` |  | To get your default project, send a GET request to `/v2/projects/default`. |
| <CopyableCode code="_get_default" /> | `EXEC` |  | To get your default project, send a GET request to `/v2/projects/default`. |
| <CopyableCode code="patch_default" /> | `EXEC` |  | To update only specific attributes of your default project, send a PATCH request to `/v2/projects/default`. At least one of the following attributes needs to be sent. |
| <CopyableCode code="update_default" /> | `EXEC` | <CopyableCode code="data__description, data__environment, data__is_default, data__name, data__purpose" /> | To update you default project, send a PUT request to `/v2/projects/default`. All of the following attributes must be sent. |
