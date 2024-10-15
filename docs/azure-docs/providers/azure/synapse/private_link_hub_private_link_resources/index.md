---
title: private_link_hub_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_hub_private_link_resources
  - synapse
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

Creates, updates, deletes, gets or lists a <code>private_link_hub_private_link_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_link_hub_private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.private_link_hub_private_link_resources" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_link_hub_private_link_resources', value: 'view', },
        { label: 'private_link_hub_private_link_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="privateLinkHubName" /> | `text` | field from the `properties` object |
| <CopyableCode code="privateLinkResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="required_members" /> | `text` | field from the `properties` object |
| <CopyableCode code="required_zone_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a private link resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateLinkHubName, privateLinkResourceName, resourceGroupName, subscriptionId" /> | Get private link resource in private link hub |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="privateLinkHubName, resourceGroupName, subscriptionId" /> | Get all private link resources for a private link hub |

## `SELECT` examples

Get all private link resources for a private link hub

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_link_hub_private_link_resources', value: 'view', },
        { label: 'private_link_hub_private_link_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
group_id,
privateLinkHubName,
privateLinkResourceName,
required_members,
required_zone_names,
resourceGroupName,
subscriptionId
FROM azure.synapse.vw_private_link_hub_private_link_resources
WHERE privateLinkHubName = '{{ privateLinkHubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.synapse.private_link_hub_private_link_resources
WHERE privateLinkHubName = '{{ privateLinkHubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

