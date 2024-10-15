---
title: jit_network_access_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - jit_network_access_policies
  - security
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

Creates, updates, deletes, gets or lists a <code>jit_network_access_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jit_network_access_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.jit_network_access_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_jit_network_access_policies', value: 'view', },
        { label: 'jit_network_access_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="ascLocation" /> | `text` | field from the `properties` object |
| <CopyableCode code="jitNetworkAccessPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Kind of the resource |
| <CopyableCode code="location" /> | `text` | Location where the resource is stored |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="requests" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="virtual_machines" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="kind" /> | `string` | Kind of the resource |
| <CopyableCode code="location" /> | `string` | Location where the resource is stored |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ascLocation, jitNetworkAccessPolicyName, resourceGroupName, subscriptionId" /> | Policies for protecting resources using Just-in-Time access control for the subscription, location |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Policies for protecting resources using Just-in-Time access control. |
| <CopyableCode code="list_by_region" /> | `SELECT` | <CopyableCode code="ascLocation, subscriptionId" /> | Policies for protecting resources using Just-in-Time access control for the subscription, location |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Policies for protecting resources using Just-in-Time access control for the subscription, location |
| <CopyableCode code="list_by_resource_group_and_region" /> | `SELECT` | <CopyableCode code="ascLocation, resourceGroupName, subscriptionId" /> | Policies for protecting resources using Just-in-Time access control for the subscription, location |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="ascLocation, jitNetworkAccessPolicyName, resourceGroupName, subscriptionId, data__properties" /> | Create a policy for protecting resources using Just-in-Time access control |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="ascLocation, jitNetworkAccessPolicyName, resourceGroupName, subscriptionId" /> | Delete a Just-in-Time access control policy. |
| <CopyableCode code="initiate" /> | `EXEC` | <CopyableCode code="ascLocation, jitNetworkAccessPolicyInitiateType, jitNetworkAccessPolicyName, resourceGroupName, subscriptionId, data__virtualMachines" /> | Initiate a JIT access from a specific Just-in-Time policy configuration. |

## `SELECT` examples

Policies for protecting resources using Just-in-Time access control.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_jit_network_access_policies', value: 'view', },
        { label: 'jit_network_access_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
ascLocation,
jitNetworkAccessPolicyName,
kind,
location,
provisioning_state,
requests,
resourceGroupName,
subscriptionId,
type,
virtual_machines
FROM azure.security.vw_jit_network_access_policies
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
kind,
location,
properties,
type
FROM azure.security.jit_network_access_policies
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>jit_network_access_policies</code> resource.

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
INSERT INTO azure.security.jit_network_access_policies (
ascLocation,
jitNetworkAccessPolicyName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
kind
)
SELECT 
'{{ ascLocation }}',
'{{ jitNetworkAccessPolicyName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ kind }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: virtualMachines
          value:
            - - name: id
                value: string
              - name: ports
                value:
                  - - name: number
                      value: []
                    - name: protocol
                      value: string
                    - name: allowedSourceAddressPrefix
                      value: string
                    - name: allowedSourceAddressPrefixes
                      value:
                        - string
                    - name: maxRequestAccessDuration
                      value: string
              - name: publicIpAddress
                value: string
        - name: requests
          value:
            - - name: virtualMachines
                value:
                  - - name: id
                      value: string
                    - name: ports
                      value:
                        - - name: allowedSourceAddressPrefix
                            value: string
                          - name: allowedSourceAddressPrefixes
                            value:
                              - string
                          - name: endTimeUtc
                            value: string
                          - name: status
                            value: string
                          - name: statusReason
                            value: string
                          - name: mappedPort
                            value: integer
              - name: startTimeUtc
                value: string
              - name: requestor
                value: string
              - name: justification
                value: string
        - name: provisioningState
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: kind
      value: string
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>jit_network_access_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.jit_network_access_policies
WHERE ascLocation = '{{ ascLocation }}'
AND jitNetworkAccessPolicyName = '{{ jitNetworkAccessPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
