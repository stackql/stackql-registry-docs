---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - file
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.file.backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the backup, in the format `projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/backups/&#123;backup_id&#125;`. |
| <CopyableCode code="description" /> | `string` | A description of the backup with 2048 characters or less. Requests with longer descriptions will be rejected. |
| <CopyableCode code="capacityGb" /> | `string` | Output only. Capacity of the source file share when the backup was created. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the backup was created. |
| <CopyableCode code="downloadBytes" /> | `string` | Output only. Amount of bytes that will be downloaded if the backup is restored. This may be different than storage bytes, since sequential backups of the same disk will share storage. |
| <CopyableCode code="kmsKey" /> | `string` | Immutable. KMS key name used for data encryption. |
| <CopyableCode code="labels" /> | `object` | Resource labels to represent user provided metadata. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="sourceFileShare" /> | `string` | Name of the file share in the source Filestore instance that the backup is created from. |
| <CopyableCode code="sourceInstance" /> | `string` | The resource name of the source Filestore instance, in the format `projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/instances/&#123;instance_id&#125;`, used to create this backup. |
| <CopyableCode code="sourceInstanceTier" /> | `string` | Output only. The service tier of the source Filestore instance that this backup is created from. |
| <CopyableCode code="state" /> | `string` | Output only. The backup state. |
| <CopyableCode code="storageBytes" /> | `string` | Output only. The size of the storage used by the backup. As backups share storage, this number is expected to change with backup creation/deletion. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupsId, locationsId, projectsId" /> | Gets the details of a specific backup. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all backups in a project for either a specified location or for all locations. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a backup. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupsId, locationsId, projectsId" /> | Deletes a backup. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists all backups in a project for either a specified location or for all locations. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="backupsId, locationsId, projectsId" /> | Updates the settings of a specific backup. |
