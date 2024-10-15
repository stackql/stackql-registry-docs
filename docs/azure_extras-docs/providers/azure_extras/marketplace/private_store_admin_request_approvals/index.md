---
title: private_store_admin_request_approvals
hide_title: false
hide_table_of_contents: false
keywords:
  - private_store_admin_request_approvals
  - marketplace
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

Creates, updates, deletes, gets or lists a <code>private_store_admin_request_approvals</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_store_admin_request_approvals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.marketplace.private_store_admin_request_approvals" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_store_admin_request_approvals', value: 'view', },
        { label: 'private_store_admin_request_approvals', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="adminRequestApprovalId" /> | `text` | field from the `properties` object |
| <CopyableCode code="admin_action" /> | `text` | field from the `properties` object |
| <CopyableCode code="administrator" /> | `text` | field from the `properties` object |
| <CopyableCode code="approved_plans" /> | `text` | field from the `properties` object |
| <CopyableCode code="collection_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="comment" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="icon" /> | `text` | field from the `properties` object |
| <CopyableCode code="offer_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="plans" /> | `text` | field from the `properties` object |
| <CopyableCode code="privateStoreId" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisherId" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | Admin approval request resource properties |
| <CopyableCode code="systemData" /> | `object` | Read only system data |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="adminRequestApprovalId, privateStoreId, publisherId" /> | Get open approval requests |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="adminRequestApprovalId, privateStoreId" /> | Update the admin action, weather the request is approved or rejected and the approved plans |

## `SELECT` examples

Get open approval requests

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_store_admin_request_approvals', value: 'view', },
        { label: 'private_store_admin_request_approvals', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
adminRequestApprovalId,
admin_action,
administrator,
approved_plans,
collection_ids,
comment,
display_name,
icon,
offer_id,
plans,
privateStoreId,
publisherId,
publisher_id,
system_data,
type
FROM azure_extras.marketplace.vw_private_store_admin_request_approvals
WHERE adminRequestApprovalId = '{{ adminRequestApprovalId }}'
AND privateStoreId = '{{ privateStoreId }}'
AND publisherId = '{{ publisherId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure_extras.marketplace.private_store_admin_request_approvals
WHERE adminRequestApprovalId = '{{ adminRequestApprovalId }}'
AND privateStoreId = '{{ privateStoreId }}'
AND publisherId = '{{ publisherId }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>private_store_admin_request_approvals</code> resource.

```sql
/*+ update */
REPLACE azure_extras.marketplace.private_store_admin_request_approvals
SET 
properties = '{{ properties }}'
WHERE 
adminRequestApprovalId = '{{ adminRequestApprovalId }}'
AND privateStoreId = '{{ privateStoreId }}';
```
