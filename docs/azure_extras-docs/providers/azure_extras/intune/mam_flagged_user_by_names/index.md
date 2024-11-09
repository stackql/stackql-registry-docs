---
title: mam_flagged_user_by_names
hide_title: false
hide_table_of_contents: false
keywords:
  - mam_flagged_user_by_names
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

Creates, updates, deletes, gets or lists a <code>mam_flagged_user_by_names</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mam_flagged_user_by_names</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.intune.mam_flagged_user_by_names" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_mam_flagged_user_by_names', value: 'view', },
        { label: 'mam_flagged_user_by_names', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="error_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="tags" /> | `text` | Resource Tags |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="userName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource Tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostName, userName" /> | Returns Intune flagged user details |

## `SELECT` examples

Returns Intune flagged user details

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_mam_flagged_user_by_names', value: 'view', },
        { label: 'mam_flagged_user_by_names', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
error_count,
friendly_name,
hostName,
location,
tags,
type,
userName
FROM azure_extras.intune.vw_mam_flagged_user_by_names
WHERE hostName = '{{ hostName }}'
AND userName = '{{ userName }}';
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
FROM azure_extras.intune.mam_flagged_user_by_names
WHERE hostName = '{{ hostName }}'
AND userName = '{{ userName }}';
```
</TabItem></Tabs>
