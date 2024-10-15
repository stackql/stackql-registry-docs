---
title: mam_status
hide_title: false
hide_table_of_contents: false
keywords:
  - mam_status
  - intune
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

Creates, updates, deletes, gets or lists a <code>mam_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mam_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.intune.mam_status" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_mam_status', value: 'view', },
        { label: 'mam_status', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="deployed_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="enrolled_users" /> | `text` | field from the `properties` object |
| <CopyableCode code="flagged_users" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostName" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="nextlink" /> | `text` | Gets the URL to get the next set of results. |
| <CopyableCode code="policy_applied_users" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource Tags |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="wipe_failed_apps" /> | `text` | field from the `properties` object |
| <CopyableCode code="wipe_pending_apps" /> | `text` | field from the `properties` object |
| <CopyableCode code="wipe_succeeded_apps" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="nextlink" /> | `string` | Gets the URL to get the next set of results. |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource Tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostName" /> | Returns Intune Tenant level statuses. |

## `SELECT` examples

Returns Intune Tenant level statuses.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_mam_status', value: 'view', },
        { label: 'mam_status', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
deployed_policies,
enrolled_users,
flagged_users,
hostName,
last_modified_time,
location,
nextlink,
policy_applied_users,
status,
tags,
type,
wipe_failed_apps,
wipe_pending_apps,
wipe_succeeded_apps
FROM azure_extras.intune.vw_mam_status
WHERE hostName = '{{ hostName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
nextlink,
properties,
tags,
type
FROM azure_extras.intune.mam_status
WHERE hostName = '{{ hostName }}';
```
</TabItem></Tabs>

