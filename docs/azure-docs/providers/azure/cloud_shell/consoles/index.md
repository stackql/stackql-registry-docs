---
title: consoles
hide_title: false
hide_table_of_contents: false
keywords:
  - consoles
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

Creates, updates, deletes, gets or lists a <code>consoles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consoles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cloud_shell.consoles" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_consoles', value: 'view', },
        { label: 'consoles', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="consoleName" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="consoleName" /> | Gets the console for the user. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="consoleName" /> | Deletes the console |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="consoleName, data__properties" /> | Puts a request for a console |
| <CopyableCode code="keep_alive" /> | `EXEC` | <CopyableCode code="consoleName" /> | Keep console alive |
| <CopyableCode code="keep_alive_with_location" /> | `EXEC` | <CopyableCode code="consoleName, location" /> | Keep console alive |
| <CopyableCode code="put_with_location" /> | `EXEC` | <CopyableCode code="consoleName, location" /> | Puts a request for a console |

## `SELECT` examples

Gets the console for the user.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_consoles', value: 'view', },
        { label: 'consoles', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
consoleName,
os_type,
provisioning_state,
uri
FROM azure.cloud_shell.vw_consoles
WHERE consoleName = '{{ consoleName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.cloud_shell.consoles
WHERE consoleName = '{{ consoleName }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>consoles</code> resource.

```sql
/*+ update */
REPLACE azure.cloud_shell.consoles
SET 
properties = '{{ properties }}'
WHERE 
consoleName = '{{ consoleName }}'
AND data__properties = '{{ data__properties }}';
```

## `DELETE` example

Deletes the specified <code>consoles</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cloud_shell.consoles
WHERE consoleName = '{{ consoleName }}';
```
