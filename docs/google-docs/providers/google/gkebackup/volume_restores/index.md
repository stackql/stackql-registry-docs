---
title: volume_restores
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_restores
  - gkebackup
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
<tr><td><b>Name</b></td><td><code>volume_restores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.gkebackup.volume_restores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Full name of the VolumeRestore resource. Format: `projects/*/locations/*/restorePlans/*/restores/*/volumeRestores/*` |
| <CopyableCode code="completeTime" /> | `string` | Output only. The timestamp when the associated underlying volume restoration completed. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when this VolumeRestore resource was created. |
| <CopyableCode code="etag" /> | `string` | Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a volume restore from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform volume restore updates in order to avoid race conditions. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of this VolumeRestore. |
| <CopyableCode code="stateMessage" /> | `string` | Output only. A human readable message explaining why the VolumeRestore is in its current state. |
| <CopyableCode code="targetPvc" /> | `object` | A reference to a namespaced resource in Kubernetes. |
| <CopyableCode code="uid" /> | `string` | Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when this VolumeRestore resource was last updated. |
| <CopyableCode code="volumeBackup" /> | `string` | Output only. The full name of the VolumeBackup from which the volume will be restored. Format: `projects/*/locations/*/backupPlans/*/backups/*/volumeBackups/*`. |
| <CopyableCode code="volumeHandle" /> | `string` | Output only. A storage system-specific opaque handler to the underlying volume created for the target PVC from the volume backup. |
| <CopyableCode code="volumeType" /> | `string` | Output only. The type of volume provisioned |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, restorePlansId, restoresId, volumeRestoresId" /> | Retrieve the details of a single VolumeRestore. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, restorePlansId, restoresId" /> | Lists the VolumeRestores for a given Restore. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, restorePlansId, restoresId" /> | Lists the VolumeRestores for a given Restore. |
