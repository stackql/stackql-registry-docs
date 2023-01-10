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
| `PrivateStore_Get` | `SELECT` | `privateStoreId` | Get information about the private store |
| `PrivateStore_List` | `SELECT` |  | Gets the list of available private stores. |
| `PrivateStore_CreateOrUpdate` | `INSERT` | `privateStoreId` | Changes private store properties |
| `PrivateStore_Delete` | `DELETE` | `privateStoreId` | Deletes the private store. All that is not saved will be lost. |
| `PrivateStore_AcknowledgeOfferNotification` | `EXEC` | `offerId, privateStoreId` | Acknowledge notification for offer |
| `PrivateStore_AdminRequestApprovalsList` | `EXEC` | `privateStoreId` | Get list of admin request approvals |
| `PrivateStore_AnyExistingOffersInTheCollections` | `EXEC` | `privateStoreId` | Query whether exists any offer in the collections. |
| `PrivateStore_BillingAccounts` | `EXEC` | `privateStoreId` | Tenant billing accounts names |
| `PrivateStore_BulkCollectionsAction` | `EXEC` | `privateStoreId` | Perform an action on bulk collections |
| `PrivateStore_CollectionsToSubscriptionsMapping` | `EXEC` | `privateStoreId` | For a given subscriptions list, the API will return a map of collections and the related subscriptions from the supplied list. |
| `PrivateStore_CreateApprovalRequest` | `EXEC` | `privateStoreId, requestApprovalId` | Create approval request |
| `PrivateStore_FetchAllSubscriptionsInTenant` | `EXEC` | `privateStoreId` | Fetch all subscriptions in tenant, only for marketplace admin |
| `PrivateStore_GetAdminRequestApproval` | `EXEC` | `adminRequestApprovalId, privateStoreId, publisherId` | Get open approval requests |
| `PrivateStore_GetApprovalRequestsList` | `EXEC` | `privateStoreId` | Get all open approval requests of current user |
| `PrivateStore_GetRequestApproval` | `EXEC` | `privateStoreId, requestApprovalId` | Get open request approval details |
| `PrivateStore_ListNewPlansNotifications` | `EXEC` | `privateStoreId` | List new plans notifications |
| `PrivateStore_ListStopSellOffersPlansNotifications` | `EXEC` | `privateStoreId` | List stop sell notifications for both stop sell offers and stop sell plans |
| `PrivateStore_ListSubscriptionsContext` | `EXEC` | `privateStoreId` | List all the subscriptions in the private store context |
| `PrivateStore_QueryApprovedPlans` | `EXEC` | `privateStoreId` | Get map of plans and related approved subscriptions. |
| `PrivateStore_QueryNotificationsState` | `EXEC` | `privateStoreId` | Get private store notifications state |
| `PrivateStore_QueryOffers` | `EXEC` | `privateStoreId` | List of offers, regardless the collections |
| `PrivateStore_QueryRequestApproval` | `EXEC` | `privateStoreId, requestApprovalId` | Get request statuses foreach plan, this api is used as a complex GET action. |
| `PrivateStore_QueryUserOffers` | `EXEC` | `privateStoreId` | List of user's approved offers for the provided offers and subscriptions |
| `PrivateStore_UpdateAdminRequestApproval` | `EXEC` | `adminRequestApprovalId, privateStoreId` | Update the admin action, weather the request is approved or rejected and the approved plans |
| `PrivateStore_WithdrawPlan` | `EXEC` | `privateStoreId, requestApprovalId` | Withdraw a user request approval on specific plan |
