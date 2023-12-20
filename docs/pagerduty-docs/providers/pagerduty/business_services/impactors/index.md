---
title: impactors
hide_title: false
hide_table_of_contents: false
keywords:
  - impactors
  - business_services
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
<tr><td><b>Name</b></td><td><code>impactors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.business_services.impactors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `type` | `string` | The kind of object that is impacting |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_business_service_top_level_impactors` | `SELECT` | `X-EARLY-ACCESS` |
| `_get_business_service_top_level_impactors` | `EXEC` | `X-EARLY-ACCESS` |
