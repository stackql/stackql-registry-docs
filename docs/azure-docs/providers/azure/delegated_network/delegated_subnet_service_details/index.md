---
title: delegated_subnet_service_details
hide_title: false
hide_table_of_contents: false
keywords:
  - delegated_subnet_service_details
  - delegated_network
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

Creates, updates, deletes, gets or lists a <code>delegated_subnet_service_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delegated_subnet_service_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.delegated_network.delegated_subnet_service_details" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_delegated_subnet_service_details', value: 'view', },
        { label: 'delegated_subnet_service_details', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | An identifier that represents the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="allocation_block_prefix_size" /> | `text` | field from the `properties` object |
| <CopyableCode code="controller_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="subnet_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="type" /> | `text` | The type of resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | An identifier that represents the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of delegated subnet |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets details about the specified dnc DelegatedSubnet Link. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Delete dnc DelegatedSubnet. |

## `SELECT` examples

Gets details about the specified dnc DelegatedSubnet Link.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_delegated_subnet_service_details', value: 'view', },
        { label: 'delegated_subnet_service_details', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
allocation_block_prefix_size,
controller_details,
location,
provisioning_state,
resourceGroupName,
resourceName,
resource_guid,
subnet_details,
subscriptionId,
tags,
type
FROM azure.delegated_network.vw_delegated_subnet_service_details
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.delegated_network.delegated_subnet_service_details
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>delegated_subnet_service_details</code> resource.

```sql
/*+ delete */
DELETE FROM azure.delegated_network.delegated_subnet_service_details
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
