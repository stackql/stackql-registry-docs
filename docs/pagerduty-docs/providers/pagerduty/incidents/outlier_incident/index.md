---
title: outlier_incident
hide_title: false
hide_table_of_contents: false
keywords:
  - outlier_incident
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
<tr><td><b>Name</b></td><td><code>outlier_incident</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.incidents.outlier_incident</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `incident` | `object` |
| `incident_template` | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_outlier_incident` | `SELECT` | `id` |
| `_get_outlier_incident` | `EXEC` | `id` |
