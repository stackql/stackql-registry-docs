---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - services
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.services.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` | The name of the service. |
| <CopyableCode code="description" /> | `string` | The user-provided description of the service. |
| <CopyableCode code="_type" /> | `string` | The type of object being created. |
| <CopyableCode code="acknowledgement_timeout" /> | `integer` | Time in seconds that an incident changes to the Triggered State after being Acknowledged. Value is `null` if the feature is disabled. Value must not be negative. Setting this field to `0`, `null` (or unset in POST request) will disable the feature. |
| <CopyableCode code="addons" /> | `array` | The array of Add-ons associated with this service. |
| <CopyableCode code="alert_creation" /> | `string` | Whether a service creates only incidents, or both alerts and incidents. A service must create alerts in order to enable incident merging.<br />* "create_incidents" - The service will create one incident and zero alerts for each incoming event.<br />* "create_alerts_and_incidents" - The service will create one incident and one associated alert for each incoming event.<br /> |
| <CopyableCode code="alert_grouping" /> | `string` | Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. There are three available options:<br />* null - No alert grouping on the service. Each alert will create a separate incident;<br />* "time" - All alerts within a specified duration will be grouped into the same incident. This duration is set in the `alert_grouping_timeout` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans;<br />* "intelligent" - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plans<br /> |
| <CopyableCode code="alert_grouping_parameters" /> | `object` | Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. To turn grouping off set the type to null.<br /> |
| <CopyableCode code="alert_grouping_timeout" /> | `integer` | The duration in minutes within which to automatically group incoming alerts. This setting applies only when `alert_grouping` is set to `time`. To continue grouping alerts until the Incident is resolved, set this value to `0`.<br /> |
| <CopyableCode code="auto_pause_notifications_parameters" /> | `object` | Defines how alerts on this service are automatically suspended for a period of time before triggering, when identified as likely being transient. Note that automatically pausing notifications is only available on certain plans. |
| <CopyableCode code="auto_resolve_timeout" /> | `integer` | Time in seconds that an incident is automatically resolved if left open for that long. Value is `null` if the feature is disabled. Value must not be negative. Setting this field to `0`, `null` (or unset in POST request) will disable the feature. |
| <CopyableCode code="created_at" /> | `string` | The date/time when this service was created |
| <CopyableCode code="escalation_policy" /> | `object` |  |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="incident_urgency_rule" /> | `object` |  |
| <CopyableCode code="integrations" /> | `array` | An array containing Integration objects that belong to this service. If `integrations` is passed as an argument, these are full objects - otherwise, these are references. |
| <CopyableCode code="last_incident_timestamp" /> | `string` | The date/time when the most recent incident was created for this service. |
| <CopyableCode code="response_play" /> | `object` | Response plays associated with this service. |
| <CopyableCode code="scheduled_actions" /> | `array` | An array containing scheduled actions for the service. |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="status" /> | `string` | The current state of the Service. Valid statuses are:<br /><br /><br />- `active`: The service is enabled and has no open incidents. This is the only status a service can be created with.<br />- `warning`: The service is enabled and has one or more acknowledged incidents.<br />- `critical`: The service is enabled and has one or more triggered incidents.<br />- `maintenance`: The service is under maintenance, no new incidents will be triggered during maintenance mode.<br />- `disabled`: The service is disabled and will not have any new triggered incidents.<br /> |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="support_hours" /> | `object` |  |
| <CopyableCode code="teams" /> | `array` | The set of teams associated with this service. |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_service" /> | `SELECT` | <CopyableCode code="id" /> | Get details about an existing service.<br /><br />A service may represent an application, component, or team you wish to open incidents against.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#services)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| <CopyableCode code="list_services" /> | `SELECT` |  | List existing Services.<br /><br />A service may represent an application, component, or team you wish to open incidents against.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#services)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| <CopyableCode code="create_service" /> | `INSERT` | <CopyableCode code="data__service" /> | Create a new service.<br /><br />If `status` is included in the request, it must have a value of `active` when creating a new service. If a different status is required, make a second request to update the service.<br /><br />A service may represent an application, component, or team you wish to open incidents against.<br /><br />There is a limit of 25,000 services per account. If the limit is reached, the API will respond with an error. There is also a limit of 100,000 open Incidents per Service. If the limit is reached and `auto_resolve_timeout` is disabled (set to 0 or null), the `auto_resolve_timeout` property will automatically be set to  84600 (1 day).<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#services)<br /><br />Scoped OAuth requires: `services.write`<br /> |
| <CopyableCode code="delete_service" /> | `DELETE` | <CopyableCode code="id" /> | Delete an existing service.<br /><br />Once the service is deleted, it will not be accessible from the web UI and new incidents won't be able to be created for this service.<br /><br />A service may represent an application, component, or team you wish to open incidents against.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#services)<br /><br />Scoped OAuth requires: `services.write`<br /> |
| <CopyableCode code="_get_service" /> | `EXEC` | <CopyableCode code="id" /> | Get details about an existing service.<br /><br />A service may represent an application, component, or team you wish to open incidents against.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#services)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| <CopyableCode code="_list_services" /> | `EXEC` |  | List existing Services.<br /><br />A service may represent an application, component, or team you wish to open incidents against.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#services)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| <CopyableCode code="update_service" /> | `EXEC` | <CopyableCode code="id, data__service" /> | Update an existing service.<br /><br />A service may represent an application, component, or team you wish to open incidents against.<br /><br />There is a limit of 100,000 open Incidents per Service. If the limit is reached and you disable `auto_resolve_timeout` (set to 0 or null), the API will respond with an error.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#services)<br /><br />Scoped OAuth requires: `services.write`<br /> |
