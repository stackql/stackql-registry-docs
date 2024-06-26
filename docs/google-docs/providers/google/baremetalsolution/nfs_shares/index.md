---
title: nfs_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - nfs_shares
  - baremetalsolution
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
<tr><td><b>Name</b></td><td><code>nfs_shares</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.baremetalsolution.nfs_shares" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Output only. An identifier for the NFS share, generated by the backend. This is the same value as nfs_share_id and will replace it in the future. |
| <CopyableCode code="name" /> | `string` | Immutable. The name of the NFS share. |
| <CopyableCode code="allowedClients" /> | `array` | List of allowed access points. |
| <CopyableCode code="labels" /> | `object` | Labels as key value pairs. |
| <CopyableCode code="nfsShareId" /> | `string` | Output only. An identifier for the NFS share, generated by the backend. This field will be deprecated in the future, use `id` instead. |
| <CopyableCode code="pod" /> | `string` | Immutable. Pod name. Pod is an independent part of infrastructure. NFSShare can only be connected to the assets (networks, instances) allocated in the same pod. |
| <CopyableCode code="requestedSizeGib" /> | `string` | The requested size, in GiB. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the NFS share. |
| <CopyableCode code="storageType" /> | `string` | Immutable. The storage type of the underlying volume. |
| <CopyableCode code="volume" /> | `string` | Output only. The underlying volume of the share. Created automatically during provisioning. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, nfsSharesId, projectsId" /> | Get details of a single NFS share. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List NFS shares. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create an NFS share. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, nfsSharesId, projectsId" /> | Delete an NFS share. The underlying volume is automatically deleted. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, nfsSharesId, projectsId" /> | Update details of a single NFS share. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | List NFS shares. |
| <CopyableCode code="rename" /> | `EXEC` | <CopyableCode code="locationsId, nfsSharesId, projectsId" /> | RenameNfsShare sets a new name for an nfsshare. Use with caution, previous names become immediately invalidated. |
