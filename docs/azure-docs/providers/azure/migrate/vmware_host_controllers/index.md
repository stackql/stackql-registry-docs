---
title: vmware_host_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - vmware_host_controllers
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

Creates, updates, deletes, gets or lists a <code>vmware_host_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vmware_host_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.vmware_host_controllers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vmware_host_controllers', value: 'view', },
        { label: 'vmware_host_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="appliance_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="datastores" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="uuid" /> | `text` | field from the `properties` object |
| <CopyableCode code="vcenter_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Class for host properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostName, resourceGroupName, siteName, subscriptionId" /> | Get a VmwareHost |
| <CopyableCode code="list_by_vmware_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | List VmwareHost resources by VmwareSite |

## `SELECT` examples

List VmwareHost resources by VmwareSite

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vmware_host_controllers', value: 'view', },
        { label: 'vmware_host_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
appliance_names,
created_timestamp,
datastores,
hostName,
provisioning_state,
resourceGroupName,
siteName,
subscriptionId,
updated_timestamp,
uuid,
vcenter_id
FROM azure.migrate.vw_vmware_host_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.migrate.vmware_host_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

