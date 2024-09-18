---
title: targets
hide_title: false
hide_table_of_contents: false
keywords:
  - targets
  - clouddeploy
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

Creates, updates, deletes, gets or lists a <code>targets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.clouddeploy.targets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Optional. Name of the `Target`. Format is `projects/{project}/locations/{location}/targets/{target}`. The `target` component must match `[a-z]([a-z0-9-]{0,61}[a-z0-9])?` |
| <CopyableCode code="description" /> | `string` | Optional. Description of the `Target`. Max length is 255 characters. |
| <CopyableCode code="annotations" /> | `object` | Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. |
| <CopyableCode code="anthosCluster" /> | `object` | Information specifying an Anthos Cluster. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time at which the `Target` was created. |
| <CopyableCode code="customTarget" /> | `object` | Information specifying a Custom Target. |
| <CopyableCode code="deployParameters" /> | `object` | Optional. The deploy parameters to use for this target. |
| <CopyableCode code="etag" /> | `string` | Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="executionConfigs" /> | `array` | Configurations for all execution that relates to this `Target`. Each `ExecutionEnvironmentUsage` value may only be used in a single configuration; using the same value multiple times is an error. When one or more configurations are specified, they must include the `RENDER` and `DEPLOY` `ExecutionEnvironmentUsage` values. When no configurations are specified, execution will use the default specified in `DefaultPool`. |
| <CopyableCode code="gke" /> | `object` | Information specifying a GKE Cluster. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be <= 128 bytes. |
| <CopyableCode code="multiTarget" /> | `object` | Information specifying a multiTarget. |
| <CopyableCode code="requireApproval" /> | `boolean` | Optional. Whether or not the `Target` requires approval. |
| <CopyableCode code="run" /> | `object` | Information specifying where to deploy a Cloud Run Service. |
| <CopyableCode code="targetId" /> | `string` | Output only. Resource id of the `Target`. |
| <CopyableCode code="uid" /> | `string` | Output only. Unique identifier of the `Target`. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Most recent time at which the `Target` was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, targetsId" /> | Gets details of a single Target. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Targets in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Target in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, targetsId" /> | Deletes a single Target. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, targetsId" /> | Updates the parameters of a single Target. |

## `SELECT` examples

Lists Targets in a given project and location.

```sql
SELECT
name,
description,
annotations,
anthosCluster,
createTime,
customTarget,
deployParameters,
etag,
executionConfigs,
gke,
labels,
multiTarget,
requireApproval,
run,
targetId,
uid,
updateTime
FROM google.clouddeploy.targets
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>targets</code> resource.

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
INSERT INTO google.clouddeploy.targets (
locationsId,
projectsId,
name,
description,
annotations,
labels,
requireApproval,
gke,
anthosCluster,
run,
multiTarget,
customTarget,
etag,
executionConfigs,
deployParameters
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ annotations }}',
'{{ labels }}',
true|false,
'{{ gke }}',
'{{ anthosCluster }}',
'{{ run }}',
'{{ multiTarget }}',
'{{ customTarget }}',
'{{ etag }}',
'{{ executionConfigs }}',
'{{ deployParameters }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
targetId: string
uid: string
description: string
annotations: object
labels: object
requireApproval: boolean
createTime: string
updateTime: string
gke:
  cluster: string
  internalIp: boolean
  proxyUrl: string
anthosCluster:
  membership: string
run:
  location: string
multiTarget:
  targetIds:
    - type: string
customTarget:
  customTargetType: string
etag: string
executionConfigs:
  - usages:
      - type: string
        enumDescriptions: string
        enum: string
    defaultPool:
      serviceAccount: string
      artifactStorage: string
    privatePool:
      workerPool: string
      serviceAccount: string
      artifactStorage: string
    workerPool: string
    serviceAccount: string
    artifactStorage: string
    executionTimeout: string
    verbose: boolean
deployParameters: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>targets</code> resource.

```sql
/*+ update */
UPDATE google.clouddeploy.targets
SET 
name = '{{ name }}',
description = '{{ description }}',
annotations = '{{ annotations }}',
labels = '{{ labels }}',
requireApproval = true|false,
gke = '{{ gke }}',
anthosCluster = '{{ anthosCluster }}',
run = '{{ run }}',
multiTarget = '{{ multiTarget }}',
customTarget = '{{ customTarget }}',
etag = '{{ etag }}',
executionConfigs = '{{ executionConfigs }}',
deployParameters = '{{ deployParameters }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND targetsId = '{{ targetsId }}';
```

## `DELETE` example

Deletes the specified <code>targets</code> resource.

```sql
/*+ delete */
DELETE FROM google.clouddeploy.targets
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND targetsId = '{{ targetsId }}';
```
