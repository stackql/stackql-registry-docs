---
title: agent_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pools
  - nexus
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.agent_pools" /></td></tr>
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
| <CopyableCode code="administrator_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="agentPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="agent_options" /> | `text` | field from the `properties` object |
| <CopyableCode code="attached_network_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_zones" /> | `text` | field from the `properties` object |
| <CopyableCode code="count" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="kubernetesClusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kubernetes_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="labels" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="taints" /> | `text` | field from the `properties` object |
| <CopyableCode code="upgrade_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_sku_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` |  |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="agentPoolName, kubernetesClusterName, resourceGroupName, subscriptionId" /> | Get properties of the provided Kubernetes cluster agent pool. |
| <CopyableCode code="list_by_kubernetes_cluster" /> | `SELECT` | <CopyableCode code="kubernetesClusterName, resourceGroupName, subscriptionId" /> | Get a list of agent pools for the provided Kubernetes cluster. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="agentPoolName, kubernetesClusterName, resourceGroupName, subscriptionId, data__properties" /> | Create a new Kubernetes cluster agent pool or update the properties of the existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="agentPoolName, kubernetesClusterName, resourceGroupName, subscriptionId" /> | Delete the provided Kubernetes cluster agent pool. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="agentPoolName, kubernetesClusterName, resourceGroupName, subscriptionId" /> | Patch the properties of the provided Kubernetes cluster agent pool, or update the tags associated with the Kubernetes cluster agent pool. Properties and tag updates can be done independently. |

## `SELECT` examples

Get a list of agent pools for the provided Kubernetes cluster.

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
administrator_configuration,
agentPoolName,
agent_options,
attached_network_configuration,
availability_zones,
count,
detailed_status,
detailed_status_message,
extended_location,
kubernetesClusterName,
kubernetes_version,
labels,
location,
mode,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
taints,
upgrade_settings,
vm_sku_name
FROM azure.nexus.vw_agent_pools
WHERE kubernetesClusterName = '{{ kubernetesClusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure.nexus.agent_pools
WHERE kubernetesClusterName = '{{ kubernetesClusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
INSERT INTO azure.nexus.agent_pools (
agentPoolName,
kubernetesClusterName,
resourceGroupName,
subscriptionId,
data__properties,
extendedLocation,
properties,
tags,
location
)
SELECT 
'{{ agentPoolName }}',
'{{ kubernetesClusterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ extendedLocation }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: string
    - name: properties
      value:
        - name: administratorConfiguration
          value:
            - name: adminUsername
              value: string
            - name: sshPublicKeys
              value:
                - - name: keyData
                    value: string
        - name: agentOptions
          value:
            - name: hugepagesCount
              value: integer
            - name: hugepagesSize
              value: string
        - name: attachedNetworkConfiguration
          value:
            - name: l2Networks
              value:
                - - name: networkId
                    value: string
                  - name: pluginType
                    value: string
            - name: l3Networks
              value:
                - - name: ipamEnabled
                    value: string
                  - name: networkId
                    value: string
                  - name: pluginType
                    value: string
            - name: trunkedNetworks
              value:
                - - name: networkId
                    value: string
                  - name: pluginType
                    value: string
        - name: availabilityZones
          value:
            - string
        - name: count
          value: integer
        - name: detailedStatus
          value: string
        - name: detailedStatusMessage
          value: string
        - name: kubernetesVersion
          value: string
        - name: labels
          value:
            - - name: key
                value: string
              - name: value
                value: string
        - name: mode
          value: string
        - name: provisioningState
          value: string
        - name: taints
          value:
            - - name: key
                value: string
              - name: value
                value: string
        - name: upgradeSettings
          value:
            - name: drainTimeout
              value: integer
            - name: maxSurge
              value: string
            - name: maxUnavailable
              value: string
        - name: vmSkuName
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>agent_pools</code> resource.

```sql
/*+ update */
UPDATE azure.nexus.agent_pools
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
agentPoolName = '{{ agentPoolName }}'
AND kubernetesClusterName = '{{ kubernetesClusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>agent_pools</code> resource.

```sql
/*+ delete */
DELETE FROM azure.nexus.agent_pools
WHERE agentPoolName = '{{ agentPoolName }}'
AND kubernetesClusterName = '{{ kubernetesClusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
