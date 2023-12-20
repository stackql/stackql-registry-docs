---
title: business_services
hide_title: false
hide_table_of_contents: false
keywords:
  - business_services
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
<tr><td><b>Name</b></td><td><code>business_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.business_services.business_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` | The name of the business service. |
| `description` | `string` | The user-provided description of the business service. |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `point_of_contact` | `string` | The point of contact assigned to this service. |
| `self` | `string` | the API show URL at which the object is accessible |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `team` | `object` | Reference to the team that owns the business service. |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_business_service` | `SELECT` | `id` | Get details about an existing Business Service.<br /><br />Business services model capabilities that span multiple technical services and that may be owned by several different teams.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#business-services)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| `list_business_services` | `SELECT` |  | List existing Business Services.<br /><br />Business services model capabilities that span multiple technical services and that may be owned by several different teams.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#business-services)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| `create_business_service` | `INSERT` |  | Create a new Business Service.<br /><br />Business services model capabilities that span multiple technical services and that may be owned by several different teams.<br /><br />There is a limit of 5,000 business services per account. If the limit is reached, the API will respond with an error.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#business-services)<br /><br />Scoped OAuth requires: `services.write`<br /> |
| `delete_business_service` | `DELETE` | `id` | Delete an existing Business Service.<br /><br />Once the service is deleted, it will not be accessible from the web UI and new incidents won't be able to be created for this service.<br /><br />Business services model capabilities that span multiple technical services and that may be owned by several different teams.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#business-services)<br /><br />Scoped OAuth requires: `services.write`<br /> |
| `_get_business_service` | `EXEC` | `id` | Get details about an existing Business Service.<br /><br />Business services model capabilities that span multiple technical services and that may be owned by several different teams.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#business-services)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| `_list_business_services` | `EXEC` |  | List existing Business Services.<br /><br />Business services model capabilities that span multiple technical services and that may be owned by several different teams.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#business-services)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| `update_business_service` | `EXEC` | `id` | Update an existing Business Service. NOTE that this endpoint also accepts the PATCH verb.<br /><br />Business services model capabilities that span multiple technical services and that may be owned by several different teams.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#business-services)<br /><br />Scoped OAuth requires: `services.write`<br /> |
