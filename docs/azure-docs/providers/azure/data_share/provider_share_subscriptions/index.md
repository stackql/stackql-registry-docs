---
title: provider_share_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_share_subscriptions
  - data_share
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

Creates, updates, deletes, gets or lists a <code>provider_share_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_share_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.provider_share_subscriptions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_provider_share_subscriptions', value: 'view', },
        { label: 'provider_share_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id of the azure resource |
| <CopyableCode code="name" /> | `text` | Name of the azure resource |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="consumer_email" /> | `text` | field from the `properties` object |
| <CopyableCode code="consumer_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="consumer_tenant_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="providerShareSubscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_email" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="shareName" /> | `text` | field from the `properties` object |
| <CopyableCode code="share_subscription_object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="share_subscription_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="shared_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the azure resource |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id of the azure resource |
| <CopyableCode code="name" /> | `string` | Name of the azure resource |
| <CopyableCode code="properties" /> | `object` | Provider share subscription properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of the azure resource |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_share" /> | `SELECT` | <CopyableCode code="accountName, providerShareSubscriptionId, resourceGroupName, shareName, subscriptionId" /> | Get share subscription in a provider share |
| <CopyableCode code="list_by_share" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, shareName, subscriptionId" /> | List share subscriptions in a provider share |
| <CopyableCode code="adjust" /> | `EXEC` | <CopyableCode code="accountName, providerShareSubscriptionId, resourceGroupName, shareName, subscriptionId" /> | Adjust a share subscription's expiration date in a provider share |
| <CopyableCode code="reinstate" /> | `EXEC` | <CopyableCode code="accountName, providerShareSubscriptionId, resourceGroupName, shareName, subscriptionId" /> | Reinstate share subscription in a provider share |
| <CopyableCode code="revoke" /> | `EXEC` | <CopyableCode code="accountName, providerShareSubscriptionId, resourceGroupName, shareName, subscriptionId" /> | Revoke share subscription in a provider share |

## `SELECT` examples

List share subscriptions in a provider share

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_provider_share_subscriptions', value: 'view', },
        { label: 'provider_share_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
consumer_email,
consumer_name,
consumer_tenant_name,
created_at,
expiration_date,
providerShareSubscriptionId,
provider_email,
provider_name,
resourceGroupName,
shareName,
share_subscription_object_id,
share_subscription_status,
shared_at,
subscriptionId,
system_data,
type
FROM azure.data_share.vw_provider_share_subscriptions
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND shareName = '{{ shareName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.data_share.provider_share_subscriptions
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND shareName = '{{ shareName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

