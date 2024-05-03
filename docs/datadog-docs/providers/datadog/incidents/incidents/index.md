---
title: incidents
hide_title: false
hide_table_of_contents: false
keywords:
  - incidents
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
<tr><td><b>Name</b></td><td><code>incidents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.incidents.incidents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The incident's ID. |
| <CopyableCode code="attributes" /> | `object` | The incident's attributes from a response. |
| <CopyableCode code="relationships" /> | `object` | The incident's relationships from a response. |
| <CopyableCode code="type" /> | `string` | Incident resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_incident" /> | `SELECT` | <CopyableCode code="incident_id, dd_site" /> | Get the details of an incident by `incident_id`. |
| <CopyableCode code="list_incidents" /> | `SELECT` | <CopyableCode code="dd_site" /> | Get all incidents for the user's organization. |
| <CopyableCode code="search_incidents" /> | `SELECT` | <CopyableCode code="query, dd_site" /> | Search for incidents matching a certain query. |
| <CopyableCode code="create_incident" /> | `INSERT` | <CopyableCode code="data__data, dd_site" /> | Create an incident. |
| <CopyableCode code="delete_incident" /> | `DELETE` | <CopyableCode code="incident_id, dd_site" /> | Deletes an existing incident from the users organization. |
| <CopyableCode code="_get_incident" /> | `EXEC` | <CopyableCode code="incident_id, dd_site" /> | Get the details of an incident by `incident_id`. |
| <CopyableCode code="_list_incidents" /> | `EXEC` | <CopyableCode code="dd_site" /> | Get all incidents for the user's organization. |
| <CopyableCode code="_search_incidents" /> | `EXEC` | <CopyableCode code="query, dd_site" /> | Search for incidents matching a certain query. |
| <CopyableCode code="update_incident" /> | `EXEC` | <CopyableCode code="incident_id, data__data, dd_site" /> | Updates an incident. Provide only the attributes that should be updated as this request is a partial update. |
