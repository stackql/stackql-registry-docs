---
title: deployment_resource_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_resource_pools
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

Creates, updates, deletes, gets or lists a <code>deployment_resource_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment_resource_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.deployment_resource_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the DeploymentResourcePool. Format: `projects/{project}/locations/{location}/deploymentResourcePools/{deployment_resource_pool}` |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this DeploymentResourcePool was created. |
| <CopyableCode code="dedicatedResources" /> | `object` | A description of resources that are dedicated to a DeployedModel, and that need a higher degree of manual configuration. |
| <CopyableCode code="disableContainerLogging" /> | `boolean` | If the DeploymentResourcePool is deployed with custom-trained Models or AutoML Tabular Models, the container(s) of the DeploymentResourcePool will send `stderr` and `stdout` streams to Cloud Logging by default. Please note that the logs incur cost, which are subject to [Cloud Logging pricing](https://cloud.google.com/logging/pricing). User can disable container logging by setting this flag to true. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="serviceAccount" /> | `string` | The service account that the DeploymentResourcePool's container(s) run as. Specify the email address of the service account. If this service account is not specified, the container(s) run as a service account that doesn't have access to the resource project. Users deploying the Models to this DeploymentResourcePool must have the `iam.serviceAccounts.actAs` permission on this service account. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deploymentResourcePoolsId, locationsId, projectsId" /> | Get a DeploymentResourcePool. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List DeploymentResourcePools in a location. |
| <CopyableCode code="query_deployed_models" /> | `SELECT` | <CopyableCode code="deploymentResourcePoolsId, locationsId, projectsId" /> | List DeployedModels that have been deployed on this DeploymentResourcePool. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a DeploymentResourcePool. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deploymentResourcePoolsId, locationsId, projectsId" /> | Delete a DeploymentResourcePool. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="deploymentResourcePoolsId, locationsId, projectsId" /> | Update a DeploymentResourcePool. |

## `SELECT` examples

List DeploymentResourcePools in a location.

```sql
SELECT
name,
createTime,
dedicatedResources,
disableContainerLogging,
encryptionSpec,
satisfiesPzi,
satisfiesPzs,
serviceAccount
FROM google.aiplatform.deployment_resource_pools
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>deployment_resource_pools</code> resource.

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
INSERT INTO google.aiplatform.deployment_resource_pools (
locationsId,
projectsId,
deploymentResourcePoolId,
deploymentResourcePool
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ deploymentResourcePoolId }}',
'{{ deploymentResourcePool }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
deploymentResourcePoolId: string
deploymentResourcePool:
  serviceAccount: string
  dedicatedResources:
    spot: boolean
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
    autoscalingMetricSpecs:
      - metricName: string
        target: integer
    minReplicaCount: integer
    maxReplicaCount: integer
  disableContainerLogging: boolean
  encryptionSpec:
    kmsKeyName: string
  createTime: string
  satisfiesPzs: boolean
  satisfiesPzi: boolean
  name: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>deployment_resource_pools</code> resource.

```sql
/*+ update */
UPDATE google.aiplatform.deployment_resource_pools
SET 
serviceAccount = '{{ serviceAccount }}',
dedicatedResources = '{{ dedicatedResources }}',
disableContainerLogging = true|false,
encryptionSpec = '{{ encryptionSpec }}',
name = '{{ name }}'
WHERE 
deploymentResourcePoolsId = '{{ deploymentResourcePoolsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>deployment_resource_pools</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.deployment_resource_pools
WHERE deploymentResourcePoolsId = '{{ deploymentResourcePoolsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
