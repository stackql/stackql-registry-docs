---
title: business_services
hide_title: false
hide_table_of_contents: false
keywords:
  - business_services
  - service_dependencies
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
<tr><td><b>Name</b></td><td><code>business_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.service_dependencies.business_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `dependent_service` | `object` | The reference to the service that is dependent on the Business Service. |
| `supporting_service` | `object` | The reference to the service that supports the Business Service. |
| `type` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_business_service_service_dependencies` | `SELECT` | `id` |
| `_get_business_service_service_dependencies` | `EXEC` | `id` |
