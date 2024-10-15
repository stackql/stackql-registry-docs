---
title: available_inplace_upgrade_os
hide_title: false
hide_table_of_contents: false
keywords:
  - available_inplace_upgrade_os
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

Creates, updates, deletes, gets or lists a <code>available_inplace_upgrade_os</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>available_inplace_upgrade_os</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.available_inplace_upgrade_os" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_available_inplace_upgrade_os', value: 'view', },
        { label: 'available_inplace_upgrade_os', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="availableInplaceUpgradeOSResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="osUpdateType" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_os_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_os_releases" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_target_os_name_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The Available In-place Upgrade OS properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="availableInplaceUpgradeOSResourceName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets an available In-place Upgrade OS to run a package under a Test Base Account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="osUpdateType, resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all the available In-place Upgrade OSs to a package under a Test Base Account. |

## `SELECT` examples

Lists all the available In-place Upgrade OSs to a package under a Test Base Account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_available_inplace_upgrade_os', value: 'view', },
        { label: 'available_inplace_upgrade_os', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
availableInplaceUpgradeOSResourceName,
osUpdateType,
provisioning_state,
resourceGroupName,
source_os_name,
source_os_releases,
subscriptionId,
supported_target_os_name_list,
testBaseAccountName
FROM azure_extras.test_base.vw_available_inplace_upgrade_os
WHERE osUpdateType = '{{ osUpdateType }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.test_base.available_inplace_upgrade_os
WHERE osUpdateType = '{{ osUpdateType }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem></Tabs>

