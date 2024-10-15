---
title: deleted_services
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_services
  - api_center
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

Creates, updates, deletes, gets or lists a <code>deleted_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deleted_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_center.deleted_services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deleted_services', value: 'view', },
        { label: 'deleted_services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="deletedServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduled_purge_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="soft_deletion_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Deleted service properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deletedServiceName, resourceGroupName, subscriptionId" /> | Returns details of the soft-deleted service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists soft-deleted services. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists services within an Azure subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deletedServiceName, resourceGroupName, subscriptionId" /> | Permanently deletes specified service. |

## `SELECT` examples

Lists services within an Azure subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deleted_services', value: 'view', },
        { label: 'deleted_services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
deletedServiceName,
resourceGroupName,
scheduled_purge_date,
soft_deletion_date,
subscriptionId
FROM azure.api_center.vw_deleted_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_center.deleted_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>deleted_services</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_center.deleted_services
WHERE deletedServiceName = '{{ deletedServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
