---
title: broker_listeners
hide_title: false
hide_table_of_contents: false
keywords:
  - broker_listeners
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

Creates, updates, deletes, gets or lists a <code>broker_listeners</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>broker_listeners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iotoperations.broker_listeners" /></td></tr>
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
| <CopyableCode code="brokerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="instanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="listenerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ports" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | Extended location is an extension of Azure locations. They provide a way to use their Azure ARC enabled Kubernetes clusters as target locations for deploying Azure services instances. |
| <CopyableCode code="properties" /> | `object` | Defines a Broker listener. A listener is a collection of ports on which the broker accepts connections from clients. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="brokerName, instanceName, listenerName, resourceGroupName, subscriptionId" /> | Get a BrokerListenerResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="brokerName, instanceName, resourceGroupName, subscriptionId" /> | List BrokerListenerResource resources by BrokerResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="brokerName, instanceName, listenerName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a BrokerListenerResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="brokerName, instanceName, listenerName, resourceGroupName, subscriptionId" /> | Delete a BrokerListenerResource |

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
brokerName,
extended_location,
instanceName,
listenerName,
ports,
provisioning_state,
resourceGroupName,
service_name,
service_type,
subscriptionId
FROM azure.iotoperations.vw_broker_listeners
WHERE brokerName = '{{ brokerName }}'
AND instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
properties
FROM azure.iotoperations.broker_listeners
WHERE brokerName = '{{ brokerName }}'
AND instanceName = '{{ instanceName }}'
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
INSERT INTO azure.iotoperations.broker_listeners (
brokerName,
instanceName,
listenerName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
properties,
extendedLocation
)
SELECT 
'{{ brokerName }}',
'{{ instanceName }}',
'{{ listenerName }}',
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
        - name: serviceName
          value: string
        - name: ports
          value:
            - - name: authenticationRef
                value: string
              - name: authorizationRef
                value: string
              - name: nodePort
                value: integer
              - name: port
                value: integer
              - name: protocol
                value: string
              - name: tls
                value:
                  - name: mode
                    value: []
                  - name: certManagerCertificateSpec
                    value:
                      - name: duration
                        value: string
                      - name: secretName
                        value: string
                      - name: renewBefore
                        value: string
                      - name: issuerRef
                        value:
                          - name: group
                            value: string
                          - name: kind
                            value: []
                          - name: name
                            value: string
                      - name: privateKey
                        value:
                          - name: algorithm
                            value: []
                          - name: rotationPolicy
                            value: []
                      - name: san
                        value:
                          - name: dns
                            value:
                              - string
                          - name: ip
                            value:
                              - string
                  - name: manual
                    value:
                      - name: secretRef
                        value: string
        - name: serviceType
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

Deletes the specified <code>broker_listeners</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iotoperations.broker_listeners
WHERE brokerName = '{{ brokerName }}'
AND instanceName = '{{ instanceName }}'
AND listenerName = '{{ listenerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
