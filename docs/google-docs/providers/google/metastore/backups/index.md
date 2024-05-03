---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - metastore
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.metastore.backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The relative resource name of the backup, in the following form:projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/services/&#123;service_id&#125;/backups/&#123;backup_id&#125; |
| <CopyableCode code="description" /> | `string` | The description of the backup. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the backup was started. |
| <CopyableCode code="endTime" /> | `string` | Output only. The time when the backup finished creating. |
| <CopyableCode code="restoringServices" /> | `array` | Output only. Services that are restoring from the backup. |
| <CopyableCode code="serviceRevision" /> | `object` | A managed metastore service that serves metadata queries. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the backup. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupsId, locationsId, projectsId, servicesId" /> | Gets details of a single backup. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Lists backups in a service. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Creates a new backup in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupsId, locationsId, projectsId, servicesId" /> | Deletes a single backup. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Lists backups in a service. |
