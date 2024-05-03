---
title: incident_services
hide_title: false
hide_table_of_contents: false
keywords:
  - incident_services
  - incidents
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
<tr><td><b>Name</b></td><td><code>incident_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.incidents.incident_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The incident service's ID. |
| <CopyableCode code="attributes" /> | `object` | The incident service's attributes from a response. |
| <CopyableCode code="relationships" /> | `object` | The incident service's relationships. |
| <CopyableCode code="type" /> | `string` | Incident service resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_incident_service" /> | `SELECT` | <CopyableCode code="service_id, dd_site" /> | Get details of an incident service. If the `include[users]` query parameter is provided,<br />the included attribute will contain the users related to these incident services. |
| <CopyableCode code="list_incident_services" /> | `SELECT` | <CopyableCode code="dd_site" /> | Get all incident services uploaded for the requesting user's organization. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these incident services. |
| <CopyableCode code="create_incident_service" /> | `INSERT` | <CopyableCode code="data__data, dd_site" /> | Creates a new incident service. |
| <CopyableCode code="delete_incident_service" /> | `DELETE` | <CopyableCode code="service_id, dd_site" /> | Deletes an existing incident service. |
| <CopyableCode code="_get_incident_service" /> | `EXEC` | <CopyableCode code="service_id, dd_site" /> | Get details of an incident service. If the `include[users]` query parameter is provided,<br />the included attribute will contain the users related to these incident services. |
| <CopyableCode code="_list_incident_services" /> | `EXEC` | <CopyableCode code="dd_site" /> | Get all incident services uploaded for the requesting user's organization. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these incident services. |
| <CopyableCode code="update_incident_service" /> | `EXEC` | <CopyableCode code="service_id, data__data, dd_site" /> | Updates an existing incident service. Only provide the attributes which should be updated as this request is a partial update. |
