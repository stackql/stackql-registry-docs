---
title: private_endpoint_connections_group_ids
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections_group_ids
  - notification_hubs
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

Creates, updates, deletes, gets or lists a <code>private_endpoint_connections_group_ids</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_endpoint_connections_group_ids</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.notification_hubs.private_endpoint_connections_group_ids" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_endpoint_connections_group_ids', value: 'view', },
        { label: 'private_endpoint_connections_group_ids', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="namespaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="required_members" /> | `text` | field from the `properties` object |
| <CopyableCode code="required_zone_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Represents properties of Private Link Resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subResourceName, subscriptionId" /> | Even though this namespace requires subscription id, resource group and namespace name, it returns a constant payload (for a given namespacE) every time it's called.
That's why we don't send it to the sibling RP, but process it directly in the scale unit that received the request. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Even though this namespace requires subscription id, resource group and namespace name, it returns a constant payload (for a given namespacE) every time it's called.
That's why we don't send it to the sibling RP, but process it directly in the scale unit that received the request. |

## `SELECT` examples

Even though this namespace requires subscription id, resource group and namespace name, it returns a constant payload (for a given namespacE) every time it's called.
That's why we don't send it to the sibling RP, but process it directly in the scale unit that received the request.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_endpoint_connections_group_ids', value: 'view', },
        { label: 'private_endpoint_connections_group_ids', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
group_id,
namespaceName,
required_members,
required_zone_names,
resourceGroupName,
subResourceName,
subscriptionId
FROM azure.notification_hubs.vw_private_endpoint_connections_group_ids
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.notification_hubs.private_endpoint_connections_group_ids
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

