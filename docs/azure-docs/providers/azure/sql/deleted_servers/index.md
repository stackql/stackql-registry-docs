---
title: deleted_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_servers
  - sql
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

Creates, updates, deletes, gets or lists a <code>deleted_servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deleted_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.deleted_servers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deleted_servers', value: 'view', },
        { label: 'deleted_servers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="deletedServerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="deletion_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="fully_qualified_domain_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="locationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="original_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a deleted server. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deletedServerName, locationName, subscriptionId" /> | Gets a deleted server. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of all deleted servers in a subscription. |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="locationName, subscriptionId" /> | Gets a list of deleted servers for a location. |
| <CopyableCode code="recover" /> | `EXEC` | <CopyableCode code="deletedServerName, locationName, subscriptionId" /> | Recovers a deleted server. |

## `SELECT` examples

Gets a list of all deleted servers in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deleted_servers', value: 'view', },
        { label: 'deleted_servers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
deletedServerName,
deletion_time,
fully_qualified_domain_name,
locationName,
original_id,
subscriptionId,
version
FROM azure.sql.vw_deleted_servers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.deleted_servers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

