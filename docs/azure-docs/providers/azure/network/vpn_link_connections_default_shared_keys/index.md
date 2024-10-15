---
title: vpn_link_connections_default_shared_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_link_connections_default_shared_keys
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

Creates, updates, deletes, gets or lists a <code>vpn_link_connections_default_shared_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_link_connections_default_shared_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.vpn_link_connections_default_shared_keys" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vpn_link_connections_default_shared_keys', value: 'view', },
        { label: 'vpn_link_connections_default_shared_keys', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="connectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="gatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="linkConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="shared_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="shared_key_length" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="properties" /> | `object` | Parameters for SharedKey. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionName, gatewayName, linkConnectionName, resourceGroupName, subscriptionId" /> | Gets the shared key of VpnLink connection specified. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="connectionName, gatewayName, linkConnectionName, resourceGroupName, subscriptionId" /> | Gets the value of the shared key of VpnLink connection specified. |

## `SELECT` examples

Gets the shared key of VpnLink connection specified.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vpn_link_connections_default_shared_keys', value: 'view', },
        { label: 'vpn_link_connections_default_shared_keys', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
connectionName,
gatewayName,
linkConnectionName,
provisioning_state,
resourceGroupName,
shared_key,
shared_key_length,
subscriptionId,
type
FROM azure.network.vw_vpn_link_connections_default_shared_keys
WHERE connectionName = '{{ connectionName }}'
AND gatewayName = '{{ gatewayName }}'
AND linkConnectionName = '{{ linkConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.network.vpn_link_connections_default_shared_keys
WHERE connectionName = '{{ connectionName }}'
AND gatewayName = '{{ gatewayName }}'
AND linkConnectionName = '{{ linkConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

