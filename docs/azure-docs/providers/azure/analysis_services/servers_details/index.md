---
title: servers_details
hide_title: false
hide_table_of_contents: false
keywords:
  - servers_details
  - analysis_services
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

Creates, updates, deletes, gets or lists a <code>servers_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>servers_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.analysis_services.servers_details" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_servers_details', value: 'view', },
        { label: 'servers_details', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | An identifier that represents the Analysis Services resource. |
| <CopyableCode code="name" /> | `text` | The name of the Analysis Services resource. |
| <CopyableCode code="as_administrators" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_blob_container_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="gateway_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_v4_firewall_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the Analysis Services resource. |
| <CopyableCode code="managed_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="querypool_connection_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_full_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_monitor_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Represents the SKU name and Azure pricing tier for Analysis Services resource. |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Key-value pairs of additional resource provisioning properties. |
| <CopyableCode code="type" /> | `text` | The type of the Analysis Services resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | An identifier that represents the Analysis Services resource. |
| <CopyableCode code="name" /> | `string` | The name of the Analysis Services resource. |
| <CopyableCode code="location" /> | `string` | Location of the Analysis Services resource. |
| <CopyableCode code="properties" /> | `object` | Properties of Analysis Services resource. |
| <CopyableCode code="sku" /> | `object` | Represents the SKU name and Azure pricing tier for Analysis Services resource. |
| <CopyableCode code="tags" /> | `object` | Key-value pairs of additional resource provisioning properties. |
| <CopyableCode code="type" /> | `string` | The type of the Analysis Services resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets details about the specified Analysis Services server. |

## `SELECT` examples

Gets details about the specified Analysis Services server.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_servers_details', value: 'view', },
        { label: 'servers_details', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
as_administrators,
backup_blob_container_uri,
gateway_details,
ip_v4_firewall_settings,
location,
managed_mode,
provisioning_state,
querypool_connection_mode,
resourceGroupName,
serverName,
server_full_name,
server_monitor_mode,
sku,
state,
subscriptionId,
tags,
type
FROM azure.analysis_services.vw_servers_details
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
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
sku,
tags,
type
FROM azure.analysis_services.servers_details
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

