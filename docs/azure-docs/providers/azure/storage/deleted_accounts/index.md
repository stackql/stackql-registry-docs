---
title: deleted_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_accounts
  - storage
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

Creates, updates, deletes, gets or lists a <code>deleted_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deleted_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.deleted_accounts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deleted_accounts', value: 'view', },
        { label: 'deleted_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="deletedAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="deletion_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore_reference" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Attributes of a deleted storage account. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deletedAccountName, location, subscriptionId" /> | Get properties of specified deleted account resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists deleted accounts under the subscription. |

## `SELECT` examples

Lists deleted accounts under the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deleted_accounts', value: 'view', },
        { label: 'deleted_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
creation_time,
deletedAccountName,
deletion_time,
location,
restore_reference,
storage_account_resource_id,
subscriptionId
FROM azure.storage.vw_deleted_accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.storage.deleted_accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

