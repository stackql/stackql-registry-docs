---
title: broker_authentications
hide_title: false
hide_table_of_contents: false
keywords:
  - broker_authentications
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

Creates, updates, deletes, gets or lists a <code>broker_authentications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>broker_authentications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iotoperations.broker_authentications" /></td></tr>
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
| <CopyableCode code="instanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | Extended location is an extension of Azure locations. They provide a way to use their Azure ARC enabled Kubernetes clusters as target locations for deploying Azure services instances. |
| <CopyableCode code="properties" /> | `object` | BrokerAuthentication Resource properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authenticationName, brokerName, instanceName, resourceGroupName, subscriptionId" /> | Get a BrokerAuthenticationResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="brokerName, instanceName, resourceGroupName, subscriptionId" /> | List BrokerAuthenticationResource resources by BrokerResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authenticationName, brokerName, instanceName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a BrokerAuthenticationResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authenticationName, brokerName, instanceName, resourceGroupName, subscriptionId" /> | Delete a BrokerAuthenticationResource |

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
instanceName,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure.iotoperations.vw_broker_authentications
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
FROM azure.iotoperations.broker_authentications
WHERE brokerName = '{{ brokerName }}'
AND instanceName = '{{ instanceName }}'
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
INSERT INTO azure.iotoperations.broker_authentications (
authenticationName,
brokerName,
instanceName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
properties,
extendedLocation
)
SELECT 
'{{ authenticationName }}',
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
        - name: authenticationMethods
          value:
            - - name: method
                value: []
              - name: customSettings
                value:
                  - name: auth
                    value:
                      - name: x509
                        value:
                          - name: secretRef
                            value: string
                  - name: caCertConfigMap
                    value: string
                  - name: endpoint
                    value: string
                  - name: headers
                    value: object
              - name: serviceAccountTokenSettings
                value:
                  - name: audiences
                    value:
                      - string
              - name: x509Settings
                value:
                  - name: authorizationAttributes
                    value: object
                  - name: trustedClientCaCert
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

Deletes the specified <code>broker_authentications</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iotoperations.broker_authentications
WHERE authenticationName = '{{ authenticationName }}'
AND brokerName = '{{ brokerName }}'
AND instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
