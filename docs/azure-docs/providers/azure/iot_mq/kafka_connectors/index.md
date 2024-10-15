---
title: kafka_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - kafka_connectors
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

Creates, updates, deletes, gets or lists a <code>kafka_connectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kafka_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_mq.kafka_connectors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_kafka_connectors', value: 'view', },
        { label: 'kafka_connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="client_id_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="image" /> | `text` | field from the `properties` object |
| <CopyableCode code="instances" /> | `text` | field from the `properties` object |
| <CopyableCode code="kafkaConnectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kafka_connection" /> | `text` | field from the `properties` object |
| <CopyableCode code="local_broker_connection" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="log_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="mqName" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_tolerations" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | KafkaConnector Properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="kafkaConnectorName, mqName, resourceGroupName, subscriptionId" /> | Get a KafkaConnectorResource |
| <CopyableCode code="list_by_mq_resource" /> | `SELECT` | <CopyableCode code="mqName, resourceGroupName, subscriptionId" /> | List KafkaConnectorResource resources by MqResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="kafkaConnectorName, mqName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a KafkaConnectorResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="kafkaConnectorName, mqName, resourceGroupName, subscriptionId" /> | Delete a KafkaConnectorResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="kafkaConnectorName, mqName, resourceGroupName, subscriptionId" /> | Update a KafkaConnectorResource |

## `SELECT` examples

List KafkaConnectorResource resources by MqResource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_kafka_connectors', value: 'view', },
        { label: 'kafka_connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
client_id_prefix,
extended_location,
image,
instances,
kafkaConnectorName,
kafka_connection,
local_broker_connection,
location,
log_level,
mqName,
node_tolerations,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.iot_mq.vw_kafka_connectors
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
FROM azure.iot_mq.kafka_connectors
WHERE mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>kafka_connectors</code> resource.

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
INSERT INTO azure.iot_mq.kafka_connectors (
kafkaConnectorName,
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
'{{ kafkaConnectorName }}',
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
        - name: instances
          value: integer
        - name: kafkaConnection
          value:
            - name: authentication
              value:
                - name: authType
                  value:
                    - name: sasl
                      value:
                        - name: saslType
                          value: []
                        - name: token
                          value:
                            - name: keyVault
                              value:
                                - name: username
                                  value: string
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
                                - name: vaultSecret
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
                    - name: x509
                      value:
                        - name: keyVault
                          value: []
                        - name: secretName
                          value: string
                - name: enabled
                  value: boolean
            - name: endpoint
              value: string
            - name: tls
              value:
                - name: tlsEnabled
                  value: boolean
                - name: trustedCaCertificateConfigMap
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

Updates a <code>kafka_connectors</code> resource.

```sql
/*+ update */
UPDATE azure.iot_mq.kafka_connectors
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
kafkaConnectorName = '{{ kafkaConnectorName }}'
AND mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>kafka_connectors</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iot_mq.kafka_connectors
WHERE kafkaConnectorName = '{{ kafkaConnectorName }}'
AND mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
