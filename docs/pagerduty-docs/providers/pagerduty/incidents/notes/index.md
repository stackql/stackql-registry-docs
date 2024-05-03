---
title: notes
hide_title: false
hide_table_of_contents: false
keywords:
  - notes
  - incidents
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
<tr><td><b>Name</b></td><td><code>notes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.incidents.notes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="channel" /> | `object` | The means by which this Note was created. Has different formats depending on type. |
| <CopyableCode code="content" /> | `string` | The note content |
| <CopyableCode code="created_at" /> | `string` | The time at which the note was submitted |
| <CopyableCode code="user" /> | `object` | The user who created a Note. If a service created this Note the `user.type` will be "bot_user_reference" and `user.summary` will list the name of the service rather than the user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_incident_notes" /> | `SELECT` | <CopyableCode code="id" /> | List existing notes for the specified incident.<br /><br />An incident represents a problem or an issue that needs to be addressed and resolved.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#incidents)<br /><br />Scoped OAuth requires: `incidents.read`<br /> |
| <CopyableCode code="create_incident_note" /> | `INSERT` | <CopyableCode code="From, id, data__note" /> | Create a new note for the specified incident.<br /><br />An incident represents a problem or an issue that needs to be addressed and resolved.<br /><br />A maximum of 2000 notes can be added to an incident.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#incidents)<br /><br />Scoped OAuth requires: `incidents.write`<br /> |
| <CopyableCode code="_list_incident_notes" /> | `EXEC` | <CopyableCode code="id" /> | List existing notes for the specified incident.<br /><br />An incident represents a problem or an issue that needs to be addressed and resolved.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#incidents)<br /><br />Scoped OAuth requires: `incidents.read`<br /> |
