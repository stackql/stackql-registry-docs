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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>technical_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.service_dependencies.technical_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="dependent_service" /> | `object` | The reference to the service that is dependent on the technical service. |
| <CopyableCode code="supporting_service" /> | `object` | The reference to the service that supports the technical service. |
| <CopyableCode code="type" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_technical_service_service_dependencies" /> | `SELECT` | <CopyableCode code="id" /> | Get all immediate dependencies of any technical service.<br />Technical services are also known as `services`.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#services)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| <CopyableCode code="create_service_dependency" /> | `INSERT` |  | Create new dependencies between two services.<br /><br />Business services model capabilities that span multiple technical services and that may be owned by several different teams.<br /><br />A service can have a maximum of 2,000 dependencies with a depth limit of 100. If the limit is reached, the API will respond with an error.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#business-services)<br /><br />Scoped OAuth requires: `services.write`<br /> |
| <CopyableCode code="_get_technical_service_service_dependencies" /> | `EXEC` | <CopyableCode code="id" /> | Get all immediate dependencies of any technical service.<br />Technical services are also known as `services`.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#services)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| <CopyableCode code="delete_service_dependency" /> | `EXEC` |  | Disassociate dependencies between two services.<br /><br />Business services model capabilities that span multiple technical services and that may be owned by several different teams.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#business-services)<br /><br />Scoped OAuth requires: `services.write`<br /> |
