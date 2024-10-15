---
title: share_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - share_subscriptions
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

Creates, updates, deletes, gets or lists a <code>share_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>share_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.share_subscriptions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_share_subscriptions', value: 'view', },
        { label: 'share_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id of the azure resource |
| <CopyableCode code="name" /> | `text` | Name of the azure resource |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="invitation_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_email" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_tenant_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="shareSubscriptionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="share_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="share_kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="share_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="share_subscription_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="share_terms" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_share_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the azure resource |
| <CopyableCode code="user_email" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id of the azure resource |
| <CopyableCode code="name" /> | `string` | Name of the azure resource |
| <CopyableCode code="properties" /> | `object` | Share subscription property bag. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of the azure resource |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, shareSubscriptionName, subscriptionId" /> | Get a shareSubscription in an account |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List share subscriptions in an account |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, shareSubscriptionName, subscriptionId, data__properties" /> | Create a shareSubscription in an account |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, shareSubscriptionName, subscriptionId" /> | Delete a shareSubscription in an account |
| <CopyableCode code="cancel_synchronization" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, shareSubscriptionName, subscriptionId, data__synchronizationId" /> | Request to cancel a synchronization. |
| <CopyableCode code="synchronize" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, shareSubscriptionName, subscriptionId" /> | Initiate a copy |

## `SELECT` examples

List share subscriptions in an account

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_share_subscriptions', value: 'view', },
        { label: 'share_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
created_at,
expiration_date,
invitation_id,
provider_email,
provider_name,
provider_tenant_name,
provisioning_state,
resourceGroupName,
shareSubscriptionName,
share_description,
share_kind,
share_name,
share_subscription_status,
share_terms,
source_share_location,
subscriptionId,
system_data,
type,
user_email,
user_name
FROM azure.data_share.vw_share_subscriptions
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
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
FROM azure.data_share.share_subscriptions
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>share_subscriptions</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.data_share.share_subscriptions (
accountName,
resourceGroupName,
shareSubscriptionName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ shareSubscriptionName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: systemData
      value:
        - name: createdAt
          value: string
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: lastModifiedAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: createdAt
          value: string
        - name: expirationDate
          value: string
        - name: invitationId
          value: string
        - name: providerEmail
          value: string
        - name: providerName
          value: string
        - name: providerTenantName
          value: string
        - name: provisioningState
          value: string
        - name: shareDescription
          value: string
        - name: shareKind
          value: string
        - name: shareName
          value: string
        - name: shareSubscriptionStatus
          value: string
        - name: shareTerms
          value: string
        - name: sourceShareLocation
          value: string
        - name: userEmail
          value: string
        - name: userName
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>share_subscriptions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_share.share_subscriptions
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND shareSubscriptionName = '{{ shareSubscriptionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
