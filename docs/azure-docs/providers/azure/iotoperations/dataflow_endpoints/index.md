---
title: dataflow_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - dataflow_endpoints
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

Creates, updates, deletes, gets or lists a <code>dataflow_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataflow_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iotoperations.dataflow_endpoints" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dataflow_endpoints', value: 'view', },
        { label: 'dataflow_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data_explorer_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_lake_storage_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataflowEndpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoint_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabric_one_lake_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="instanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kafka_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="local_storage_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="mqtt_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | Extended location is an extension of Azure locations. They provide a way to use their Azure ARC enabled Kubernetes clusters as target locations for deploying Azure services instances. |
| <CopyableCode code="properties" /> | `object` | DataflowEndpoint Resource properties. NOTE - Only one type of endpoint is supported for one Resource |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataflowEndpointName, instanceName, resourceGroupName, subscriptionId" /> | Get a DataflowEndpointResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | List DataflowEndpointResource resources by InstanceResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataflowEndpointName, instanceName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a DataflowEndpointResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataflowEndpointName, instanceName, resourceGroupName, subscriptionId" /> | Delete a DataflowEndpointResource |

## `SELECT` examples

List DataflowEndpointResource resources by InstanceResource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dataflow_endpoints', value: 'view', },
        { label: 'dataflow_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
data_explorer_settings,
data_lake_storage_settings,
dataflowEndpointName,
endpoint_type,
extended_location,
fabric_one_lake_settings,
instanceName,
kafka_settings,
local_storage_settings,
mqtt_settings,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure.iotoperations.vw_dataflow_endpoints
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
FROM azure.iotoperations.dataflow_endpoints
WHERE instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dataflow_endpoints</code> resource.

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
INSERT INTO azure.iotoperations.dataflow_endpoints (
dataflowEndpointName,
instanceName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
properties,
extendedLocation
)
SELECT 
'{{ dataflowEndpointName }}',
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
        - name: endpointType
          value: []
        - name: dataExplorerSettings
          value:
            - name: authentication
              value:
                - name: method
                  value: []
                - name: systemAssignedManagedIdentitySettings
                  value:
                    - name: audience
                      value: string
                - name: userAssignedManagedIdentitySettings
                  value:
                    - name: clientId
                      value: string
                    - name: scope
                      value: string
                    - name: tenantId
                      value: string
            - name: database
              value: string
            - name: host
              value: string
            - name: batching
              value:
                - name: latencySeconds
                  value: integer
                - name: maxMessages
                  value: integer
        - name: dataLakeStorageSettings
          value:
            - name: authentication
              value:
                - name: method
                  value: []
                - name: accessTokenSettings
                  value:
                    - name: secretRef
                      value: string
            - name: host
              value: string
        - name: fabricOneLakeSettings
          value:
            - name: authentication
              value:
                - name: method
                  value: []
            - name: names
              value:
                - name: lakehouseName
                  value: string
                - name: workspaceName
                  value: string
            - name: oneLakePathType
              value: []
            - name: host
              value: string
        - name: kafkaSettings
          value:
            - name: authentication
              value:
                - name: method
                  value: []
                - name: saslSettings
                  value:
                    - name: saslType
                      value: []
                    - name: secretRef
                      value: string
                - name: x509CertificateSettings
                  value:
                    - name: secretRef
                      value: string
            - name: consumerGroupId
              value: string
            - name: host
              value: string
            - name: batching
              value:
                - name: mode
                  value: string
                - name: latencyMs
                  value: integer
                - name: maxBytes
                  value: integer
                - name: maxMessages
                  value: integer
            - name: copyMqttProperties
              value: string
            - name: compression
              value: string
            - name: kafkaAcks
              value: string
            - name: partitionStrategy
              value: string
            - name: tls
              value:
                - name: mode
                  value: string
                - name: trustedCaCertificateConfigMapRef
                  value: string
            - name: cloudEventAttributes
              value: []
        - name: localStorageSettings
          value:
            - name: persistentVolumeClaimRef
              value: string
        - name: mqttSettings
          value:
            - name: authentication
              value:
                - name: method
                  value: []
                - name: serviceAccountTokenSettings
                  value:
                    - name: audience
                      value: string
            - name: clientIdPrefix
              value: string
            - name: host
              value: string
            - name: protocol
              value: string
            - name: keepAliveSeconds
              value: integer
            - name: retain
              value: string
            - name: maxInflightMessages
              value: integer
            - name: qos
              value: integer
            - name: sessionExpirySeconds
              value: integer
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

Deletes the specified <code>dataflow_endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iotoperations.dataflow_endpoints
WHERE dataflowEndpointName = '{{ dataflowEndpointName }}'
AND instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
