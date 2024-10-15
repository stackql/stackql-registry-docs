---
title: publishers
hide_title: false
hide_table_of_contents: false
keywords:
  - publishers
  - edge_marketplace
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

Creates, updates, deletes, gets or lists a <code>publishers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>publishers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.edge_marketplace.publishers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_publishers', value: 'view', },
        { label: 'publishers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisherName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceUri" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Publisher properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="publisherName, resourceUri" /> | Get a Publisher |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | List Publisher resources by parent |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List Publisher resources in subscription |

## `SELECT` examples

List Publisher resources by parent

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_publishers', value: 'view', },
        { label: 'publishers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
provisioning_state,
publisherName,
resourceUri,
subscriptionId
FROM azure_extras.edge_marketplace.vw_publishers
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.edge_marketplace.publishers
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem></Tabs>

