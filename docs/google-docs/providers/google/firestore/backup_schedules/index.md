---
title: backup_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_schedules
  - firestore
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firestore.backup_schedules" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupSchedulesId, databasesId, projectsId" /> | Gets information about a backup schedule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="databasesId, projectsId" /> | List backup schedules. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="databasesId, projectsId" /> | Creates a backup schedule on a database. At most two backup schedules can be configured on a database, one daily backup schedule and one weekly backup schedule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupSchedulesId, databasesId, projectsId" /> | Deletes a backup schedule. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="backupSchedulesId, databasesId, projectsId" /> | Updates a backup schedule. |
