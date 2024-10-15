---
title: vpn_site_link_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_site_link_connections
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

Creates, updates, deletes, gets or lists a <code>vpn_site_link_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_site_link_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.vpn_site_link_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vpn_site_link_connections', value: 'view', },
        { label: 'vpn_site_link_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="connectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_bandwidth" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="dpd_timeout_seconds" /> | `text` | field from the `properties` object |
| <CopyableCode code="egress_bytes_transferred" /> | `text` | field from the `properties` object |
| <CopyableCode code="egress_nat_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_bgp" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_rate_limiting" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="gatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ingress_bytes_transferred" /> | `text` | field from the `properties` object |
| <CopyableCode code="ingress_nat_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipsec_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="linkConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routing_weight" /> | `text` | field from the `properties` object |
| <CopyableCode code="shared_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="use_local_azure_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="use_policy_based_traffic_selectors" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_connection_protocol_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_gateway_custom_bgp_addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_link_connection_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_site_link" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Parameters for VpnConnection. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionName, gatewayName, linkConnectionName, resourceGroupName, subscriptionId" /> | Retrieves the details of a vpn site link connection. |

## `SELECT` examples

Retrieves the details of a vpn site link connection.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vpn_site_link_connections', value: 'view', },
        { label: 'vpn_site_link_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
connectionName,
connection_bandwidth,
connection_status,
dpd_timeout_seconds,
egress_bytes_transferred,
egress_nat_rules,
enable_bgp,
enable_rate_limiting,
etag,
gatewayName,
ingress_bytes_transferred,
ingress_nat_rules,
ipsec_policies,
linkConnectionName,
provisioning_state,
resourceGroupName,
routing_weight,
shared_key,
subscriptionId,
type,
use_local_azure_ip_address,
use_policy_based_traffic_selectors,
vpn_connection_protocol_type,
vpn_gateway_custom_bgp_addresses,
vpn_link_connection_mode,
vpn_site_link
FROM azure.network.vw_vpn_site_link_connections
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
etag,
properties,
type
FROM azure.network.vpn_site_link_connections
WHERE connectionName = '{{ connectionName }}'
AND gatewayName = '{{ gatewayName }}'
AND linkConnectionName = '{{ linkConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

