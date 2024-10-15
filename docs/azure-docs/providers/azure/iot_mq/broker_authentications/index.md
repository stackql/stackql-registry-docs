---
title: broker_authentications
hide_title: false
hide_table_of_contents: false
keywords:
  - broker_authentications
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

Creates, updates, deletes, gets or lists a <code>broker_authentications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>broker_authentications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_mq.broker_authentications" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_broker_authentications', value: 'view', },
        { label: 'broker_authentications', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="authenticationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="authentication_methods" /> | `text` | field from the `properties` object |
| <CopyableCode code="brokerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="listener_ref" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authenticationName, brokerName, mqName, resourceGroupName, subscriptionId" /> | Get a BrokerAuthenticationResource |
| <CopyableCode code="list_by_broker_resource" /> | `SELECT` | <CopyableCode code="brokerName, mqName, resourceGroupName, subscriptionId" /> | List BrokerAuthenticationResource resources by BrokerResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authenticationName, brokerName, mqName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a BrokerAuthenticationResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authenticationName, brokerName, mqName, resourceGroupName, subscriptionId" /> | Delete a BrokerAuthenticationResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="authenticationName, brokerName, mqName, resourceGroupName, subscriptionId" /> | Update a BrokerAuthenticationResource |

## `SELECT` examples

List BrokerAuthenticationResource resources by BrokerResource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_broker_authentications', value: 'view', },
        { label: 'broker_authentications', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
authenticationName,
authentication_methods,
brokerName,
extended_location,
listener_ref,
location,
mqName,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.iot_mq.vw_broker_authentications
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
FROM azure.iot_mq.broker_authentications
WHERE brokerName = '{{ brokerName }}'
AND mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>broker_authentications</code> resource.

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
INSERT INTO azure.iot_mq.broker_authentications (
authenticationName,
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
'{{ authenticationName }}',
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
        - name: authenticationMethods
          value:
            - - name: custom
                value:
                  - name: auth
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
                  - name: caCertConfigMap
                    value: string
                  - name: endpoint
                    value: string
                  - name: headers
                    value: object
              - name: sat
                value:
                  - name: audiences
                    value:
                      - string
              - name: svid
                value:
                  - name: agentSocketPath
                    value: string
                  - name: identityMaxRetry
                    value: integer
                  - name: identityWaitRetryMs
                    value: integer
              - name: usernamePassword
                value:
                  - name: keyVault
                    value: []
                  - name: secretName
                    value: string
              - name: x509
                value:
                  - name: attributes
                    value:
                      - name: secretName
                        value: string
                  - name: trustedClientCaCertConfigMap
                    value: string
        - name: listenerRef
          value:
            - string
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

Updates a <code>broker_authentications</code> resource.

```sql
/*+ update */
UPDATE azure.iot_mq.broker_authentications
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
authenticationName = '{{ authenticationName }}'
AND brokerName = '{{ brokerName }}'
AND mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>broker_authentications</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iot_mq.broker_authentications
WHERE authenticationName = '{{ authenticationName }}'
AND brokerName = '{{ brokerName }}'
AND mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
