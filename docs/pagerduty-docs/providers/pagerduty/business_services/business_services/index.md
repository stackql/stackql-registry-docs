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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>business_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.business_services.business_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` | The name of the business service. |
| <CopyableCode code="description" /> | `string` | The user-provided description of the business service. |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="point_of_contact" /> | `string` | The point of contact assigned to this service. |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="team" /> | `object` | Reference to the team that owns the business service. |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_business_service" /> | `SELECT` | <CopyableCode code="id" /> | Get details about an existing Business Service.<br /><br />Business services model capabilities that span multiple technical services and that may be owned by several different teams.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#business-services)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| <CopyableCode code="list_business_services" /> | `SELECT` |  | List existing Business Services.<br /><br />Business services model capabilities that span multiple technical services and that may be owned by several different teams.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#business-services)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| <CopyableCode code="create_business_service" /> | `INSERT` |  | Create a new Business Service.<br /><br />Business services model capabilities that span multiple technical services and that may be owned by several different teams.<br /><br />There is a limit of 5,000 business services per account. If the limit is reached, the API will respond with an error.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#business-services)<br /><br />Scoped OAuth requires: `services.write`<br /> |
| <CopyableCode code="delete_business_service" /> | `DELETE` | <CopyableCode code="id" /> | Delete an existing Business Service.<br /><br />Once the service is deleted, it will not be accessible from the web UI and new incidents won't be able to be created for this service.<br /><br />Business services model capabilities that span multiple technical services and that may be owned by several different teams.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#business-services)<br /><br />Scoped OAuth requires: `services.write`<br /> |
| <CopyableCode code="_get_business_service" /> | `EXEC` | <CopyableCode code="id" /> | Get details about an existing Business Service.<br /><br />Business services model capabilities that span multiple technical services and that may be owned by several different teams.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#business-services)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| <CopyableCode code="_list_business_services" /> | `EXEC` |  | List existing Business Services.<br /><br />Business services model capabilities that span multiple technical services and that may be owned by several different teams.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#business-services)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| <CopyableCode code="update_business_service" /> | `EXEC` | <CopyableCode code="id" /> | Update an existing Business Service. NOTE that this endpoint also accepts the PATCH verb.<br /><br />Business services model capabilities that span multiple technical services and that may be owned by several different teams.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#business-services)<br /><br />Scoped OAuth requires: `services.write`<br /> |
