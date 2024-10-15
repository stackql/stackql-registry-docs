---
title: ddos_custom_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - ddos_custom_policies
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

Creates, updates, deletes, gets or lists a <code>ddos_custom_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ddos_custom_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.ddos_custom_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ddos_custom_policies', value: 'view', },
        { label: 'ddos_custom_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="ddosCustomPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | DDoS custom policy properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ddosCustomPolicyName, resourceGroupName, subscriptionId" /> | Gets information about the specified DDoS custom policy. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="ddosCustomPolicyName, resourceGroupName, subscriptionId" /> | Creates or updates a DDoS custom policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="ddosCustomPolicyName, resourceGroupName, subscriptionId" /> | Deletes the specified DDoS custom policy. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="ddosCustomPolicyName, resourceGroupName, subscriptionId" /> | Update a DDoS custom policy tags. |

## `SELECT` examples

Gets information about the specified DDoS custom policy.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ddos_custom_policies', value: 'view', },
        { label: 'ddos_custom_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
ddosCustomPolicyName,
etag,
location,
provisioning_state,
resourceGroupName,
resource_guid,
subscriptionId,
tags,
type
FROM azure.network.vw_ddos_custom_policies
WHERE ddosCustomPolicyName = '{{ ddosCustomPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
tags,
type
FROM azure.network.ddos_custom_policies
WHERE ddosCustomPolicyName = '{{ ddosCustomPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ddos_custom_policies</code> resource.

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
INSERT INTO azure.network.ddos_custom_policies (
ddosCustomPolicyName,
resourceGroupName,
subscriptionId,
properties,
id,
location,
tags
)
SELECT 
'{{ ddosCustomPolicyName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ id }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: resourceGuid
          value: string
        - name: provisioningState
          value: []
    - name: etag
      value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>ddos_custom_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.ddos_custom_policies
WHERE ddosCustomPolicyName = '{{ ddosCustomPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
