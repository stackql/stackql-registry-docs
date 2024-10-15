---
title: broker_authorizations
hide_title: false
hide_table_of_contents: false
keywords:
  - broker_authorizations
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

Creates, updates, deletes, gets or lists a <code>broker_authorizations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>broker_authorizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iotoperations.broker_authorizations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_broker_authorizations', value: 'view', },
        { label: 'broker_authorizations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="authorizationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorization_policies" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | BrokerAuthorization Resource properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authorizationName, brokerName, instanceName, resourceGroupName, subscriptionId" /> | Get a BrokerAuthorizationResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="brokerName, instanceName, resourceGroupName, subscriptionId" /> | List BrokerAuthorizationResource resources by BrokerResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authorizationName, brokerName, instanceName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a BrokerAuthorizationResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authorizationName, brokerName, instanceName, resourceGroupName, subscriptionId" /> | Delete a BrokerAuthorizationResource |

## `SELECT` examples

List BrokerAuthorizationResource resources by BrokerResource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_broker_authorizations', value: 'view', },
        { label: 'broker_authorizations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
authorizationName,
authorization_policies,
brokerName,
extended_location,
instanceName,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure.iotoperations.vw_broker_authorizations
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
FROM azure.iotoperations.broker_authorizations
WHERE brokerName = '{{ brokerName }}'
AND instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>broker_authorizations</code> resource.

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
INSERT INTO azure.iotoperations.broker_authorizations (
authorizationName,
brokerName,
instanceName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
properties,
extendedLocation
)
SELECT 
'{{ authorizationName }}',
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
        - name: authorizationPolicies
          value:
            - name: cache
              value: string
            - name: rules
              value:
                - - name: brokerResources
                    value:
                      - - name: method
                          value: []
                        - name: clientIds
                          value:
                            - string
                        - name: topics
                          value:
                            - string
                  - name: principals
                    value:
                      - name: attributes
                        value:
                          - object
                      - name: clientIds
                        value:
                          - string
                      - name: usernames
                        value:
                          - string
                  - name: stateStoreResources
                    value:
                      - - name: keyType
                          value: []
                        - name: keys
                          value:
                            - string
                        - name: method
                          value: []
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

Deletes the specified <code>broker_authorizations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iotoperations.broker_authorizations
WHERE authorizationName = '{{ authorizationName }}'
AND brokerName = '{{ brokerName }}'
AND instanceName = '{{ instanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
