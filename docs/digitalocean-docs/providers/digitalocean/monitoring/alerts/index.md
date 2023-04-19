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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.monitoring.alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `policies` | `array` |  |
| `links` | `object` |  |
| `meta` | `object` | Information about the response itself. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_alertPolicy` | `SELECT` | `alert_uuid` | To retrieve a given alert policy, send a GET request to `/v2/monitoring/alerts/&#123;alert_uuid&#125;` |
| `list_alertPolicy` | `SELECT` |  | Returns all alert policies that are configured for the given account. To List all alert policies, send a GET request to `/v2/monitoring/alerts`. |
| `create_alertPolicy` | `INSERT` | `data__alerts, data__compare, data__description, data__enabled, data__entities, data__tags, data__type, data__value, data__window` | To create a new alert, send a POST request to `/v2/monitoring/alerts`. |
| `delete_alertPolicy` | `DELETE` | `alert_uuid` | To delete an alert policy, send a DELETE request to `/v2/monitoring/alerts/&#123;alert_uuid&#125;` |
| `update_alertPolicy` | `EXEC` | `alert_uuid, data__alerts, data__compare, data__description, data__enabled, data__entities, data__tags, data__type, data__value, data__window` | To update en existing policy, send a PUT request to `v2/monitoring/alerts/&#123;alert_uuid&#125;`. |
