---
title: extension_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - extension_schemas
  - extension_schemas
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
<tr><td><b>Name</b></td><td><code>extension_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.extension_schemas.extension_schemas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | The long description for the Extension |
| <CopyableCode code="guide_url" /> | `string` | A link to the extension's support guide |
| <CopyableCode code="icon_url" /> | `string` | A small logo, 18-by-18 pixels. |
| <CopyableCode code="key" /> | `string` | Machine friendly display label |
| <CopyableCode code="label" /> | `string` | Human friendly display label |
| <CopyableCode code="logo_url" /> | `string` | A large logo, 75 pixels high and no more than 300 pixels wide. |
| <CopyableCode code="send_types" /> | `array` | The types of PagerDuty incident events that will activate this Extension |
| <CopyableCode code="url" /> | `string` | The url that the webhook payload will be sent to for this Extension. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_extension_schema" /> | `SELECT` | <CopyableCode code="id" /> | Get details about one specific extension vendor.<br /><br />A PagerDuty extension vendor represents a specific type of outbound extension such as Generic Webhook, Slack, ServiceNow.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#extension-schemas)<br /><br />Scoped OAuth requires: `extension_schemas.read`<br /> |
| <CopyableCode code="list_extension_schemas" /> | `SELECT` |  | List all extension schemas.<br /><br />A PagerDuty extension vendor represents a specific type of outbound extension such as Generic Webhook, Slack, ServiceNow.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#extension-schemas)<br /><br />Scoped OAuth requires: `extension_schemas.read`<br /> |
| <CopyableCode code="_get_extension_schema" /> | `EXEC` | <CopyableCode code="id" /> | Get details about one specific extension vendor.<br /><br />A PagerDuty extension vendor represents a specific type of outbound extension such as Generic Webhook, Slack, ServiceNow.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#extension-schemas)<br /><br />Scoped OAuth requires: `extension_schemas.read`<br /> |
| <CopyableCode code="_list_extension_schemas" /> | `EXEC` |  | List all extension schemas.<br /><br />A PagerDuty extension vendor represents a specific type of outbound extension such as Generic Webhook, Slack, ServiceNow.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#extension-schemas)<br /><br />Scoped OAuth requires: `extension_schemas.read`<br /> |
