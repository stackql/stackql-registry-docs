---
title: restriction_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - restriction_policies
  - restriction_policies
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restriction_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.restriction_policies.restriction_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier, always equivalent to the value specified in the `resource_id` path parameter. |
| `attributes` | `object` | Restriction policy attributes. |
| `type` | `string` | Restriction policy type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_restriction_policy` | `SELECT` | `resource_id, dd_site` | Retrieves the restriction policy associated with a specified resource. |
| `delete_restriction_policy` | `DELETE` | `resource_id, dd_site` | Deletes the restriction policy associated with a specified resource. |
| `_get_restriction_policy` | `EXEC` | `resource_id, dd_site` | Retrieves the restriction policy associated with a specified resource. |
| `update_restriction_policy` | `EXEC` | `resource_id, data__data, dd_site` | Updates the restriction policy associated with a resource.<br /><br />#### Supported resources<br />Restriction policies can be applied to the following resources:<br />- Connections: `connection`<br />- Dashboards: `dashboard`<br />- Notebooks: `notebook`<br />- Security Rules: `security-rule`<br />- Service Level Objectives: `slo`<br /><br />#### Supported relations for resources<br />Resource Type            \| Supported Relations<br />-------------------------\|--------------------------<br />Connections              \| `viewer`, `editor`, `resolver`<br />Dashboards               \| `viewer`, `editor`<br />Notebooks                \| `viewer`, `editor`<br />Security Rules           \| `viewer`, `editor`<br />Service Level Objectives \| `viewer`, `editor` |
