---
title: agent_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pools
  - hybrid_aks
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

Creates, updates, deletes, gets or lists a <code>agent_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_aks.agent_pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_agent_pools', value: 'view', },
        { label: 'agent_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="agentPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectedClusterResourceUri" /> | `text` | field from the `properties` object |
| <CopyableCode code="count" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_auto_scaling" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="kubernetes_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_pods" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_labels" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_taints" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="vm_size" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | Extended location pointing to the underlying infrastructure |
| <CopyableCode code="properties" /> | `object` | Properties of the agent pool resource |
| <CopyableCode code="tags" /> | `object` | Resource tags |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="agentPoolName, connectedClusterResourceUri" /> | Gets the specified agent pool in the provisioned cluster |
| <CopyableCode code="list_by_provisioned_cluster" /> | `SELECT` | <CopyableCode code="connectedClusterResourceUri" /> | Gets the list of agent pools in the specified provisioned cluster |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="agentPoolName, connectedClusterResourceUri" /> | Creates or updates the agent pool in the provisioned cluster |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="agentPoolName, connectedClusterResourceUri" /> | Deletes the specified agent pool in the provisioned cluster |

## `SELECT` examples

Gets the list of agent pools in the specified provisioned cluster

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_agent_pools', value: 'view', },
        { label: 'agent_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
agentPoolName,
connectedClusterResourceUri,
count,
enable_auto_scaling,
extended_location,
kubernetes_version,
max_count,
max_pods,
min_count,
node_labels,
node_taints,
os_sku,
os_type,
provisioning_state,
status,
tags,
vm_size
FROM azure.hybrid_aks.vw_agent_pools
WHERE connectedClusterResourceUri = '{{ connectedClusterResourceUri }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
properties,
tags
FROM azure.hybrid_aks.agent_pools
WHERE connectedClusterResourceUri = '{{ connectedClusterResourceUri }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>agent_pools</code> resource.

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
INSERT INTO azure.hybrid_aks.agent_pools (
agentPoolName,
connectedClusterResourceUri,
properties,
tags,
extendedLocation
)
SELECT 
'{{ agentPoolName }}',
'{{ connectedClusterResourceUri }}',
'{{ properties }}',
'{{ tags }}',
'{{ extendedLocation }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: osType
          value: []
        - name: osSKU
          value: []
        - name: nodeLabels
          value: object
        - name: nodeTaints
          value:
            - string
        - name: maxCount
          value: integer
        - name: minCount
          value: integer
        - name: enableAutoScaling
          value: boolean
        - name: maxPods
          value: integer
        - name: count
          value: integer
        - name: vmSize
          value: string
        - name: kubernetesVersion
          value: string
        - name: provisioningState
          value: []
        - name: status
          value:
            - name: errorMessage
              value: string
            - name: readyReplicas
              value:
                - - name: count
                    value: integer
                  - name: vmSize
                    value: string
                  - name: kubernetesVersion
                    value: string
    - name: tags
      value: object
    - name: extendedLocation
      value:
        - name: type
          value: string
        - name: name
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>agent_pools</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_aks.agent_pools
WHERE agentPoolName = '{{ agentPoolName }}'
AND connectedClusterResourceUri = '{{ connectedClusterResourceUri }}';
```
