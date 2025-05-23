---
title: nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - nodes
  - tpu
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

Creates, updates, deletes, gets or lists a <code>nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.tpu.nodes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Output only. The unique identifier for the TPU Node. |
| <CopyableCode code="name" /> | `string` | Output only. Immutable. The name of the TPU. |
| <CopyableCode code="description" /> | `string` | The user-supplied description of the TPU. Maximum of 512 characters. |
| <CopyableCode code="acceleratorConfig" /> | `object` | A TPU accelerator configuration. |
| <CopyableCode code="acceleratorType" /> | `string` | Optional. The type of hardware accelerators associated with this node. |
| <CopyableCode code="apiVersion" /> | `string` | Output only. The API version that created this Node. |
| <CopyableCode code="cidrBlock" /> | `string` | The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network that is using that CIDR block. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the node was created. |
| <CopyableCode code="dataDisks" /> | `array` | The additional data disks for the Node. |
| <CopyableCode code="health" /> | `string` | The health status of the TPU node. |
| <CopyableCode code="healthDescription" /> | `string` | Output only. If this field is populated, it contains a description of why the TPU Node is unhealthy. |
| <CopyableCode code="labels" /> | `object` | Resource labels to represent user-provided metadata. |
| <CopyableCode code="metadata" /> | `object` | Custom metadata to apply to the TPU Node. Can set startup-script and shutdown-script |
| <CopyableCode code="multisliceNode" /> | `boolean` | Output only. Whether the Node belongs to a Multislice group. |
| <CopyableCode code="networkConfig" /> | `object` | Network related configurations. |
| <CopyableCode code="networkEndpoints" /> | `array` | Output only. The network endpoints where TPU workers can be accessed and sent work. It is recommended that runtime clients of the node reach out to the 0th entry in this map first. |
| <CopyableCode code="queuedResource" /> | `string` | Output only. The qualified name of the QueuedResource that requested this Node. |
| <CopyableCode code="runtimeVersion" /> | `string` | Required. The runtime version running in the Node. |
| <CopyableCode code="schedulingConfig" /> | `object` | Sets the scheduling options for this node. |
| <CopyableCode code="serviceAccount" /> | `object` | A service account. |
| <CopyableCode code="shieldedInstanceConfig" /> | `object` | A set of Shielded Instance options. |
| <CopyableCode code="state" /> | `string` | Output only. The current state for the TPU Node. |
| <CopyableCode code="symptoms" /> | `array` | Output only. The Symptoms that have occurred to the TPU Node. |
| <CopyableCode code="tags" /> | `array` | Tags to apply to the TPU Node. Tags are used to identify valid sources or targets for network firewalls. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, nodesId, projectsId" /> | Gets the details of a node. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists nodes. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a node. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, nodesId, projectsId" /> | Deletes a node. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, nodesId, projectsId" /> | Updates the configurations of a node. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="locationsId, nodesId, projectsId" /> | Starts a node. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="locationsId, nodesId, projectsId" /> | Stops a node. This operation is only available with single TPU nodes. |

## `SELECT` examples

Lists nodes.

```sql
SELECT
id,
name,
description,
acceleratorConfig,
acceleratorType,
apiVersion,
cidrBlock,
createTime,
dataDisks,
health,
healthDescription,
labels,
metadata,
multisliceNode,
networkConfig,
networkEndpoints,
queuedResource,
runtimeVersion,
schedulingConfig,
serviceAccount,
shieldedInstanceConfig,
state,
symptoms,
tags
FROM google.tpu.nodes
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>nodes</code> resource.

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
INSERT INTO google.tpu.nodes (
locationsId,
projectsId,
description,
acceleratorType,
runtimeVersion,
networkConfig,
cidrBlock,
serviceAccount,
schedulingConfig,
health,
labels,
metadata,
tags,
dataDisks,
shieldedInstanceConfig,
acceleratorConfig
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ description }}',
'{{ acceleratorType }}',
'{{ runtimeVersion }}',
'{{ networkConfig }}',
'{{ cidrBlock }}',
'{{ serviceAccount }}',
'{{ schedulingConfig }}',
'{{ health }}',
'{{ labels }}',
'{{ metadata }}',
'{{ tags }}',
'{{ dataDisks }}',
'{{ shieldedInstanceConfig }}',
'{{ acceleratorConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: description
      value: string
    - name: acceleratorType
      value: string
    - name: state
      value: string
    - name: healthDescription
      value: string
    - name: runtimeVersion
      value: string
    - name: networkConfig
      value:
        - name: network
          value: string
        - name: subnetwork
          value: string
        - name: enableExternalIps
          value: boolean
        - name: canIpForward
          value: boolean
        - name: queueCount
          value: integer
    - name: cidrBlock
      value: string
    - name: serviceAccount
      value:
        - name: email
          value: string
        - name: scope
          value:
            - string
    - name: createTime
      value: string
    - name: schedulingConfig
      value:
        - name: preemptible
          value: boolean
        - name: reserved
          value: boolean
        - name: spot
          value: boolean
    - name: networkEndpoints
      value:
        - - name: ipAddress
            value: string
          - name: port
            value: integer
          - name: accessConfig
            value:
              - name: externalIp
                value: string
    - name: health
      value: string
    - name: labels
      value: object
    - name: metadata
      value: object
    - name: tags
      value:
        - string
    - name: id
      value: string
    - name: dataDisks
      value:
        - - name: sourceDisk
            value: string
          - name: mode
            value: string
    - name: apiVersion
      value: string
    - name: symptoms
      value:
        - - name: createTime
            value: string
          - name: symptomType
            value: string
          - name: details
            value: string
          - name: workerId
            value: string
    - name: shieldedInstanceConfig
      value:
        - name: enableSecureBoot
          value: boolean
    - name: acceleratorConfig
      value:
        - name: type
          value: string
        - name: topology
          value: string
    - name: queuedResource
      value: string
    - name: multisliceNode
      value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>nodes</code> resource.

```sql
/*+ update */
UPDATE google.tpu.nodes
SET 
description = '{{ description }}',
acceleratorType = '{{ acceleratorType }}',
runtimeVersion = '{{ runtimeVersion }}',
networkConfig = '{{ networkConfig }}',
cidrBlock = '{{ cidrBlock }}',
serviceAccount = '{{ serviceAccount }}',
schedulingConfig = '{{ schedulingConfig }}',
health = '{{ health }}',
labels = '{{ labels }}',
metadata = '{{ metadata }}',
tags = '{{ tags }}',
dataDisks = '{{ dataDisks }}',
shieldedInstanceConfig = '{{ shieldedInstanceConfig }}',
acceleratorConfig = '{{ acceleratorConfig }}'
WHERE 
locationsId = '{{ locationsId }}'
AND nodesId = '{{ nodesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>nodes</code> resource.

```sql
/*+ delete */
DELETE FROM google.tpu.nodes
WHERE locationsId = '{{ locationsId }}'
AND nodesId = '{{ nodesId }}'
AND projectsId = '{{ projectsId }}';
```
