---
title: past_incidents
hide_title: false
hide_table_of_contents: false
keywords:
  - past_incidents
  - incidents
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
<tr><td><b>Name</b></td><td><code>past_incidents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.incidents.past_incidents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `incident` | `object` | Incident model reference |
| `score` | `number` | The computed similarity score associated with the incident and parent incident  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_past_incidents` | `SELECT` | `id` |
| `_get_past_incidents` | `EXEC` | `id` |
