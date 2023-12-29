---
title: findings
hide_title: false
hide_table_of_contents: false
keywords:
  - findings
  - security_monitoring
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
<tr><td><b>Name</b></td><td><code>findings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.security_monitoring.findings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique ID for this finding. |
| `attributes` | `object` | The JSON:API attributes of the detailed finding. |
| `type` | `string` | The JSON:API type for findings that have the message and resource configuration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_finding` | `SELECT` | `finding_id, dd_site` | Returns a single finding with message and resource configuration. |
| `list_findings` | `SELECT` | `dd_site` | Get a list of CSPM findings.<br /><br />### Filtering<br /><br />Filters can be applied by appending query parameters to the URL.<br /><br />  - Using a single filter: `?filter[attribute_key]=attribute_value`<br />  - Chaining filters: `?filter[attribute_key]=attribute_value&filter[attribute_key]=attribute_value...`<br />  - Filtering on tags: `?filter[tags]=tag_key:tag_value&filter[tags]=tag_key_2:tag_value_2`<br /><br />Here, `attribute_key` can be any of the filter keys described further below.<br /><br />Query parameters of type `integer` support comparison operators (`&gt;`, `&gt;=`, `&lt;`, `&lt;=`). This is particularly useful when filtering by `evaluation_changed_at` or `resource_discovery_timestamp`. For example: `?filter[evaluation_changed_at]=&gt;20123123121`.<br /><br />You can also use the negation operator on strings. For example, use `filter[resource_type]=-aws*` to filter for any non-AWS resources.<br /><br />The operator must come after the equal sign. For example, to filter with the `&gt;=` operator, add the operator after the equal sign: `filter[evaluation_changed_at]=&gt;=1678809373257`.<br /><br />Query parameters must be only among the documented ones and with values of correct types. Duplicated query parameters (e.g. `filter[status]=low&filter[status]=info`) are not allowed.<br /><br />### Response<br /><br />The response includes an array of finding objects, pagination metadata, and a count of items that match the query.<br /><br />Each finding object contains the following:<br /><br />- The finding ID that can be used in a `GetFinding` request to retrieve the full finding details.<br />- Core attributes, including status, evaluation, high-level resource details, muted state, and rule details.<br />- `evaluation_changed_at` and `resource_discovery_date` time stamps.<br />- An array of associated tags.<br /> |
| `_get_finding` | `EXEC` | `finding_id, dd_site` | Returns a single finding with message and resource configuration. |
| `_list_findings` | `EXEC` | `dd_site` | Get a list of CSPM findings.<br /><br />### Filtering<br /><br />Filters can be applied by appending query parameters to the URL.<br /><br />  - Using a single filter: `?filter[attribute_key]=attribute_value`<br />  - Chaining filters: `?filter[attribute_key]=attribute_value&filter[attribute_key]=attribute_value...`<br />  - Filtering on tags: `?filter[tags]=tag_key:tag_value&filter[tags]=tag_key_2:tag_value_2`<br /><br />Here, `attribute_key` can be any of the filter keys described further below.<br /><br />Query parameters of type `integer` support comparison operators (`&gt;`, `&gt;=`, `&lt;`, `&lt;=`). This is particularly useful when filtering by `evaluation_changed_at` or `resource_discovery_timestamp`. For example: `?filter[evaluation_changed_at]=&gt;20123123121`.<br /><br />You can also use the negation operator on strings. For example, use `filter[resource_type]=-aws*` to filter for any non-AWS resources.<br /><br />The operator must come after the equal sign. For example, to filter with the `&gt;=` operator, add the operator after the equal sign: `filter[evaluation_changed_at]=&gt;=1678809373257`.<br /><br />Query parameters must be only among the documented ones and with values of correct types. Duplicated query parameters (e.g. `filter[status]=low&filter[status]=info`) are not allowed.<br /><br />### Response<br /><br />The response includes an array of finding objects, pagination metadata, and a count of items that match the query.<br /><br />Each finding object contains the following:<br /><br />- The finding ID that can be used in a `GetFinding` request to retrieve the full finding details.<br />- Core attributes, including status, evaluation, high-level resource details, muted state, and rule details.<br />- `evaluation_changed_at` and `resource_discovery_date` time stamps.<br />- An array of associated tags.<br /> |
| `mute_findings` | `EXEC` | `data__data, dd_site` | Mute or unmute findings. |
