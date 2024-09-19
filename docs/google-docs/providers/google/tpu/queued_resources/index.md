---
title: queued_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - queued_resources
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

Creates, updates, deletes, gets or lists a <code>queued_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queued_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.tpu.queued_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Immutable. The name of the QueuedResource. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the QueuedResource was created. |
| <CopyableCode code="guaranteed" /> | `object` | Guaranteed tier definition. |
| <CopyableCode code="queueingPolicy" /> | `object` | Defines the policy of the QueuedRequest. |
| <CopyableCode code="reservationName" /> | `string` | Optional. Name of the reservation in which the resource should be provisioned. Format: projects/{project}/locations/{zone}/reservations/{reservation} |
| <CopyableCode code="spot" /> | `object` | Spot tier definition. |
| <CopyableCode code="state" /> | `object` | QueuedResourceState defines the details of the QueuedResource request. |
| <CopyableCode code="tpu" /> | `object` | Details of the TPU resource(s) being requested. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, queuedResourcesId" /> | Gets details of a queued resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists queued resources. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a QueuedResource TPU instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, queuedResourcesId" /> | Deletes a QueuedResource TPU instance. |
| <CopyableCode code="reset" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, queuedResourcesId" /> | Resets a QueuedResource TPU instance |

## `SELECT` examples

Lists queued resources.

```sql
SELECT
name,
createTime,
guaranteed,
queueingPolicy,
reservationName,
spot,
state,
tpu
FROM google.tpu.queued_resources
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>queued_resources</code> resource.

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
INSERT INTO google.tpu.queued_resources (
locationsId,
projectsId,
tpu,
spot,
guaranteed,
queueingPolicy,
reservationName
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ tpu }}',
'{{ spot }}',
'{{ guaranteed }}',
'{{ queueingPolicy }}',
'{{ reservationName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: createTime
      value: string
    - name: tpu
      value:
        - name: nodeSpec
          value:
            - - name: parent
                value: string
              - name: nodeId
                value: string
              - name: multisliceParams
                value:
                  - name: nodeCount
                    value: integer
                  - name: nodeIdPrefix
                    value: string
              - name: node
                value:
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
    - name: spot
      value: []
    - name: guaranteed
      value:
        - name: minDuration
          value: string
    - name: queueingPolicy
      value:
        - name: validUntilDuration
          value: string
        - name: validUntilTime
          value: string
        - name: validAfterDuration
          value: string
        - name: validAfterTime
          value: string
        - name: validInterval
          value:
            - name: startTime
              value: string
            - name: endTime
              value: string
    - name: state
      value:
        - name: state
          value: string
        - name: creatingData
          value: []
        - name: acceptedData
          value: []
        - name: provisioningData
          value: []
        - name: failedData
          value:
            - name: error
              value:
                - name: code
                  value: integer
                - name: message
                  value: string
                - name: details
                  value:
                    - object
        - name: deletingData
          value: []
        - name: activeData
          value: []
        - name: suspendingData
          value: []
        - name: suspendedData
          value: []
        - name: stateInitiator
          value: string
    - name: reservationName
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>queued_resources</code> resource.

```sql
/*+ delete */
DELETE FROM google.tpu.queued_resources
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND queuedResourcesId = '{{ queuedResourcesId }}';
```
