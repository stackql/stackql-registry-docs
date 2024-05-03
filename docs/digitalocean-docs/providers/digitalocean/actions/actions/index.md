---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
  - actions
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
<tr><td><b>Name</b></td><td><code>actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.actions.actions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | A unique numeric ID that can be used to identify and reference an action. |
| <CopyableCode code="completed_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the action was completed. |
| <CopyableCode code="region" /> | `object` |  |
| <CopyableCode code="region_slug" /> | `string` | A human-readable string that is used as a unique identifier for each region. |
| <CopyableCode code="resource_id" /> | `integer` | A unique identifier for the resource that the action is associated with. |
| <CopyableCode code="resource_type" /> | `string` | The type of resource that the action is associated with. |
| <CopyableCode code="started_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the action was initiated. |
| <CopyableCode code="status" /> | `string` | The current status of the action. This can be "in-progress", "completed", or "errored". |
| <CopyableCode code="type" /> | `string` | This is the type of action that the object represents. For example, this could be "transfer" to represent the state of an image transfer action. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="action_id" /> | To retrieve a specific action object, send a GET request to `/v2/actions/$ACTION_ID`. |
| <CopyableCode code="list" /> | `SELECT` |  | This will be the entire list of actions taken on your account, so it will be quite large. As with any large collection returned by the API, the results will be paginated with only 20 on each page by default. |
| <CopyableCode code="_get" /> | `EXEC` | <CopyableCode code="action_id" /> | To retrieve a specific action object, send a GET request to `/v2/actions/$ACTION_ID`. |
| <CopyableCode code="_list" /> | `EXEC` |  | This will be the entire list of actions taken on your account, so it will be quite large. As with any large collection returned by the API, the results will be paginated with only 20 on each page by default. |
