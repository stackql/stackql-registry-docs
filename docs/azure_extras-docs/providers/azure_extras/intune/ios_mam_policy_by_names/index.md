---
title: ios_mam_policy_by_names
hide_title: false
hide_table_of_contents: false
keywords:
  - ios_mam_policy_by_names
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

Creates, updates, deletes, gets or lists a <code>ios_mam_policy_by_names</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ios_mam_policy_by_names</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.intune.ios_mam_policy_by_names" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ios_mam_policy_by_names', value: 'view', },
        { label: 'ios_mam_policy_by_names', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="access_recheck_offline_timeout" /> | `text` | field from the `properties` object |
| <CopyableCode code="access_recheck_online_timeout" /> | `text` | field from the `properties` object |
| <CopyableCode code="app_sharing_from_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="app_sharing_to_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="authentication" /> | `text` | field from the `properties` object |
| <CopyableCode code="clipboard_sharing_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_backup" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_compliance" /> | `text` | field from the `properties` object |
| <CopyableCode code="file_encryption_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="file_sharing_save_as" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="group_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostName" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="managed_browser" /> | `text` | field from the `properties` object |
| <CopyableCode code="num_of_apps" /> | `text` | field from the `properties` object |
| <CopyableCode code="offline_wipe_timeout" /> | `text` | field from the `properties` object |
| <CopyableCode code="pin" /> | `text` | field from the `properties` object |
| <CopyableCode code="pin_num_retry" /> | `text` | field from the `properties` object |
| <CopyableCode code="policyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource Tags |
| <CopyableCode code="touch_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Intune MAM iOS Policy Properties. |
| <CopyableCode code="tags" /> | `object` | Resource Tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostName, policyName" /> | Returns Intune iOS policies. |

## `SELECT` examples

Returns Intune iOS policies.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ios_mam_policy_by_names', value: 'view', },
        { label: 'ios_mam_policy_by_names', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
access_recheck_offline_timeout,
access_recheck_online_timeout,
app_sharing_from_level,
app_sharing_to_level,
authentication,
clipboard_sharing_level,
data_backup,
device_compliance,
file_encryption_level,
file_sharing_save_as,
friendly_name,
group_status,
hostName,
last_modified_time,
location,
managed_browser,
num_of_apps,
offline_wipe_timeout,
pin,
pin_num_retry,
policyName,
tags,
touch_id,
type
FROM azure_extras.intune.vw_ios_mam_policy_by_names
WHERE hostName = '{{ hostName }}'
AND policyName = '{{ policyName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure_extras.intune.ios_mam_policy_by_names
WHERE hostName = '{{ hostName }}'
AND policyName = '{{ policyName }}';
```
</TabItem></Tabs>

