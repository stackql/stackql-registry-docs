---
title: impacts
hide_title: false
hide_table_of_contents: false
keywords:
  - impacts
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
<tr><td><b>Name</b></td><td><code>impacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.business_services.impacts</code></td></tr>
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
| `get_business_service_impacts` | `SELECT` | `X-EARLY-ACCESS` |
| `_get_business_service_impacts` | `EXEC` | `X-EARLY-ACCESS` |
