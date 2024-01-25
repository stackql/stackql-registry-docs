---
title: role_eligibility_schedule_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - role_eligibility_schedule_instances
  - authorization
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_eligibility_schedule_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.role_eligibility_schedule_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The role eligibility schedule instance ID. |
| `name` | `string` | The role eligibility schedule instance name. |
| `properties` | `object` | Role eligibility schedule properties with scope. |
| `type` | `string` | The role eligibility schedule instance type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `roleEligibilityScheduleInstanceName, scope` |
