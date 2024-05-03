---
title: opsgenie_services
hide_title: false
hide_table_of_contents: false
keywords:
  - opsgenie_services
  - opsgenie_integration
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>opsgenie_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.opsgenie_integration.opsgenie_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the Opsgenie service. |
| <CopyableCode code="attributes" /> | `object` | The attributes from an Opsgenie service response. |
| <CopyableCode code="type" /> | `string` | Opsgenie service resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_opsgenie_service" /> | `SELECT` | <CopyableCode code="integration_service_id, dd_site" /> | Get a single service from the Datadog Opsgenie integration. |
| <CopyableCode code="list_opsgenie_services" /> | `SELECT` | <CopyableCode code="dd_site" /> | Get a list of all services from the Datadog Opsgenie integration. |
| <CopyableCode code="create_opsgenie_service" /> | `INSERT` | <CopyableCode code="data__data, dd_site" /> | Create a new service object in the Opsgenie integration. |
| <CopyableCode code="delete_opsgenie_service" /> | `DELETE` | <CopyableCode code="integration_service_id, dd_site" /> | Delete a single service object in the Datadog Opsgenie integration. |
| <CopyableCode code="_get_opsgenie_service" /> | `EXEC` | <CopyableCode code="integration_service_id, dd_site" /> | Get a single service from the Datadog Opsgenie integration. |
| <CopyableCode code="_list_opsgenie_services" /> | `EXEC` | <CopyableCode code="dd_site" /> | Get a list of all services from the Datadog Opsgenie integration. |
| <CopyableCode code="update_opsgenie_service" /> | `EXEC` | <CopyableCode code="integration_service_id, data__data, dd_site" /> | Update a single service object in the Datadog Opsgenie integration. |
