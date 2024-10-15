---
title: storage_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_accounts
  - storage_admin
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

Creates, updates, deletes, gets or lists a <code>storage_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.storage_admin.storage_accounts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_accounts', value: 'view', },
        { label: 'storage_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource Name. |
| <CopyableCode code="access_tier" /> | `text` | field from the `properties` object |
| <CopyableCode code="accountId" /> | `text` | field from the `properties` object |
| <CopyableCode code="account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="account_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="account_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="deleted_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="fault_domain" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The kind of storage account |
| <CopyableCode code="location" /> | `text` | Resource Location. |
| <CopyableCode code="primary_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_of_primary" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supports_https_traffic_only" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="tenant_resource_group_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_storage_account_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_subscription_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_view_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource Type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | The kind of storage account |
| <CopyableCode code="location" /> | `string` | Resource Location. |
| <CopyableCode code="properties" /> | `object` | Properties of a storage account. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource Type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountId, location, subscriptionId" /> | Returns the requested storage account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Returns a list of storage accounts. |
| <CopyableCode code="reclaim_storage_capacity" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Start reclaim storage capacity on deleted storage objects. |
| <CopyableCode code="undelete" /> | `EXEC` | <CopyableCode code="accountId, location, subscriptionId" /> | Undelete a deleted storage account with new account name if the a new name is provided. |

## `SELECT` examples

Returns a list of storage accounts.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_accounts', value: 'view', },
        { label: 'storage_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
access_tier,
accountId,
account_id,
account_status,
account_type,
creation_time,
deleted_time,
encryption,
fault_domain,
health_state,
kind,
location,
primary_endpoints,
primary_location,
provisioning_state,
status_of_primary,
subscriptionId,
supports_https_traffic_only,
tags,
tenant_resource_group_name,
tenant_storage_account_name,
tenant_subscription_id,
tenant_view_id,
type
FROM azure_stack.storage_admin.vw_storage_accounts
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
kind,
location,
properties,
tags,
type
FROM azure_stack.storage_admin.storage_accounts
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

