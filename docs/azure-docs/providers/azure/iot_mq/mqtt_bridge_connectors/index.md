---
title: mqtt_bridge_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - mqtt_bridge_connectors
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

Creates, updates, deletes, gets or lists a <code>mqtt_bridge_connectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mqtt_bridge_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_mq.mqtt_bridge_connectors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_mqtt_bridge_connectors', value: 'view', },
        { label: 'mqtt_bridge_connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="bridge_instances" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_id_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="image" /> | `text` | field from the `properties` object |
| <CopyableCode code="local_broker_connection" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="log_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="mqName" /> | `text` | field from the `properties` object |
| <CopyableCode code="mqttBridgeConnectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_tolerations" /> | `text` | field from the `properties` object |
| <CopyableCode code="protocol" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="remote_broker_connection" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation properties |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | MqttBridgeConnector Properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId" /> | Get a MqttBridgeConnectorResource |
| <CopyableCode code="list_by_mq_resource" /> | `SELECT` | <CopyableCode code="mqName, resourceGroupName, subscriptionId" /> | List MqttBridgeConnectorResource resources by MqResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a MqttBridgeConnectorResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId" /> | Delete a MqttBridgeConnectorResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId" /> | Update a MqttBridgeConnectorResource |

## `SELECT` examples

List MqttBridgeConnectorResource resources by MqResource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_mqtt_bridge_connectors', value: 'view', },
        { label: 'mqtt_bridge_connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
bridge_instances,
client_id_prefix,
extended_location,
image,
local_broker_connection,
location,
log_level,
mqName,
mqttBridgeConnectorName,
node_tolerations,
protocol,
provisioning_state,
remote_broker_connection,
resourceGroupName,
subscriptionId,
tags
FROM azure.iot_mq.vw_mqtt_bridge_connectors
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
FROM azure.iot_mq.mqtt_bridge_connectors
WHERE mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>mqtt_bridge_connectors</code> resource.

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
INSERT INTO azure.iot_mq.mqtt_bridge_connectors (
mqName,
mqttBridgeConnectorName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
properties,
extendedLocation,
tags,
location
)
SELECT 
'{{ mqName }}',
'{{ mqttBridgeConnectorName }}',
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
        - name: bridgeInstances
          value: integer
        - name: clientIdPrefix
          value: string
        - name: image
          value:
            - name: pullPolicy
              value: string
            - name: pullSecrets
              value: string
            - name: repository
              value: string
            - name: tag
              value: string
        - name: localBrokerConnection
          value:
            - name: authentication
              value:
                - name: kubernetes
                  value:
                    - name: secretPath
                      value: string
                    - name: serviceAccountTokenName
                      value: string
            - name: endpoint
              value: string
            - name: tls
              value:
                - name: tlsEnabled
                  value: boolean
                - name: trustedCaCertificateConfigMap
                  value: string
        - name: logLevel
          value: string
        - name: nodeTolerations
          value:
            - name: effect
              value: string
            - name: key
              value: string
            - name: operator
              value: string
            - name: value
              value: string
        - name: protocol
          value: []
        - name: provisioningState
          value: []
        - name: remoteBrokerConnection
          value:
            - name: authentication
              value:
                - name: x509
                  value:
                    - name: keyVault
                      value:
                        - name: vault
                          value:
                            - name: credentials
                              value:
                                - name: servicePrincipalLocalSecretName
                                  value: string
                            - name: directoryId
                              value: string
                            - name: name
                              value: string
                        - name: vaultCaChainSecret
                          value:
                            - name: name
                              value: string
                            - name: version
                              value: string
                    - name: secretName
                      value: string
                - name: systemAssignedManagedIdentity
                  value:
                    - name: audience
                      value: string
                    - name: extensionName
                      value: string
            - name: endpoint
              value: string
            - name: protocol
              value: string
            - name: tls
              value:
                - name: tlsEnabled
                  value: boolean
                - name: trustedCaCertificateConfigMap
                  value: string
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

Updates a <code>mqtt_bridge_connectors</code> resource.

```sql
/*+ update */
UPDATE azure.iot_mq.mqtt_bridge_connectors
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
mqName = '{{ mqName }}'
AND mqttBridgeConnectorName = '{{ mqttBridgeConnectorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>mqtt_bridge_connectors</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iot_mq.mqtt_bridge_connectors
WHERE mqName = '{{ mqName }}'
AND mqttBridgeConnectorName = '{{ mqttBridgeConnectorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
