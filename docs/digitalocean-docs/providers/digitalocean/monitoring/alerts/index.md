---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - monitoring
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
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.monitoring.alerts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="links" /> | `object` |  |
| <CopyableCode code="meta" /> | `object` | Information about the response itself. |
| <CopyableCode code="policies" /> | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_alertPolicy" /> | `SELECT` | <CopyableCode code="alert_uuid" /> | To retrieve a given alert policy, send a GET request to `/v2/monitoring/alerts/&#123;alert_uuid&#125;` |
| <CopyableCode code="list_alertPolicy" /> | `SELECT` |  | Returns all alert policies that are configured for the given account. To List all alert policies, send a GET request to `/v2/monitoring/alerts`. |
| <CopyableCode code="create_alertPolicy" /> | `INSERT` | <CopyableCode code="data__alerts, data__compare, data__description, data__enabled, data__entities, data__tags, data__type, data__value, data__window" /> | To create a new alert, send a POST request to `/v2/monitoring/alerts`. |
| <CopyableCode code="delete_alertPolicy" /> | `DELETE` | <CopyableCode code="alert_uuid" /> | To delete an alert policy, send a DELETE request to `/v2/monitoring/alerts/&#123;alert_uuid&#125;` |
| <CopyableCode code="update_alertPolicy" /> | `EXEC` | <CopyableCode code="alert_uuid, data__alerts, data__compare, data__description, data__enabled, data__entities, data__tags, data__type, data__value, data__window" /> | To update en existing policy, send a PUT request to `v2/monitoring/alerts/&#123;alert_uuid&#125;`. |
