---
title: console_with_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - console_with_locations
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

Creates, updates, deletes, gets or lists a <code>console_with_locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>console_with_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cloud_shell.console_with_locations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_console_with_locations', value: 'view', },
        { label: 'console_with_locations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="consoleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="uri" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Cloud shell console properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="consoleName, location" /> | Gets the console for the user. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="consoleName, location" /> | Deletes the console |

## `SELECT` examples

Gets the console for the user.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_console_with_locations', value: 'view', },
        { label: 'console_with_locations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
consoleName,
location,
os_type,
provisioning_state,
uri
FROM azure.cloud_shell.vw_console_with_locations
WHERE consoleName = '{{ consoleName }}'
AND location = '{{ location }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.cloud_shell.console_with_locations
WHERE consoleName = '{{ consoleName }}'
AND location = '{{ location }}';
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>console_with_locations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cloud_shell.console_with_locations
WHERE consoleName = '{{ consoleName }}'
AND location = '{{ location }}';
```
