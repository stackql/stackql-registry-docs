---
title: notebook_runtime_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - notebook_runtime_templates
  - aiplatform
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

Creates, updates, deletes, gets or lists a <code>notebook_runtime_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notebook_runtime_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.notebook_runtime_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the NotebookRuntimeTemplate. |
| <CopyableCode code="description" /> | `string` | The description of the NotebookRuntimeTemplate. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this NotebookRuntimeTemplate was created. |
| <CopyableCode code="dataPersistentDiskSpec" /> | `object` | Represents the spec of persistent disk options. |
| <CopyableCode code="displayName" /> | `string` | Required. The display name of the NotebookRuntimeTemplate. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="etag" /> | `string` | Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="eucConfig" /> | `object` | The euc configuration of NotebookRuntimeTemplate. |
| <CopyableCode code="idleShutdownConfig" /> | `object` | The idle shutdown configuration of NotebookRuntimeTemplate, which contains the idle_timeout as required field. |
| <CopyableCode code="isDefault" /> | `boolean` | Output only. The default template to use if not specified. |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize the NotebookRuntimeTemplates. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| <CopyableCode code="machineSpec" /> | `object` | Specification of a single machine. |
| <CopyableCode code="networkSpec" /> | `object` | Network spec. |
| <CopyableCode code="networkTags" /> | `array` | Optional. The Compute Engine tags to add to runtime (see [Tagging instances](https://cloud.google.com/vpc/docs/add-remove-network-tags)). |
| <CopyableCode code="notebookRuntimeType" /> | `string` | Optional. Immutable. The type of the notebook runtime template. |
| <CopyableCode code="serviceAccount" /> | `string` | The service account that the runtime workload runs as. You can use any service account within the same project, but you must have the service account user permission to use the instance. If not specified, the [Compute Engine default service account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used. |
| <CopyableCode code="shieldedVmConfig" /> | `object` | A set of Shielded Instance options. See [Images using supported Shielded VM features](https://cloud.google.com/compute/docs/instances/modifying-shielded-vm). |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this NotebookRuntimeTemplate was most recently updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, notebookRuntimeTemplatesId, projectsId" /> | Gets a NotebookRuntimeTemplate. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists NotebookRuntimeTemplates in a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a NotebookRuntimeTemplate. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, notebookRuntimeTemplatesId, projectsId" /> | Deletes a NotebookRuntimeTemplate. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, notebookRuntimeTemplatesId, projectsId" /> | Updates a NotebookRuntimeTemplate. |

## `SELECT` examples

Lists NotebookRuntimeTemplates in a Location.

```sql
SELECT
name,
description,
createTime,
dataPersistentDiskSpec,
displayName,
encryptionSpec,
etag,
eucConfig,
idleShutdownConfig,
isDefault,
labels,
machineSpec,
networkSpec,
networkTags,
notebookRuntimeType,
serviceAccount,
shieldedVmConfig,
updateTime
FROM google.aiplatform.notebook_runtime_templates
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>notebook_runtime_templates</code> resource.

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
INSERT INTO google.aiplatform.notebook_runtime_templates (
locationsId,
projectsId,
machineSpec,
notebookRuntimeType,
shieldedVmConfig,
name,
description,
displayName,
labels,
eucConfig,
encryptionSpec,
serviceAccount,
networkSpec,
idleShutdownConfig,
etag,
dataPersistentDiskSpec,
networkTags
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ machineSpec }}',
'{{ notebookRuntimeType }}',
'{{ shieldedVmConfig }}',
'{{ name }}',
'{{ description }}',
'{{ displayName }}',
'{{ labels }}',
'{{ eucConfig }}',
'{{ encryptionSpec }}',
'{{ serviceAccount }}',
'{{ networkSpec }}',
'{{ idleShutdownConfig }}',
'{{ etag }}',
'{{ dataPersistentDiskSpec }}',
'{{ networkTags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
machineSpec:
  acceleratorCount: integer
  reservationAffinity:
    key: string
    reservationAffinityType: string
    values:
      - type: string
  tpuTopology: string
  acceleratorType: string
  machineType: string
notebookRuntimeType: string
shieldedVmConfig:
  enableSecureBoot: boolean
name: string
description: string
displayName: string
labels: object
eucConfig:
  eucDisabled: boolean
  bypassActasCheck: boolean
encryptionSpec:
  kmsKeyName: string
isDefault: boolean
serviceAccount: string
networkSpec:
  subnetwork: string
  enableInternetAccess: boolean
  network: string
createTime: string
idleShutdownConfig:
  idleTimeout: string
  idleShutdownDisabled: boolean
etag: string
dataPersistentDiskSpec:
  diskType: string
  diskSizeGb: string
updateTime: string
networkTags:
  - type: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>notebook_runtime_templates</code> resource.

```sql
/*+ update */
UPDATE google.aiplatform.notebook_runtime_templates
SET 
machineSpec = '{{ machineSpec }}',
notebookRuntimeType = '{{ notebookRuntimeType }}',
shieldedVmConfig = '{{ shieldedVmConfig }}',
name = '{{ name }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
labels = '{{ labels }}',
eucConfig = '{{ eucConfig }}',
encryptionSpec = '{{ encryptionSpec }}',
serviceAccount = '{{ serviceAccount }}',
networkSpec = '{{ networkSpec }}',
idleShutdownConfig = '{{ idleShutdownConfig }}',
etag = '{{ etag }}',
dataPersistentDiskSpec = '{{ dataPersistentDiskSpec }}',
networkTags = '{{ networkTags }}'
WHERE 
locationsId = '{{ locationsId }}'
AND notebookRuntimeTemplatesId = '{{ notebookRuntimeTemplatesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>notebook_runtime_templates</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.notebook_runtime_templates
WHERE locationsId = '{{ locationsId }}'
AND notebookRuntimeTemplatesId = '{{ notebookRuntimeTemplatesId }}'
AND projectsId = '{{ projectsId }}';
```
