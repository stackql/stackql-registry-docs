---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
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
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.firestore.backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The unique resource name of the Backup. Format is `projects/&#123;project&#125;/locations/&#123;location&#125;/backups/&#123;backup&#125;`. |
| <CopyableCode code="database" /> | `string` | Output only. Name of the Firestore database that the backup is from. Format is `projects/&#123;project&#125;/databases/&#123;database&#125;`. |
| <CopyableCode code="databaseUid" /> | `string` | Output only. The system-generated UUID4 for the Firestore database that the backup is from. |
| <CopyableCode code="expireTime" /> | `string` | Output only. The timestamp at which this backup expires. |
| <CopyableCode code="snapshotTime" /> | `string` | Output only. The backup contains an externally consistent copy of the database at this time. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the backup. |
| <CopyableCode code="stats" /> | `object` | Backup specific statistics. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupsId, locationsId, projectsId" /> | Gets information about a backup. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all the backups. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupsId, locationsId, projectsId" /> | Deletes a backup. |
