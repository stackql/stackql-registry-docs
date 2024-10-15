---
title: dns_private_views
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_private_views
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

Creates, updates, deletes, gets or lists a <code>dns_private_views</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dns_private_views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.dns_private_views" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dns_private_views', value: 'view', },
        { label: 'dns_private_views', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="dnsprivateviewocid" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_protected" /> | `text` | field from the `properties` object |
| <CopyableCode code="lifecycle_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="ocid" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="self" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_updated" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Views resource model |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dnsprivateviewocid, location, subscriptionId" /> | Get a DnsPrivateView |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | List DnsPrivateView resources by Location |

## `SELECT` examples

List DnsPrivateView resources by Location

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dns_private_views', value: 'view', },
        { label: 'dns_private_views', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
display_name,
dnsprivateviewocid,
is_protected,
lifecycle_state,
location,
ocid,
provisioning_state,
self,
subscriptionId,
time_created,
time_updated
FROM azure_isv.oracle.vw_dns_private_views
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.oracle.dns_private_views
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

