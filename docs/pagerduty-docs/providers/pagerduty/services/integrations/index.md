---
title: integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - integrations
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.services.integrations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` | The name of this integration. |
| `_type` | `string` |  |
| `created_at` | `string` | The date/time when this integration was created. |
| `email_filter_mode` | `string` | Specify for generic_email_inbound_integration. May override email_incident_creation |
| `email_filters` | `array` | Specify for generic_email_inbound_integration. |
| `email_incident_creation` | `string` | Specify for generic_email_inbound_integration |
| `email_parsers` | `array` | Specify for generic_email_inbound_integration. |
| `email_parsing_fallback` | `string` | Specify for generic_email_inbound_integration. |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `integration_email` | `string` | Specify for generic_email_inbound_integration. Must be set to an email address @your-subdomain.pagerduty.com |
| `self` | `string` | the API show URL at which the object is accessible |
| `service` | `object` |  |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `vendor` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_service_integration` | `SELECT` | `id, integration_id` | Get details about an integration belonging to a service.<br /><br />A service may represent an application, component, or team you wish to open incidents against.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#services)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| `create_service_integration` | `INSERT` | `id, data__integration` | Create a new integration belonging to a Service.<br /><br />A service may represent an application, component, or team you wish to open incidents against.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#services)<br /><br />Scoped OAuth requires: `services.write`<br /> |
| `_get_service_integration` | `EXEC` | `id, integration_id` | Get details about an integration belonging to a service.<br /><br />A service may represent an application, component, or team you wish to open incidents against.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#services)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| `update_service_integration` | `EXEC` | `id, integration_id, data__integration` | Update an integration belonging to a Service.<br /><br />A service may represent an application, component, or team you wish to open incidents against.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#services)<br /><br />Scoped OAuth requires: `services.write`<br /> |
