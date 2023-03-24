---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - apps
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
<tr><td><b>Id</b></td><td><code>digitalocean.apps.alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `progress` | `object` |
| `slack_webhooks` | `array` |
| `spec` | `object` |
| `component_name` | `string` |
| `emails` | `array` |
| `phase` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_alerts` | `SELECT` | `app_id` | List alerts associated to the app and any components. This includes configuration information about the alerts including emails, slack webhooks, and triggering events or conditions. |
| `_list_alerts` | `EXEC` | `app_id` | List alerts associated to the app and any components. This includes configuration information about the alerts including emails, slack webhooks, and triggering events or conditions. |
| `assign_alertDestinations` | `EXEC` | `alert_id, app_id` | Updates the emails and slack webhook destinations for app alerts. Emails must be associated to a user with access to the app. |
