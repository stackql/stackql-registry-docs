---
title: dns_private_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_private_zones
  - oracle
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

Creates, updates, deletes, gets or lists a <code>dns_private_zones</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dns_private_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.dns_private_zones" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dns_private_zones', value: 'view', },
        { label: 'dns_private_zones', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dnsprivatezonename" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_protected" /> | `text` | field from the `properties` object |
| <CopyableCode code="lifecycle_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="ocid" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="self" /> | `text` | field from the `properties` object |
| <CopyableCode code="serial" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="view_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="zone_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Zones resource model |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dnsprivatezonename, location, subscriptionId" /> | Get a DnsPrivateZone |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | List DnsPrivateZone resources by Location |

## `SELECT` examples

List DnsPrivateZone resources by Location

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dns_private_zones', value: 'view', },
        { label: 'dns_private_zones', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dnsprivatezonename,
is_protected,
lifecycle_state,
location,
ocid,
provisioning_state,
self,
serial,
subscriptionId,
time_created,
version,
view_id,
zone_type
FROM azure_isv.oracle.vw_dns_private_zones
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.oracle.dns_private_zones
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

