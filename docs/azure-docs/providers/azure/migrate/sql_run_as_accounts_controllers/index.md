---
title: sql_run_as_accounts_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_run_as_accounts_controllers
  - migrate
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

Creates, updates, deletes, gets or lists a <code>sql_run_as_accounts_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_run_as_accounts_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.sql_run_as_accounts_controllers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_run_as_accounts_controllers', value: 'view', },
        { label: 'sql_run_as_accounts_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="appliance_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="credential_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlSiteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_timestamp" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Class for run as account properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | Get a SqlRunAsAccount |
| <CopyableCode code="list_by_sql_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | List SqlRunAsAccount resources by SqlSite |

## `SELECT` examples

List SqlRunAsAccount resources by SqlSite

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_run_as_accounts_controllers', value: 'view', },
        { label: 'sql_run_as_accounts_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
appliance_name,
created_timestamp,
credential_type,
display_name,
provisioning_state,
resourceGroupName,
siteName,
sqlSiteName,
subscriptionId,
updated_timestamp
FROM azure.migrate.vw_sql_run_as_accounts_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND sqlSiteName = '{{ sqlSiteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.migrate.sql_run_as_accounts_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND sqlSiteName = '{{ sqlSiteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

