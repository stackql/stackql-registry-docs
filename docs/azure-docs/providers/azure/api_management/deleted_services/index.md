---
title: deleted_services
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_services
  - api_management
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.deleted_services" /></td></tr>
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
| <CopyableCode code="deletion_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | API Management Service Master Location. |
| <CopyableCode code="scheduled_purge_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | API Management Service Master Location. |
| <CopyableCode code="properties" /> | `object` |  |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_name" /> | `SELECT` | <CopyableCode code="location, serviceName, subscriptionId" /> | Get soft-deleted Api Management Service by name. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all soft-deleted services available for undelete for the given subscription. |
| <CopyableCode code="purge" /> | `EXEC` | <CopyableCode code="location, serviceName, subscriptionId" /> | Purges Api Management Service (deletes it with no option to undelete). |

## `SELECT` examples

Lists all soft-deleted services available for undelete for the given subscription.

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
deletion_date,
location,
scheduled_purge_date,
serviceName,
service_id,
subscriptionId
FROM azure.api_management.vw_deleted_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties
FROM azure.api_management.deleted_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

