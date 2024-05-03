---
title: incident_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - incident_integrations
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
<tr><td><b>Name</b></td><td><code>incident_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.incidents.incident_integrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The incident integration metadata's ID. |
| <CopyableCode code="attributes" /> | `object` | Incident integration metadata's attributes for a create request. |
| <CopyableCode code="relationships" /> | `object` | The incident's integration relationships from a response. |
| <CopyableCode code="type" /> | `string` | Integration metadata resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_incident_integration" /> | `SELECT` | <CopyableCode code="incident_id, integration_metadata_id, dd_site" /> | Get incident integration metadata details. |
| <CopyableCode code="list_incident_integrations" /> | `SELECT` | <CopyableCode code="incident_id, dd_site" /> | Get all integration metadata for an incident. |
| <CopyableCode code="create_incident_integration" /> | `INSERT` | <CopyableCode code="incident_id, data__data, dd_site" /> | Create an incident integration metadata. |
| <CopyableCode code="delete_incident_integration" /> | `DELETE` | <CopyableCode code="incident_id, integration_metadata_id, dd_site" /> | Delete an incident integration metadata. |
| <CopyableCode code="_get_incident_integration" /> | `EXEC` | <CopyableCode code="incident_id, integration_metadata_id, dd_site" /> | Get incident integration metadata details. |
| <CopyableCode code="_list_incident_integrations" /> | `EXEC` | <CopyableCode code="incident_id, dd_site" /> | Get all integration metadata for an incident. |
| <CopyableCode code="update_incident_integration" /> | `EXEC` | <CopyableCode code="incident_id, integration_metadata_id, data__data, dd_site" /> | Update an existing incident integration metadata. |
