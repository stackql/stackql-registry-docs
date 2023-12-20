---
title: license
hide_title: false
hide_table_of_contents: false
keywords:
  - license
  - users
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
<tr><td><b>Name</b></td><td><code>license</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.users.license</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Uniquely identifies the resource |
| `name` | `string` | Name of the License.<br /> |
| `description` | `string` | Description of the License. May include the names of add-ons associated with<br />the License, if there are any.<br /> |
| `html_url` | `string` | HTML URL to access the License |
| `role_group` | `string` | Indicates whether this License is assignable to full or stakeholder Users |
| `self` | `string` | API URL to access the License |
| `summary` | `string` | Summary of the License |
| `type` | `string` | Type of object |
| `valid_roles` | `array` | The roles a User with this License can have |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_user_license` | `SELECT` | `id` |
| `_get_user_license` | `EXEC` | `id` |
