---
title: entitlements
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlements
  - cloudcommerceprocurement
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

Creates, updates, deletes, gets or lists a <code>entitlements</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entitlements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudcommerceprocurement.entitlements" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the entitlement. Entitlement names have the form `providers/{provider_id}/entitlements/{entitlement_id}`. |
| <CopyableCode code="account" /> | `string` | Output only. The resource name of the account that this entitlement is based on, if any. |
| <CopyableCode code="cancellationReason" /> | `string` | Output only. The reason the entitlement was cancelled. If this entitlement wasn't cancelled, this field is empty. Possible values include "unknown", "expired", "user-cancelled", "account-closed", "billing-disabled" (if the customer has manually disabled billing to their resources), "user-aborted", and "migrated" (if the entitlement has migrated across products). Values of this field are subject to change, and we recommend that you don't build your technical integration to rely on these fields. |
| <CopyableCode code="consumers" /> | `array` | Output only. The resources using this entitlement, if applicable. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp. |
| <CopyableCode code="entitlementBenefitIds" /> | `array` | Output only. The entitlement benefit IDs associated with the purchase. |
| <CopyableCode code="inputProperties" /> | `object` | Output only. The custom properties that were collected from the user to create this entitlement. |
| <CopyableCode code="messageToUser" /> | `string` | Provider-supplied message that is displayed to the end user. Currently this is used to communicate progress and ETA for provisioning. This field can be updated only when a user is waiting for an action from the provider, i.e. entitlement state is EntitlementState.ENTITLEMENT_ACTIVATION_REQUESTED or EntitlementState.ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL. This field is cleared automatically when the entitlement state changes. |
| <CopyableCode code="newOfferEndTime" /> | `string` | Output only. The end time of the new offer. If the offer was created with a term instead of a specified end date, this field is empty. This field is populated even if the entitlement isn't active yet. If there's no upcoming offer, the field is be empty. |
| <CopyableCode code="newOfferStartTime" /> | `string` | Output only. The timestamp when the new offer becomes effective. This field is populated even if the entitlement isn't active yet. If there's no upcoming offer, the field is empty. |
| <CopyableCode code="newPendingOffer" /> | `string` | Output only. The name of the offer the entitlement is switching to upon a pending plan change. Only exists if the pending plan change is moving to an offer. This field isn't populated for entitlements which aren't active yet. Format: 'projects/{project}/services/{service}/privateOffers/{offer-id}' OR 'projects/{project}/services/{service}/standardOffers/{offer-id}', depending on whether the offer is private or public. The {service} in the name is the listing service of the offer. It could be either the product service that the offer is referencing, or a generic private offer parent service. We recommend that you don't build your integration to rely on the meaning of this {service} part. |
| <CopyableCode code="newPendingOfferDuration" /> | `string` | Output only. The duration of the new offer, in ISO 8601 duration format. This field isn't populated for entitlements which aren't active yet, only for pending offer changes. If the offer was created with a specified end date instead of a duration, this field is empty. |
| <CopyableCode code="newPendingPlan" /> | `string` | Output only. The identifier of the pending new plan. Required if the product has plans and the entitlement has a pending plan change. |
| <CopyableCode code="offer" /> | `string` | Output only. The name of the offer that was procured. Field is empty if order was not made using an offer. Format: 'projects/{project}/services/{service}/privateOffers/{offer-id}' OR 'projects/{project}/services/{service}/standardOffers/{offer-id}', depending on whether the offer is private or public. The {service} in the name is the listing service of the offer. It could be either the product service that the offer is referencing, or a generic private offer parent service. We recommend that you don't build your integration to rely on the meaning of this {service} part. |
| <CopyableCode code="offerDuration" /> | `string` | Output only. The offer duration of the current offer in ISO 8601 duration format. Field is empty if entitlement was not made using an offer. If the offer was created with a specified end date instead of a duration, this field is empty. |
| <CopyableCode code="offerEndTime" /> | `string` | Output only. End time for the Offer association corresponding to this entitlement. The field is only populated if the entitlement is currently associated with an Offer. |
| <CopyableCode code="orderId" /> | `string` | Output only. The order ID of this entitlement, without any `orders/` resource name prefix. |
| <CopyableCode code="plan" /> | `string` | Output only. The identifier of the plan that was procured. Required if the product has plans. |
| <CopyableCode code="product" /> | `string` | Output only. The identifier of the entity that was purchased. This may actually represent a product, quote, or offer. We strongly recommend that you use the following more explicit fields: productExternalName, quoteExternalName, or offer. |
| <CopyableCode code="productExternalName" /> | `string` | Output only. The identifier of the product that was procured. |
| <CopyableCode code="provider" /> | `string` | Output only. The identifier of the service provider that this entitlement was created against. Each service provider is assigned a unique provider value when they onboard with Cloud Commerce platform. |
| <CopyableCode code="quoteExternalName" /> | `string` | Output only. The identifier of the quote that was used to procure. Empty if the order is not purchased using a quote. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the entitlement. |
| <CopyableCode code="subscriptionEndTime" /> | `string` | Output only. End time for the subscription corresponding to this entitlement. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp. |
| <CopyableCode code="usageReportingId" /> | `string` | Output only. The consumerId to use when reporting usage through the Service Control API. See the consumerId field at [Reporting Metrics](https://cloud.google.com/service-control/reporting-metrics) for more details. This field is present only if the product has usage-based billing configured. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="entitlementsId, providersId" /> | Gets a requested Entitlement resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="providersId" /> | Lists Entitlements for which the provider has read access. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="entitlementsId, providersId" /> | Updates an existing Entitlement. |
| <CopyableCode code="approve" /> | `EXEC` | <CopyableCode code="entitlementsId, providersId" /> | Approves an entitlement that is in the EntitlementState.ENTITLEMENT_ACTIVATION_REQUESTED state. This method is invoked by the provider to approve the creation of the entitlement resource. |
| <CopyableCode code="approve_plan_change" /> | `EXEC` | <CopyableCode code="entitlementsId, providersId" /> | Approves an entitlement plan change that is in the EntitlementState.ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL state. This method is invoked by the provider to approve the plan change on the entitlement resource. |
| <CopyableCode code="reject" /> | `EXEC` | <CopyableCode code="entitlementsId, providersId" /> | Rejects an entitlement that is in the EntitlementState.ENTITLEMENT_ACTIVATION_REQUESTED state. This method is invoked by the provider to reject the creation of the entitlement resource. |
| <CopyableCode code="reject_plan_change" /> | `EXEC` | <CopyableCode code="entitlementsId, providersId" /> | Rejects an entitlement plan change that is in the EntitlementState.ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL state. This method is invoked by the provider to reject the plan change on the entitlement resource. |
| <CopyableCode code="suspend" /> | `EXEC` | <CopyableCode code="entitlementsId, providersId" /> | Requests suspension of an active Entitlement. This is not yet supported. |

## `SELECT` examples

Lists Entitlements for which the provider has read access.

```sql
SELECT
name,
account,
cancellationReason,
consumers,
createTime,
entitlementBenefitIds,
inputProperties,
messageToUser,
newOfferEndTime,
newOfferStartTime,
newPendingOffer,
newPendingOfferDuration,
newPendingPlan,
offer,
offerDuration,
offerEndTime,
orderId,
plan,
product,
productExternalName,
provider,
quoteExternalName,
state,
subscriptionEndTime,
updateTime,
usageReportingId
FROM google.cloudcommerceprocurement.entitlements
WHERE providersId = '{{ providersId }}'; 
```

## `UPDATE` example

Updates a <code>entitlements</code> resource.

```sql
/*+ update */
UPDATE google.cloudcommerceprocurement.entitlements
SET 
provider = '{{ provider }}',
inputProperties = '{{ inputProperties }}',
product = '{{ product }}',
messageToUser = '{{ messageToUser }}',
consumers = '{{ consumers }}',
plan = '{{ plan }}',
account = '{{ account }}',
usageReportingId = '{{ usageReportingId }}',
state = '{{ state }}',
name = '{{ name }}',
newPendingPlan = '{{ newPendingPlan }}'
WHERE 
entitlementsId = '{{ entitlementsId }}'
AND providersId = '{{ providersId }}';
```
