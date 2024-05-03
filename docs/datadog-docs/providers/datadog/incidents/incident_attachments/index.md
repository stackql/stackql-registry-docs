---
title: incident_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - incident_attachments
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
<tr><td><b>Name</b></td><td><code>incident_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.incidents.incident_attachments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A unique identifier that represents the incident attachment. |
| <CopyableCode code="attributes" /> | `` | The attributes object for an attachment. |
| <CopyableCode code="relationships" /> | `object` | The incident attachment's relationships. |
| <CopyableCode code="type" /> | `string` | The incident attachment resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_incident_attachments" /> | `SELECT` | <CopyableCode code="incident_id, dd_site" /> | Get all attachments for a given incident. |
| <CopyableCode code="_list_incident_attachments" /> | `EXEC` | <CopyableCode code="incident_id, dd_site" /> | Get all attachments for a given incident. |
| <CopyableCode code="update_incident_attachments" /> | `EXEC` | <CopyableCode code="incident_id, data__data, dd_site" /> | The bulk update endpoint for creating, updating, and deleting attachments for a given incident. |
