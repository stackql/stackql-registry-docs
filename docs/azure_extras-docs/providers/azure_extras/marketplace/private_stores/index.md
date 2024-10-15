---
title: private_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - private_stores
  - marketplace
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

Creates, updates, deletes, gets or lists a <code>private_stores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.marketplace.private_stores" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_stores', value: 'view', },
        { label: 'private_stores', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="availability" /> | `text` | field from the `properties` object |
| <CopyableCode code="branding" /> | `text` | field from the `properties` object |
| <CopyableCode code="collection_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_gov" /> | `text` | field from the `properties` object |
| <CopyableCode code="notifications_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="privateStoreId" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_store_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_store_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | Describes the json payload on whether or not the private store is enabled for a given tenant |
| <CopyableCode code="systemData" /> | `object` | Read only system data |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateStoreId" /> | Get information about the private store |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Gets the list of available private stores. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="privateStoreId" /> | Changes private store properties |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateStoreId" /> | Deletes the private store. All that is not saved will be lost. |
| <CopyableCode code="acknowledge_offer_notification" /> | `EXEC` | <CopyableCode code="offerId, privateStoreId" /> | Acknowledge notification for offer |
| <CopyableCode code="admin_request_approvals_list" /> | `EXEC` | <CopyableCode code="privateStoreId" /> | Get list of admin request approvals |
| <CopyableCode code="any_existing_offers_in_the_collections" /> | `EXEC` | <CopyableCode code="privateStoreId" /> | Query whether exists any offer in the collections. |
| <CopyableCode code="billing_accounts" /> | `EXEC` | <CopyableCode code="privateStoreId" /> | Tenant billing accounts names |
| <CopyableCode code="bulk_collections_action" /> | `EXEC` | <CopyableCode code="privateStoreId" /> | Perform an action on bulk collections |
| <CopyableCode code="collections_to_subscriptions_mapping" /> | `EXEC` | <CopyableCode code="privateStoreId" /> | For a given subscriptions list, the API will return a map of collections and the related subscriptions from the supplied list. |
| <CopyableCode code="fetch_all_subscriptions_in_tenant" /> | `EXEC` | <CopyableCode code="privateStoreId" /> | Fetch all subscriptions in tenant, only for marketplace admin |
| <CopyableCode code="query_approved_plans" /> | `EXEC` | <CopyableCode code="privateStoreId" /> | Get map of plans and related approved subscriptions. |
| <CopyableCode code="query_notifications_state" /> | `EXEC` | <CopyableCode code="privateStoreId" /> | Get private store notifications state |
| <CopyableCode code="query_offers" /> | `EXEC` | <CopyableCode code="privateStoreId" /> | List of offers, regardless the collections |
| <CopyableCode code="query_request_approval" /> | `EXEC` | <CopyableCode code="privateStoreId, requestApprovalId" /> | Get request statuses foreach plan, this api is used as a complex GET action. |
| <CopyableCode code="query_user_offers" /> | `EXEC` | <CopyableCode code="privateStoreId" /> | List of user's approved offers for the provided offers and subscriptions |
| <CopyableCode code="withdraw_plan" /> | `EXEC` | <CopyableCode code="privateStoreId, requestApprovalId" /> | Withdraw a user request approval on specific plan |

## `SELECT` examples

Gets the list of available private stores.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_stores', value: 'view', },
        { label: 'private_stores', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
availability,
branding,
collection_ids,
e_tag,
is_gov,
notifications_settings,
privateStoreId,
private_store_id,
private_store_name,
system_data,
tenant_id,
type
FROM azure_extras.marketplace.vw_private_stores
;
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
FROM azure_extras.marketplace.private_stores
;
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>private_stores</code> resource.

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
INSERT INTO azure_extras.marketplace.private_stores (
privateStoreId,
properties
)
SELECT 
'{{ privateStoreId }}',
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
    - name: type
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: []
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: availability
          value: string
        - name: privateStoreId
          value: string
        - name: eTag
          value: string
        - name: privateStoreName
          value: string
        - name: tenantId
          value: string
        - name: isGov
          value: boolean
        - name: collectionIds
          value:
            - string
        - name: branding
          value: object
        - name: notificationsSettings
          value:
            - name: recipients
              value:
                - - name: principalId
                    value: string
                  - name: emailAddress
                    value: string
                  - name: displayName
                    value: string
            - name: sendToAllMarketplaceAdmins
              value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>private_stores</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.marketplace.private_stores
WHERE privateStoreId = '{{ privateStoreId }}';
```
