---
title: url_slugs_service_impacts
hide_title: false
hide_table_of_contents: false
keywords:
  - url_slugs_service_impacts
  - status_dashboards
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
<tr><td><b>Name</b></td><td><code>url_slugs_service_impacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.status_dashboards.url_slugs_service_impacts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` |  |
| `additional_fields` | `object` |  |
| `status` | `string` | The current impact status of the object |
| `type` | `string` | The kind of object that has been impacted |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_status_dashboard_service_impacts_by_url_slug` | `SELECT` | `X-EARLY-ACCESS, url_slug` |
| `_get_status_dashboard_service_impacts_by_url_slug` | `EXEC` | `X-EARLY-ACCESS, url_slug` |
