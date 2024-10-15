---
title: delegated_provider_offers
hide_title: false
hide_table_of_contents: false
keywords:
  - delegated_provider_offers
  - subscriptions_admin
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

Creates, updates, deletes, gets or lists a <code>delegated_provider_offers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delegated_provider_offers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.subscriptions_admin.delegated_provider_offers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_delegated_provider_offers', value: 'view', },
        { label: 'delegated_provider_offers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="accessibility_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="delegatedProviderSubscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="delegated_offer_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="external_reference_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource |
| <CopyableCode code="offer" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key-value pairs. |
| <CopyableCode code="type" /> | `text` | Type of resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource |
| <CopyableCode code="properties" /> | `object` | Properties for an delegated provider. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="delegatedProviderSubscriptionId, offer, subscriptionId" /> | Get the specified delegated provider offer. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="delegatedProviderSubscriptionId, subscriptionId" /> | Get the list of delegated provider offers. |

## `SELECT` examples

Get the list of delegated provider offers.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_delegated_provider_offers', value: 'view', },
        { label: 'delegated_provider_offers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
accessibility_state,
delegatedProviderSubscriptionId,
delegated_offer_id,
display_name,
external_reference_id,
location,
offer,
subscriptionId,
subscription_count,
tags,
type
FROM azure_stack.subscriptions_admin.vw_delegated_provider_offers
WHERE delegatedProviderSubscriptionId = '{{ delegatedProviderSubscriptionId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure_stack.subscriptions_admin.delegated_provider_offers
WHERE delegatedProviderSubscriptionId = '{{ delegatedProviderSubscriptionId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

