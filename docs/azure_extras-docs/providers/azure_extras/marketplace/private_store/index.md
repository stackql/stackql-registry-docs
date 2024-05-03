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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_store</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.marketplace.private_store" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | Describes the json payload on whether or not the private store is enabled for a given tenant |
| <CopyableCode code="systemData" /> | `object` | Read only system data |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateStoreId" /> | Get information about the private store |
| <CopyableCode code="list" /> | `SELECT` |  | Gets the list of available private stores. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="privateStoreId" /> | Changes private store properties |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateStoreId" /> | Deletes the private store. All that is not saved will be lost. |
| <CopyableCode code="_admin_request_approvals_list" /> | `EXEC` | <CopyableCode code="privateStoreId" /> | Get list of admin request approvals |
| <CopyableCode code="_list" /> | `EXEC` |  | Gets the list of available private stores. |
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
