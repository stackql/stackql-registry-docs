---
title: technical_services
hide_title: false
hide_table_of_contents: false
keywords:
  - technical_services
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
<tr><td><b>Name</b></td><td><code>technical_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.service_dependencies.technical_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `dependent_service` | `object` | The reference to the service that is dependent on the technical service. |
| `supporting_service` | `object` | The reference to the service that supports the technical service. |
| `type` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_technical_service_service_dependencies` | `SELECT` | `id` | Get all immediate dependencies of any technical service.<br />Technical services are also known as `services`.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#services)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| `create_service_dependency` | `INSERT` |  | Create new dependencies between two services.<br /><br />Business services model capabilities that span multiple technical services and that may be owned by several different teams.<br /><br />A service can have a maximum of 2,000 dependencies with a depth limit of 100. If the limit is reached, the API will respond with an error.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#business-services)<br /><br />Scoped OAuth requires: `services.write`<br /> |
| `_get_technical_service_service_dependencies` | `EXEC` | `id` | Get all immediate dependencies of any technical service.<br />Technical services are also known as `services`.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#services)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| `delete_service_dependency` | `EXEC` |  | Disassociate dependencies between two services.<br /><br />Business services model capabilities that span multiple technical services and that may be owned by several different teams.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#business-services)<br /><br />Scoped OAuth requires: `services.write`<br /> |
