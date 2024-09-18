---
title: workstations
hide_title: false
hide_table_of_contents: false
keywords:
  - workstations
  - workstations
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>workstations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workstations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.workstations.workstations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Full name of this workstation. |
| <CopyableCode code="annotations" /> | `object` | Optional. Client-specified annotations. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when this workstation was created. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. Time when this workstation was soft-deleted. |
| <CopyableCode code="displayName" /> | `string` | Optional. Human-readable name for this workstation. |
| <CopyableCode code="env" /> | `object` | Optional. Environment variables passed to the workstation container's entrypoint. |
| <CopyableCode code="etag" /> | `string` | Optional. Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding. |
| <CopyableCode code="host" /> | `string` | Output only. Host to which clients can send HTTPS traffic that will be received by the workstation. Authorized traffic will be received to the workstation as HTTP on port 80. To send traffic to a different port, clients may prefix the host with the destination port in the format `{port}-{host}`. |
| <CopyableCode code="kmsKey" /> | `string` | Output only. The name of the Google Cloud KMS encryption key used to encrypt this workstation. The KMS key can only be configured in the WorkstationConfig. The expected format is `projects/*/locations/*/keyRings/*/cryptoKeys/*`. |
| <CopyableCode code="labels" /> | `object` | Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation and that are also propagated to the underlying Compute Engine resources. |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. Indicates whether this workstation is currently being updated to match its intended state. |
| <CopyableCode code="startTime" /> | `string` | Output only. Time when this workstation was most recently successfully started, regardless of the workstation's initial state. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the workstation. |
| <CopyableCode code="uid" /> | `string` | Output only. A system-assigned unique identifier for this workstation. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when this workstation was most recently updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, workstationClustersId, workstationConfigsId, workstationsId" /> | Returns the requested workstation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, workstationClustersId, workstationConfigsId" /> | Returns all Workstations using the specified workstation configuration. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, workstationClustersId, workstationConfigsId" /> | Creates a new workstation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, workstationClustersId, workstationConfigsId, workstationsId" /> | Deletes the specified workstation. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, workstationClustersId, workstationConfigsId, workstationsId" /> | Updates an existing workstation. |
| <CopyableCode code="generate_access_token" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, workstationClustersId, workstationConfigsId, workstationsId" /> | Returns a short-lived credential that can be used to send authenticated and authorized traffic to a workstation. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, workstationClustersId, workstationConfigsId, workstationsId" /> | Starts running a workstation so that users can connect to it. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, workstationClustersId, workstationConfigsId, workstationsId" /> | Stops running a workstation, reducing costs. |

## `SELECT` examples

Returns all Workstations using the specified workstation configuration.

```sql
SELECT
name,
annotations,
createTime,
deleteTime,
displayName,
env,
etag,
host,
kmsKey,
labels,
reconciling,
startTime,
state,
uid,
updateTime
FROM google.workstations.workstations
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND workstationClustersId = '{{ workstationClustersId }}'
AND workstationConfigsId = '{{ workstationConfigsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workstations</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.workstations.workstations (
locationsId,
projectsId,
workstationClustersId,
workstationConfigsId,
name,
displayName,
annotations,
labels,
etag,
env
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ workstationClustersId }}',
'{{ workstationConfigsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ annotations }}',
'{{ labels }}',
'{{ etag }}',
'{{ env }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
displayName: string
uid: string
reconciling: boolean
annotations: object
labels: object
createTime: string
updateTime: string
startTime: string
deleteTime: string
etag: string
state: string
host: string
env: object
kmsKey: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workstations</code> resource.

```sql
/*+ update */
UPDATE google.workstations.workstations
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
annotations = '{{ annotations }}',
labels = '{{ labels }}',
etag = '{{ etag }}',
env = '{{ env }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND workstationClustersId = '{{ workstationClustersId }}'
AND workstationConfigsId = '{{ workstationConfigsId }}'
AND workstationsId = '{{ workstationsId }}';
```

## `DELETE` example

Deletes the specified <code>workstations</code> resource.

```sql
/*+ delete */
DELETE FROM google.workstations.workstations
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND workstationClustersId = '{{ workstationClustersId }}'
AND workstationConfigsId = '{{ workstationConfigsId }}'
AND workstationsId = '{{ workstationsId }}';
```
