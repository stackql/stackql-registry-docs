---
title: software_inventories
hide_title: false
hide_table_of_contents: false
keywords:
  - software_inventories
  - security
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

Creates, updates, deletes, gets or lists a <code>software_inventories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>software_inventories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.software_inventories" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_software_inventories', value: 'view', },
        { label: 'software_inventories', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="device_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_of_support_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_of_support_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="first_seen_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_known_vulnerabilities" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_platform" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceNamespace" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceType" /> | `text` | field from the `properties` object |
| <CopyableCode code="softwareName" /> | `text` | field from the `properties` object |
| <CopyableCode code="software_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="vendor" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Software Inventory resource properties |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, resourceNamespace, resourceType, softwareName, subscriptionId" /> | Gets a single software data of the virtual machine. |
| <CopyableCode code="list_by_extended_resource" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, resourceNamespace, resourceType, subscriptionId" /> | Gets the software inventory of the virtual machine. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the software inventory of all virtual machines in the subscriptions. |

## `SELECT` examples

Gets the software inventory of all virtual machines in the subscriptions.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_software_inventories', value: 'view', },
        { label: 'software_inventories', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
device_id,
end_of_support_date,
end_of_support_status,
first_seen_at,
number_of_known_vulnerabilities,
os_platform,
resourceGroupName,
resourceName,
resourceNamespace,
resourceType,
softwareName,
software_name,
subscriptionId,
type,
vendor,
version
FROM azure.security.vw_software_inventories
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.software_inventories
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

