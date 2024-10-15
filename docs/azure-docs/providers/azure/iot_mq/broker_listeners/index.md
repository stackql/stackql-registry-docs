---
title: broker_listeners
hide_title: false
hide_table_of_contents: false
keywords:
  - broker_listeners
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

Creates, updates, deletes, gets or lists a <code>broker_listeners</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>broker_listeners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_mq.broker_listeners" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_broker_listeners', value: 'view', },
        { label: 'broker_listeners', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="authentication_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorization_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="brokerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="broker_ref" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="listenerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="mqName" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="port" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="tls" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation properties |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Broker Listener Resource properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="brokerName, listenerName, mqName, resourceGroupName, subscriptionId" /> | Get a BrokerListenerResource |
| <CopyableCode code="list_by_broker_resource" /> | `SELECT` | <CopyableCode code="brokerName, mqName, resourceGroupName, subscriptionId" /> | List BrokerListenerResource resources by BrokerResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="brokerName, listenerName, mqName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a BrokerListenerResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="brokerName, listenerName, mqName, resourceGroupName, subscriptionId" /> | Delete a BrokerListenerResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="brokerName, listenerName, mqName, resourceGroupName, subscriptionId" /> | Update a BrokerListenerResource |

## `SELECT` examples

List BrokerListenerResource resources by BrokerResource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_broker_listeners', value: 'view', },
        { label: 'broker_listeners', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
authentication_enabled,
authorization_enabled,
brokerName,
broker_ref,
extended_location,
listenerName,
location,
mqName,
node_port,
port,
provisioning_state,
resourceGroupName,
service_name,
service_type,
subscriptionId,
tags,
tls
FROM azure.iot_mq.vw_broker_listeners
WHERE brokerName = '{{ brokerName }}'
AND mqName = '{{ mqName }}'
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
FROM azure.iot_mq.broker_listeners
WHERE brokerName = '{{ brokerName }}'
AND mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>broker_listeners</code> resource.

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
INSERT INTO azure.iot_mq.broker_listeners (
brokerName,
listenerName,
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
'{{ listenerName }}',
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
        - name: authenticationEnabled
          value: boolean
        - name: authorizationEnabled
          value: boolean
        - name: brokerRef
          value: string
        - name: nodePort
          value: integer
        - name: port
          value: integer
        - name: serviceName
          value: string
        - name: serviceType
          value: string
        - name: tls
          value:
            - name: automatic
              value:
                - name: duration
                  value: string
                - name: issuerRef
                  value:
                    - name: group
                      value: string
                    - name: kind
                      value: string
                    - name: name
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
                - name: san
                  value:
                    - name: dns
                      value:
                        - string
                    - name: ip
                      value:
                        - string
                - name: secretName
                  value: string
                - name: secretNamespace
                  value: string
            - name: manual
              value:
                - name: secretName
                  value: string
                - name: secretNamespace
                  value: string
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

Updates a <code>broker_listeners</code> resource.

```sql
/*+ update */
UPDATE azure.iot_mq.broker_listeners
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
brokerName = '{{ brokerName }}'
AND listenerName = '{{ listenerName }}'
AND mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>broker_listeners</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iot_mq.broker_listeners
WHERE brokerName = '{{ brokerName }}'
AND listenerName = '{{ listenerName }}'
AND mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
