---
title: replication_logical_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_logical_networks
  - recovery_services_site_recovery
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

Creates, updates, deletes, gets or lists a <code>replication_logical_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_logical_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_logical_networks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_logical_networks', value: 'view', },
        { label: 'replication_logical_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource Name |
| <CopyableCode code="fabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="logicalNetworkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="logical_network_definitions_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="logical_network_usage" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_virtualization_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource Type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Logical Network Properties. |
| <CopyableCode code="type" /> | `string` | Resource Type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricName, logicalNetworkName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of a logical network. |
| <CopyableCode code="list_by_replication_fabrics" /> | `SELECT` | <CopyableCode code="fabricName, resourceGroupName, resourceName, subscriptionId" /> | Lists all the logical networks of the Azure Site Recovery fabric. |

## `SELECT` examples

Lists all the logical networks of the Azure Site Recovery fabric.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_logical_networks', value: 'view', },
        { label: 'replication_logical_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
fabricName,
friendly_name,
location,
logicalNetworkName,
logical_network_definitions_status,
logical_network_usage,
network_virtualization_status,
resourceGroupName,
resourceName,
subscriptionId,
type
FROM azure.recovery_services_site_recovery.vw_replication_logical_networks
WHERE fabricName = '{{ fabricName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
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
type
FROM azure.recovery_services_site_recovery.replication_logical_networks
WHERE fabricName = '{{ fabricName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

