---
title: web_app_extended_machines_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - web_app_extended_machines_controllers
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

Creates, updates, deletes, gets or lists a <code>web_app_extended_machines_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_app_extended_machines_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.web_app_extended_machines_controllers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_web_app_extended_machines_controllers', value: 'view', },
        { label: 'web_app_extended_machines_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="created_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="extendedMachineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="hydrated_run_as_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_deleted" /> | `text` | field from the `properties` object |
| <CopyableCode code="machine_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="machine_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_as_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="webAppSiteName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Class for web extended machine properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="extendedMachineName, resourceGroupName, siteName, subscriptionId, webAppSiteName" /> | Method to get a extended machine. |
| <CopyableCode code="list_by_web_app_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, webAppSiteName" /> | Method to get all extended machines. |

## `SELECT` examples

Method to get all extended machines.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_web_app_extended_machines_controllers', value: 'view', },
        { label: 'web_app_extended_machines_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
created_timestamp,
errors,
extendedMachineName,
host_name,
hydrated_run_as_account_id,
is_deleted,
machine_display_name,
machine_id,
provisioning_state,
resourceGroupName,
run_as_account_id,
siteName,
subscriptionId,
updated_timestamp,
webAppSiteName
FROM azure.migrate.vw_web_app_extended_machines_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND webAppSiteName = '{{ webAppSiteName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.migrate.web_app_extended_machines_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND webAppSiteName = '{{ webAppSiteName }}';
```
</TabItem></Tabs>

