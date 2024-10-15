---
title: brokers
hide_title: false
hide_table_of_contents: false
keywords:
  - brokers
  - iot_mq
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_mq.brokers" /></td></tr>
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
| <CopyableCode code="auth_image" /> | `text` | field from the `properties` object |
| <CopyableCode code="brokerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="broker_image" /> | `text` | field from the `properties` object |
| <CopyableCode code="broker_node_tolerations" /> | `text` | field from the `properties` object |
| <CopyableCode code="cardinality" /> | `text` | field from the `properties` object |
| <CopyableCode code="diagnostics" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_backed_message_buffer_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="encrypt_internal_traffic" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_manager_image" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_manager_node_tolerations" /> | `text` | field from the `properties` object |
| <CopyableCode code="internal_certs" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="memory_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="mqName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation properties |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Broker Resource properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="brokerName, mqName, resourceGroupName, subscriptionId" /> | Get a BrokerResource |
| <CopyableCode code="list_by_mq_resource" /> | `SELECT` | <CopyableCode code="mqName, resourceGroupName, subscriptionId" /> | List BrokerResource resources by MqResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="brokerName, mqName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a BrokerResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="brokerName, mqName, resourceGroupName, subscriptionId" /> | Delete a BrokerResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="brokerName, mqName, resourceGroupName, subscriptionId" /> | Update a BrokerResource |

## `SELECT` examples

List BrokerResource resources by MqResource

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
auth_image,
brokerName,
broker_image,
broker_node_tolerations,
cardinality,
diagnostics,
disk_backed_message_buffer_settings,
encrypt_internal_traffic,
extended_location,
health_manager_image,
health_manager_node_tolerations,
internal_certs,
location,
memory_profile,
mode,
mqName,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.iot_mq.vw_brokers
WHERE mqName = '{{ mqName }}'
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
FROM azure.iot_mq.brokers
WHERE mqName = '{{ mqName }}'
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
INSERT INTO azure.iot_mq.brokers (
brokerName,
mqName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
properties,
extendedLocation,
tags,
location
)
SELECT 
'{{ brokerName }}',
'{{ mqName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__extendedLocation }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: authImage
          value:
            - name: pullPolicy
              value: string
            - name: pullSecrets
              value: string
            - name: repository
              value: string
            - name: tag
              value: string
        - name: brokerNodeTolerations
          value:
            - name: effect
              value: string
            - name: key
              value: string
            - name: operator
              value: string
            - name: value
              value: string
        - name: cardinality
          value:
            - name: backendChain
              value:
                - name: partitions
                  value: integer
                - name: redundancyFactor
                  value: integer
                - name: temporaryDiskTransferEnabled
                  value: boolean
                - name: temporaryDiskTransferHighWatermarkPercent
                  value: integer
                - name: temporaryDiskTransferLowWatermarkPercent
                  value: integer
                - name: temporaryMaxBackendMemUsagePercent
                  value: integer
                - name: temporaryResourceLimits
                  value:
                    - name: maxInflightMessages
                      value: integer
                    - name: maxInflightPatches
                      value: integer
                    - name: maxInflightPatchesPerClient
                      value: integer
                    - name: maxMessageExpirySecs
                      value: integer
                    - name: maxQueuedMessages
                      value: integer
                    - name: maxQueuedQos0Messages
                      value: integer
                    - name: maxSessionExpirySecs
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
            - name: diagnosticServiceEndpoint
              value: string
            - name: enableMetrics
              value: boolean
            - name: enableSelfCheck
              value: boolean
            - name: enableSelfTracing
              value: boolean
            - name: enableTracing
              value: boolean
            - name: logFormat
              value: string
            - name: logLevel
              value: string
            - name: maxCellMapLifetime
              value: integer
            - name: metricUpdateFrequencySeconds
              value: integer
            - name: probeImage
              value: string
            - name: selfCheckFrequencySeconds
              value: integer
            - name: selfCheckTimeoutSeconds
              value: integer
            - name: selfTraceFrequencySeconds
              value: integer
            - name: spanChannelCapacity
              value: integer
        - name: diskBackedMessageBufferSettings
          value:
            - name: ephemeralVolumeClaimSpec
              value:
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
                            value: string
                          - name: values
                            value:
                              - string
                    - name: matchLabels
                      value: object
                - name: storageClassName
                  value: string
                - name: volumeMode
                  value: string
                - name: volumeName
                  value: string
            - name: maxSize
              value: string
        - name: encryptInternalTraffic
          value: boolean
        - name: internalCerts
          value:
            - name: duration
              value: string
            - name: privateKey
              value:
                - name: algorithm
                  value: string
                - name: rotationPolicy
                  value: string
                - name: size
                  value: integer
            - name: renewBefore
              value: string
        - name: memoryProfile
          value: string
        - name: mode
          value: []
        - name: provisioningState
          value: []
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>brokers</code> resource.

```sql
/*+ update */
UPDATE azure.iot_mq.brokers
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
brokerName = '{{ brokerName }}'
AND mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>brokers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iot_mq.brokers
WHERE brokerName = '{{ brokerName }}'
AND mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
