---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - paymentsresellersubscription
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.paymentsresellersubscription.subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Optional. Resource name of the subscription. It will have the format of "partners/&#123;partner_id&#125;/subscriptions/&#123;subscription_id&#125;". This is available for authorizeAddon, but otherwise is response only. |
| `processingState` | `string` | Output only. Describes the processing state of the subscription. See more details at [the lifecycle of a subscription](/payments/reseller/subscription/reference/index/Receive.Notifications#payments-subscription-lifecycle). |
| `cycleEndTime` | `string` | Output only. The time at which the subscription is expected to be extended, in ISO 8061 format. UTC timezone. For example: "2019-08-31T17:28:54.564Z" |
| `createTime` | `string` | Output only. System generated timestamp when the subscription is created. UTC timezone. |
| `promotions` | `array` | Optional. Deprecated: consider using the top-level `promotion_specs` as the input. Optional. Resource name that identifies one or more promotions that can be applied on the product. A typical promotion for a subscription is Free trial. The format will be 'partners/&#123;partner_id&#125;/promotions/&#123;promotion_id&#125;'. |
| `lineItems` | `array` | Required. The line items of the subscription. |
| `freeTrialEndTime` | `string` | Output only. End of the free trial period, in ISO 8061 format. For example, "2019-08-31T17:28:54.564Z". It will be set the same as createTime if no free trial promotion is specified. |
| `products` | `array` | Required. Deprecated: consider using `line_items` as the input. Required. Resource name that identifies the purchased products. The format will be 'partners/&#123;partner_id&#125;/products/&#123;product_id&#125;'. |
| `upgradeDowngradeDetails` | `object` | Details about the previous subscription that this new subscription upgrades/downgrades from. |
| `updateTime` | `string` | Output only. System generated timestamp when the subscription is most recently updated. UTC timezone. |
| `promotionSpecs` | `array` | Optional. Subscription-level promotions. Only free trial is supported on this level. It determines the first renewal time of the subscription to be the end of the free trial period. Specify the promotion resource name only when used as input. |
| `endUserEntitled` | `boolean` | Output only. Indicates if the subscription is entitled to the end user. |
| `serviceLocation` | `object` | Describes a location of an end user. |
| `partnerUserToken` | `string` | Required. Identifier of the end-user in partner’s system. The value is restricted to 63 ASCII characters at the maximum. |
| `renewalTime` | `string` | Output only. The time at which the subscription is expected to be renewed by Google - a new charge will be incurred and the service entitlement will be renewed. A non-immediate cancellation will take place at this time too, before which, the service entitlement for the end user will remain valid. UTC timezone in ISO 8061 format. For example: "2019-08-31T17:28:54.564Z" |
| `cancellationDetails` | `object` | Describes the details of a cancelled or cancelling subscription. |
| `redirectUri` | `string` | Output only. The place where partners should redirect the end-user to after creation. This field might also be populated when creation failed. However, Partners should always prepare a default URL to redirect the user in case this field is empty. |
| `state` | `string` | Output only. Describes the state of the subscription. See more details at [the lifecycle of a subscription](/payments/reseller/subscription/reference/index/Receive.Notifications#payments-subscription-lifecycle). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `partners_subscriptions_get` | `SELECT` | `partnersId, subscriptionsId` | Used by partners to get a subscription by id. It should be called directly by the partner using service accounts. |
| `partners_subscriptions_create` | `INSERT` | `partnersId` | Used by partners to create a subscription for their customers. The created subscription is associated with the end user inferred from the end user credentials. This API must be authorized by the end user using OAuth. |
| `partners_subscriptions_cancel` | `EXEC` | `partnersId, subscriptionsId` | Used by partners to cancel a subscription service either immediately or by the end of the current billing cycle for their customers. It should be called directly by the partner using service accounts. |
| `partners_subscriptions_entitle` | `EXEC` | `partnersId, subscriptionsId` | Used by partners to entitle a previously provisioned subscription to the current end user. The end user identity is inferred from the authorized credential of the request. This API must be authorized by the end user using OAuth. |
| `partners_subscriptions_extend` | `EXEC` | `partnersId, subscriptionsId` | [Deprecated] New partners should be on auto-extend by default. Used by partners to extend a subscription service for their customers on an ongoing basis for the subscription to remain active and renewable. It should be called directly by the partner using service accounts. |
| `partners_subscriptions_provision` | `EXEC` | `partnersId` | Used by partners to provision a subscription for their customers. This creates a subscription without associating it with the end user account. EntitleSubscription must be called separately using OAuth in order for the end user account to be associated with the subscription. It should be called directly by the partner using service accounts. |
| `partners_subscriptions_undoCancel` | `EXEC` | `partnersId, subscriptionsId` | Used by partners to revoke the pending cancellation of a subscription, which is currently in `STATE_CANCEL_AT_END_OF_CYCLE` state. If the subscription is already cancelled, the request will fail. It should be called directly by the partner using service accounts. |
