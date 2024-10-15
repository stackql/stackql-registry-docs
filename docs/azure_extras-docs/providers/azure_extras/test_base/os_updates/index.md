---
title: os_updates
hide_title: false
hide_table_of_contents: false
keywords:
  - os_updates
  - test_base
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

Creates, updates, deletes, gets or lists a <code>os_updates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>os_updates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.os_updates" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_os_updates', value: 'view', },
        { label: 'os_updates', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="build_revision" /> | `text` | field from the `properties` object |
| <CopyableCode code="build_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_image_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_image_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="flighting_ring" /> | `text` | field from the `properties` object |
| <CopyableCode code="inplace_upgrade_baseline_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="osUpdateResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="osUpdateType" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="packageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="release" /> | `text` | field from the `properties` object |
| <CopyableCode code="release_version_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of an OS Update. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="osUpdateResourceName, packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets an OS Update by name in which the package was tested before. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="osUpdateType, packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists the OS Updates in which the package were tested before. |

## `SELECT` examples

Lists the OS Updates in which the package were tested before.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_os_updates', value: 'view', },
        { label: 'os_updates', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
build_revision,
build_version,
custom_image_display_name,
custom_image_id,
flighting_ring,
inplace_upgrade_baseline_properties,
osUpdateResourceName,
osUpdateType,
os_name,
packageName,
release,
release_version_date,
resourceGroupName,
subscriptionId,
testBaseAccountName,
type
FROM azure_extras.test_base.vw_os_updates
WHERE osUpdateType = '{{ osUpdateType }}'
AND packageName = '{{ packageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.test_base.os_updates
WHERE osUpdateType = '{{ osUpdateType }}'
AND packageName = '{{ packageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem></Tabs>

