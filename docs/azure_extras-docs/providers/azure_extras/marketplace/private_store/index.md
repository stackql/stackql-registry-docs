---
title: private_store
hide_title: false
hide_table_of_contents: false
keywords:
  - private_store
  - marketplace
  - azure_extras    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_store</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.marketplace.private_store</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` | Describes the json payload on whether or not the private store is enabled for a given tenant |
| `systemData` | `object` | Read only system data |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `privateStoreId` | Get information about the private store |
| `list` | `SELECT` |  | Gets the list of available private stores. |
| `create_or_update` | `INSERT` | `privateStoreId` | Changes private store properties |
| `delete` | `DELETE` | `privateStoreId` | Deletes the private store. All that is not saved will be lost. |
| `_admin_request_approvals_list` | `EXEC` | `privateStoreId` | Get list of admin request approvals |
| `_list` | `EXEC` |  | Gets the list of available private stores. |
| `acknowledge_offer_notification` | `EXEC` | `offerId, privateStoreId` | Acknowledge notification for offer |
| `admin_request_approvals_list` | `EXEC` | `privateStoreId` | Get list of admin request approvals |
| `any_existing_offers_in_the_collections` | `EXEC` | `privateStoreId` | Query whether exists any offer in the collections. |
| `billing_accounts` | `EXEC` | `privateStoreId` | Tenant billing accounts names |
| `bulk_collections_action` | `EXEC` | `privateStoreId` | Perform an action on bulk collections |
| `collections_to_subscriptions_mapping` | `EXEC` | `privateStoreId` | For a given subscriptions list, the API will return a map of collections and the related subscriptions from the supplied list. |
| `fetch_all_subscriptions_in_tenant` | `EXEC` | `privateStoreId` | Fetch all subscriptions in tenant, only for marketplace admin |
| `query_approved_plans` | `EXEC` | `privateStoreId` | Get map of plans and related approved subscriptions. |
| `query_notifications_state` | `EXEC` | `privateStoreId` | Get private store notifications state |
| `query_offers` | `EXEC` | `privateStoreId` | List of offers, regardless the collections |
| `query_request_approval` | `EXEC` | `privateStoreId, requestApprovalId` | Get request statuses foreach plan, this api is used as a complex GET action. |
| `query_user_offers` | `EXEC` | `privateStoreId` | List of user's approved offers for the provided offers and subscriptions |
| `withdraw_plan` | `EXEC` | `privateStoreId, requestApprovalId` | Withdraw a user request approval on specific plan |
