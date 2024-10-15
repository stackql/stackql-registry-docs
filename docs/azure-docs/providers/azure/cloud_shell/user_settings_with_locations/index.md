---
title: user_settings_with_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - user_settings_with_locations
  - cloud_shell
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

Creates, updates, deletes, gets or lists a <code>user_settings_with_locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_settings_with_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cloud_shell.user_settings_with_locations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_user_settings_with_locations', value: 'view', },
        { label: 'user_settings_with_locations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="preferred_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="preferred_os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="preferred_shell_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="terminal_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="userSettingsName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The cloud shell user settings properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, userSettingsName" /> | Get current user settings for current signed in user. This operation returns settings for the user's cloud shell preferences including preferred location, storage profile, shell type, font and size settings. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="location, userSettingsName" /> | Delete cloud shell settings for current signed in user |

## `SELECT` examples

Get current user settings for current signed in user. This operation returns settings for the user's cloud shell preferences including preferred location, storage profile, shell type, font and size settings.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_user_settings_with_locations', value: 'view', },
        { label: 'user_settings_with_locations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
location,
preferred_location,
preferred_os_type,
preferred_shell_type,
storage_profile,
terminal_settings,
userSettingsName
FROM azure.cloud_shell.vw_user_settings_with_locations
WHERE location = '{{ location }}'
AND userSettingsName = '{{ userSettingsName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.cloud_shell.user_settings_with_locations
WHERE location = '{{ location }}'
AND userSettingsName = '{{ userSettingsName }}';
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>user_settings_with_locations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cloud_shell.user_settings_with_locations
WHERE location = '{{ location }}'
AND userSettingsName = '{{ userSettingsName }}';
```
