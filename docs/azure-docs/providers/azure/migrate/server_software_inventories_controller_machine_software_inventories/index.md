---
title: server_software_inventories_controller_machine_software_inventories
hide_title: false
hide_table_of_contents: false
keywords:
  - server_software_inventories_controller_machine_software_inventories
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

Creates, updates, deletes, gets or lists a <code>server_software_inventories_controller_machine_software_inventories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_software_inventories_controller_machine_software_inventories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.server_software_inventories_controller_machine_software_inventories" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_software_inventories_controller_machine_software_inventories', value: 'view', },
        { label: 'server_software_inventories_controller_machine_software_inventories', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="" /> | `text` | field from the `properties` object |
| <CopyableCode code="apps_and_roles" /> | `text` | field from the `properties` object |
| <CopyableCode code="machineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Class for machine software inventory properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="default, machineName, resourceGroupName, siteName, subscriptionId" /> | Method to get a machines software inventory like applications and roles. |

## `SELECT` examples

Method to get a machines software inventory like applications and roles.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_software_inventories_controller_machine_software_inventories', value: 'view', },
        { label: 'server_software_inventories_controller_machine_software_inventories', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
,
apps_and_roles,
machineName,
provisioning_state,
resourceGroupName,
siteName,
subscriptionId
FROM azure.migrate.vw_server_software_inventories_controller_machine_software_inventories
WHERE default = '{{ default }}'
AND machineName = '{{ machineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.migrate.server_software_inventories_controller_machine_software_inventories
WHERE default = '{{ default }}'
AND machineName = '{{ machineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

