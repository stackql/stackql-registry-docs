---
title: response_plays
hide_title: false
hide_table_of_contents: false
keywords:
  - response_plays
  - response_plays
  - pagerduty    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>response_plays</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.response_plays.response_plays" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` | The name of the response play. |
| <CopyableCode code="description" /> | `string` | The description of the response play. |
| <CopyableCode code="_type" /> | `string` | The type of object being created. |
| <CopyableCode code="conference_number" /> | `string` | The telephone number that will be set as the conference number for any incident on which this response play is run. |
| <CopyableCode code="conference_type" /> | `string` | This field has three possible values and indicates how the response play was created.<br />  - `none` : The response play had no conference_number or conference_url set at time of creation.<br />  - `manual` : The response play had one or both of conference_number and conference_url set at time of creation.<br />  - `zoom` : Customers with the Zoom-Integration Entitelment can use this value to dynamicly configure conference number and url for zoom |
| <CopyableCode code="conference_url" /> | `string` | The URL that will be set as the conference URL for any incident on which this response play is run. |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="responders" /> | `array` | An array containing the users and/or escalation policies to be requested as responders to any incident on which this response play is run. |
| <CopyableCode code="responders_message" /> | `string` | The message body of the notification that will be sent to this response play's set of responders. If empty, a default response request notification will be sent. |
| <CopyableCode code="runnability" /> | `string` | String representing how this response play is allowed to be run. Valid options are:<br />  - `services`: This response play cannot be manually run by any users. It will run automatically for new incidents triggered on any services that are configured with this response play.<br />  - `teams`: This response play can be run manually on an incident only by members of its configured team. This option can only be selected when the `team` property for this response play is not empty.<br />  - `responders`: This response play can be run manually on an incident by any responders in this account. |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="subscribers" /> | `array` | An array containing the users and/or teams to be added as subscribers to any incident on which this response play is run. |
| <CopyableCode code="subscribers_message" /> | `string` | The content of the notification that will be sent to all incident subscribers upon the running of this response play. Note that this includes any users who may have already been subscribed to the incident prior to the running of this response play. If empty, no notifications will be sent. |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="team" /> | `` |  |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_response_play" /> | `SELECT` | <CopyableCode code="id" /> | Get details about an existing Response Play.<br /><br />Response Plays allow you to create packages of Incident Actions that can be applied during an Incident's life cycle.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#response-plays)<br /><br />When using a Global API token, the `From` header is required.<br />Scoped OAuth requires: `response_plays.read`<br /> |
| <CopyableCode code="list_response_plays" /> | `SELECT` |  | List all of the existing Response Plays.<br /><br />Response Plays allow you to create packages of Incident Actions that can be applied during an Incident's life cycle.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#response-plays)<br /><br />When using a Global API token, the `From` header is required.<br /><br />Scoped OAuth requires: `response_plays.read`<br /> |
| <CopyableCode code="create_response_play" /> | `INSERT` | <CopyableCode code="From, data__response_play" /> | Creates a new Response Plays.<br /><br />Response Plays allow you to create packages of Incident Actions that can be applied during an Incident's life cycle.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#response-plays)<br /><br />Scoped OAuth requires: `response_plays.write`<br /> |
| <CopyableCode code="delete_response_play" /> | `DELETE` | <CopyableCode code="From, id" /> | Delete an existing Response Play. Once the Response Play is deleted, the action cannot be undone.<br /><br />WARNING: When the Response Play is deleted, it is also removed from any Services that were using it.<br /><br />Response Plays allow you to create packages of Incident Actions that can be applied to an Incident.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#response-plays)<br /><br />Scoped OAuth requires: `response_plays.write`<br /> |
| <CopyableCode code="_get_response_play" /> | `EXEC` | <CopyableCode code="id" /> | Get details about an existing Response Play.<br /><br />Response Plays allow you to create packages of Incident Actions that can be applied during an Incident's life cycle.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#response-plays)<br /><br />When using a Global API token, the `From` header is required.<br />Scoped OAuth requires: `response_plays.read`<br /> |
| <CopyableCode code="_list_response_plays" /> | `EXEC` |  | List all of the existing Response Plays.<br /><br />Response Plays allow you to create packages of Incident Actions that can be applied during an Incident's life cycle.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#response-plays)<br /><br />When using a Global API token, the `From` header is required.<br /><br />Scoped OAuth requires: `response_plays.read`<br /> |
| <CopyableCode code="run_response_play" /> | `EXEC` | <CopyableCode code="From, response_play_id, data__incident" /> | Run a specified response play on a given incident.<br /><br />Response Plays are a package of Incident Actions that can be applied during an Incident's life cycle.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#response-plays)<br /><br />Scoped OAuth requires: `response_plays.write`<br /> |
| <CopyableCode code="update_response_play" /> | `EXEC` | <CopyableCode code="From, id, data__response_play" /> | Updates an existing Response Play.<br /><br />Response Plays allow you to create packages of Incident Actions that can be applied during an Incident's life cycle.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#response-plays)<br /><br />Scoped OAuth requires: `response_plays.write`<br /> |
