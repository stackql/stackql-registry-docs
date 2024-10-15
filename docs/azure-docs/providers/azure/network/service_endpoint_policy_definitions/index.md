---
title: service_endpoint_policy_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - service_endpoint_policy_definitions
  - network
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

Creates, updates, deletes, gets or lists a <code>service_endpoint_policy_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_endpoint_policy_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.service_endpoint_policy_definitions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_service_endpoint_policy_definitions', value: 'view', },
        { label: 'service_endpoint_policy_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceEndpointPolicyDefinitionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceEndpointPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Service Endpoint policy definition resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceEndpointPolicyDefinitionName, serviceEndpointPolicyName, subscriptionId" /> | Get the specified service endpoint policy definitions from service endpoint policy. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceEndpointPolicyName, subscriptionId" /> | Gets all service endpoint policy definitions in a service end point policy. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, serviceEndpointPolicyDefinitionName, serviceEndpointPolicyName, subscriptionId" /> | Creates or updates a service endpoint policy definition in the specified service endpoint policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serviceEndpointPolicyDefinitionName, serviceEndpointPolicyName, subscriptionId" /> | Deletes the specified ServiceEndpoint policy definitions. |

## `SELECT` examples

Gets all service endpoint policy definitions in a service end point policy.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_service_endpoint_policy_definitions', value: 'view', },
        { label: 'service_endpoint_policy_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
etag,
provisioning_state,
resourceGroupName,
service,
serviceEndpointPolicyDefinitionName,
serviceEndpointPolicyName,
service_resources,
subscriptionId,
type
FROM azure.network.vw_service_endpoint_policy_definitions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceEndpointPolicyName = '{{ serviceEndpointPolicyName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure.network.service_endpoint_policy_definitions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceEndpointPolicyName = '{{ serviceEndpointPolicyName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service_endpoint_policy_definitions</code> resource.

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
INSERT INTO azure.network.service_endpoint_policy_definitions (
resourceGroupName,
serviceEndpointPolicyDefinitionName,
serviceEndpointPolicyName,
subscriptionId,
properties,
name,
type,
id
)
SELECT 
'{{ resourceGroupName }}',
'{{ serviceEndpointPolicyDefinitionName }}',
'{{ serviceEndpointPolicyName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ name }}',
'{{ type }}',
'{{ id }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: description
          value: string
        - name: service
          value: string
        - name: serviceResources
          value:
            - string
        - name: provisioningState
          value: []
    - name: name
      value: string
    - name: etag
      value: string
    - name: type
      value: string
    - name: id
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>service_endpoint_policy_definitions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.service_endpoint_policy_definitions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceEndpointPolicyDefinitionName = '{{ serviceEndpointPolicyDefinitionName }}'
AND serviceEndpointPolicyName = '{{ serviceEndpointPolicyName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
