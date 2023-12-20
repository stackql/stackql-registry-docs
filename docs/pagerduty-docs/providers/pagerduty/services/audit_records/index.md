---
title: audit_records
hide_title: false
hide_table_of_contents: false
keywords:
  - audit_records
  - services
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
<tr><td><b>Name</b></td><td><code>audit_records</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.services.audit_records</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `action` | `string` |  |
| `actors` | `array` |  |
| `details` | `object` | Additional details to provide further information about the action or<br />the resource that has been audited.<br /> |
| `execution_context` | `object` | Action execution context |
| `execution_time` | `string` | The date/time the action executed, in ISO8601 format and millisecond precision. |
| `method` | `object` | The method information |
| `root_resource` | `object` |  |
| `self` | `string` | Record URL. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_service_audit_records` | `SELECT` | `id` |
| `_list_service_audit_records` | `EXEC` | `id` |
