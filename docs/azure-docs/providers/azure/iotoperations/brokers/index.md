---
title: brokers
hide_title: false
hide_table_of_contents: false
keywords:
  - brokers
  - iotoperations
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

Creates, updates, deletes, gets or lists a <code>brokers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>brokers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iotoperations.brokers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_brokers', value: 'view', },
        { label: 'brokers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="advanced" /> | `text` | field from the `properties` object |
| <CopyableCode code="brokerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="cardinality" /> | `text` | field from the `properties` object |
| <CopyableCode code="diagnostics" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_backed_message_buffer" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="generate_resource_limits" /> | `text` | field from the `properties` object |
| <CopyableCode code="instanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="memory_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | Extended location is an extension of Azure locations. They provide a way to use their Azure ARC enabled Kubernetes clusters as target locations for deploying Azure services instances. |
| <CopyableCode code="properties" /> | `object` | Broker Resource properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="brokerName, instanceName, resourceGroupName, subscriptionId" /> | Get a BrokerResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | List BrokerResource resources by InstanceResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="brokerName, instanceName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a BrokerResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="brokerName, instanceName, resourceGroupName, subscriptionId" /> | Delete a BrokerResource |

## `SELECT` examples

List BrokerResource resources by InstanceResource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_brokers', value: 'view', },
        { label: 'brokers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
advanced,
brokerName,
cardinality,
diagnostics,
disk_backed_message_buffer,
extended_location,
generate_resource_limits,
instanceName,
memory_profile,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure.iotoperations.vw_brokers
WHERE instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
properties
FROM azure.iotoperations.brokers
WHERE instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>brokers</code> resource.

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
INSERT INTO azure.iotoperations.brokers (
brokerName,
instanceName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
properties,
extendedLocation
)
SELECT 
'{{ brokerName }}',
'{{ instanceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__extendedLocation }}',
'{{ properties }}',
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
        - name: advanced
          value:
            - name: clients
              value:
                - name: maxSessionExpirySeconds
                  value: integer
                - name: maxMessageExpirySeconds
                  value: integer
                - name: maxPacketSizeBytes
                  value: integer
                - name: subscriberQueueLimit
                  value:
                    - name: length
                      value: integer
                    - name: strategy
                      value: string
                - name: maxReceiveMaximum
                  value: integer
                - name: maxKeepAliveSeconds
                  value: integer
            - name: encryptInternalTraffic
              value: string
            - name: internalCerts
              value:
                - name: duration
                  value: string
                - name: renewBefore
                  value: string
                - name: privateKey
                  value:
                    - name: algorithm
                      value: []
                    - name: rotationPolicy
                      value: []
        - name: cardinality
          value:
            - name: backendChain
              value:
                - name: partitions
                  value: integer
                - name: redundancyFactor
                  value: integer
                - name: workers
                  value: integer
            - name: frontend
              value:
                - name: replicas
                  value: integer
                - name: workers
                  value: integer
        - name: diagnostics
          value:
            - name: logs
              value:
                - name: opentelemetryExportConfig
                  value:
                    - name: otlpGrpcEndpoint
                      value: string
                    - name: intervalSeconds
                      value: integer
                    - name: level
                      value: string
                - name: level
                  value: string
            - name: metrics
              value:
                - name: opentelemetryExportConfig
                  value:
                    - name: otlpGrpcEndpoint
                      value: string
                    - name: intervalSeconds
                      value: integer
                - name: prometheusPort
                  value: integer
            - name: selfCheck
              value:
                - name: mode
                  value: string
                - name: intervalSeconds
                  value: integer
                - name: timeoutSeconds
                  value: integer
            - name: traces
              value:
                - name: mode
                  value: string
                - name: cacheSizeMegabytes
                  value: integer
                - name: selfTracing
                  value:
                    - name: mode
                      value: string
                    - name: intervalSeconds
                      value: integer
                - name: spanChannelCapacity
                  value: integer
        - name: diskBackedMessageBuffer
          value:
            - name: maxSize
              value: string
            - name: ephemeralVolumeClaimSpec
              value:
                - name: volumeName
                  value: string
                - name: volumeMode
                  value: string
                - name: storageClassName
                  value: string
                - name: accessModes
                  value:
                    - string
                - name: dataSource
                  value:
                    - name: apiGroup
                      value: string
                    - name: kind
                      value: string
                    - name: name
                      value: string
                - name: dataSourceRef
                  value:
                    - name: apiGroup
                      value: string
                    - name: kind
                      value: string
                    - name: name
                      value: string
                    - name: namespace
                      value: string
                - name: resources
                  value:
                    - name: limits
                      value: object
                    - name: requests
                      value: object
                - name: selector
                  value:
                    - name: matchExpressions
                      value:
                        - - name: key
                            value: string
                          - name: operator
                            value: []
                          - name: values
                            value:
                              - string
                    - name: matchLabels
                      value: object
        - name: generateResourceLimits
          value:
            - name: cpu
              value: string
        - name: memoryProfile
          value: string
        - name: provisioningState
          value: []
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>brokers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iotoperations.brokers
WHERE brokerName = '{{ brokerName }}'
AND instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
