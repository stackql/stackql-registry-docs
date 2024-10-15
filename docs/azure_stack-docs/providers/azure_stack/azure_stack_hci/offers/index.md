---
title: offers
hide_title: false
hide_table_of_contents: false
keywords:
  - offers
  - azure_stack_hci
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

Creates, updates, deletes, gets or lists a <code>offers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>offers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.offers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_offers', value: 'view', },
        { label: 'offers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="content" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="offerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisherName" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku_mappings" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Publisher properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, offerName, publisherName, resourceGroupName, subscriptionId" /> | Get Offer resource details within a publisher of HCI Cluster. |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | List Offers available across publishers for the HCI Cluster. |
| <CopyableCode code="list_by_publisher" /> | `SELECT` | <CopyableCode code="clusterName, publisherName, resourceGroupName, subscriptionId" /> | List Offers available for a publisher within the HCI Cluster. |

## `SELECT` examples

List Offers available across publishers for the HCI Cluster.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_offers', value: 'view', },
        { label: 'offers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
clusterName,
content,
content_version,
offerName,
provisioning_state,
publisherName,
publisher_id,
resourceGroupName,
sku_mappings,
subscriptionId
FROM azure_stack.azure_stack_hci.vw_offers
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_stack.azure_stack_hci.offers
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

