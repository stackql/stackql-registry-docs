---
title: vpn_site_links
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_site_links
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

Creates, updates, deletes, gets or lists a <code>vpn_site_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_site_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.vpn_site_links" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vpn_site_links', value: 'view', },
        { label: 'vpn_site_links', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="bgp_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="link_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="vpnSiteLinkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpnSiteName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Parameters for VpnSite. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vpnSiteLinkName, vpnSiteName" /> | Retrieves the details of a VPN site link. |
| <CopyableCode code="list_by_vpn_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vpnSiteName" /> | Lists all the vpnSiteLinks in a resource group for a vpn site. |

## `SELECT` examples

Lists all the vpnSiteLinks in a resource group for a vpn site.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vpn_site_links', value: 'view', },
        { label: 'vpn_site_links', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
bgp_properties,
etag,
fqdn,
ip_address,
link_properties,
provisioning_state,
resourceGroupName,
subscriptionId,
type,
vpnSiteLinkName,
vpnSiteName
FROM azure.network.vw_vpn_site_links
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vpnSiteName = '{{ vpnSiteName }}';
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
FROM azure.network.vpn_site_links
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vpnSiteName = '{{ vpnSiteName }}';
```
</TabItem></Tabs>

