---
title: organization_cluster_by_ids
hide_title: false
hide_table_of_contents: false
keywords:
  - organization_cluster_by_ids
  - confluent
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

Creates, updates, deletes, gets or lists a <code>organization_cluster_by_ids</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organization_cluster_by_ids</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.confluent.organization_cluster_by_ids" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_organization_cluster_by_ids', value: 'view', },
        { label: 'organization_cluster_by_ids', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Id of the cluster |
| <CopyableCode code="name" /> | `text` | Display name of the cluster |
| <CopyableCode code="clusterId" /> | `text` | field from the `properties` object |
| <CopyableCode code="environmentId" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Type of cluster |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="organizationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="spec" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the cluster |
| <CopyableCode code="name" /> | `string` | Display name of the cluster |
| <CopyableCode code="kind" /> | `string` | Type of cluster |
| <CopyableCode code="properties" /> | `object` | Cluster Properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterId, environmentId, organizationName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_organization_cluster_by_ids', value: 'view', },
        { label: 'organization_cluster_by_ids', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
clusterId,
environmentId,
kind,
metadata,
organizationName,
resourceGroupName,
spec,
status,
subscriptionId
FROM azure_isv.confluent.vw_organization_cluster_by_ids
WHERE clusterId = '{{ clusterId }}'
AND environmentId = '{{ environmentId }}'
AND organizationName = '{{ organizationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
kind,
properties
FROM azure_isv.confluent.organization_cluster_by_ids
WHERE clusterId = '{{ clusterId }}'
AND environmentId = '{{ environmentId }}'
AND organizationName = '{{ organizationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

