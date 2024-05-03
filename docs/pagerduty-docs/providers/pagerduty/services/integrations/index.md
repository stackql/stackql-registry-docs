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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.services.integrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` | The name of this integration. |
| <CopyableCode code="_type" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` | The date/time when this integration was created. |
| <CopyableCode code="email_filter_mode" /> | `string` | Specify for generic_email_inbound_integration. May override email_incident_creation |
| <CopyableCode code="email_filters" /> | `array` | Specify for generic_email_inbound_integration. |
| <CopyableCode code="email_incident_creation" /> | `string` | Specify for generic_email_inbound_integration |
| <CopyableCode code="email_parsers" /> | `array` | Specify for generic_email_inbound_integration. |
| <CopyableCode code="email_parsing_fallback" /> | `string` | Specify for generic_email_inbound_integration. |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="integration_email" /> | `string` | Specify for generic_email_inbound_integration. Must be set to an email address @your-subdomain.pagerduty.com |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="service" /> | `object` |  |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="vendor" /> | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_service_integration" /> | `SELECT` | <CopyableCode code="id, integration_id" /> | Get details about an integration belonging to a service.<br /><br />A service may represent an application, component, or team you wish to open incidents against.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#services)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| <CopyableCode code="create_service_integration" /> | `INSERT` | <CopyableCode code="id, data__integration" /> | Create a new integration belonging to a Service.<br /><br />A service may represent an application, component, or team you wish to open incidents against.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#services)<br /><br />Scoped OAuth requires: `services.write`<br /> |
| <CopyableCode code="_get_service_integration" /> | `EXEC` | <CopyableCode code="id, integration_id" /> | Get details about an integration belonging to a service.<br /><br />A service may represent an application, component, or team you wish to open incidents against.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#services)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| <CopyableCode code="update_service_integration" /> | `EXEC` | <CopyableCode code="id, integration_id, data__integration" /> | Update an integration belonging to a Service.<br /><br />A service may represent an application, component, or team you wish to open incidents against.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#services)<br /><br />Scoped OAuth requires: `services.write`<br /> |
