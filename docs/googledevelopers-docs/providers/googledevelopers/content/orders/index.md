---
title: orders
hide_title: false
hide_table_of_contents: false
keywords:
  - orders
  - content
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
<tr><td><b>Name</b></td><td><code>orders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.orders</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The REST ID of the order. Globally unique. |
| `billingAddress` | `object` |  |
| `merchantId` | `string` |  |
| `pickupDetails` | `object` |  |
| `status` | `string` | The status of the order. Acceptable values are: - "`canceled`" - "`delivered`" - "`inProgress`" - "`partiallyDelivered`" - "`partiallyReturned`" - "`partiallyShipped`" - "`pendingShipment`" - "`returned`" - "`shipped`"  |
| `lineItems` | `array` | Line items that are ordered. |
| `annotations` | `array` | List of key-value pairs that are attached to a given order. |
| `promotions` | `array` | Promotions associated with the order. To determine which promotions apply to which products, check the `Promotions[].appliedItems[].lineItemId` field against the `LineItems[].id` field for each promotion. If a promotion is applied to more than 1 offerId, divide the discount value by the number of affected offers to determine how much discount to apply to each offerId. Examples: 1. To calculate price paid by the customer for a single line item including the discount: For each promotion, subtract the `LineItems[].adjustments[].priceAdjustment.value` amount from the `LineItems[].Price.value`. 2. To calculate price paid by the customer for a single line item including the discount in case of multiple quantity: For each promotion, divide the `LineItems[].adjustments[].priceAdjustment.value` by the quantity of products then subtract the resulting value from the `LineItems[].Product.Price.value` for each quantity item. Only 1 promotion can be applied to an offerId in a given order. To refund an item which had a promotion applied to it, make sure to refund the amount after first subtracting the promotion discount from the item price. More details about the program are here. |
| `shipments` | `array` | Shipments of the order. |
| `netPriceAmount` | `object` |  |
| `placedDate` | `string` | The date when the order was placed, in ISO 8601 format. |
| `customer` | `object` |  |
| `shippingCostTax` | `object` |  |
| `taxCollector` | `string` | The party responsible for collecting and remitting taxes. Acceptable values are: - "`marketplaceFacilitator`" - "`merchant`"  |
| `netTaxAmount` | `object` |  |
| `shippingCost` | `object` |  |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#order`" |
| `acknowledged` | `boolean` | Whether the order was acknowledged. |
| `refunds` | `array` | Refunds for the order. |
| `deliveryDetails` | `object` |  |
| `paymentStatus` | `string` | The status of the payment. Acceptable values are: - "`paymentCaptured`" - "`paymentRejected`" - "`paymentSecured`" - "`pendingAuthorization`"  |
| `merchantOrderId` | `string` | Merchant-provided ID of the order. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `merchantId, orderId` | Retrieves an order from your Merchant Center account. |
| `list` | `SELECT` | `merchantId` | Lists the orders in your Merchant Center account. |
| `acknowledge` | `EXEC` | `merchantId, orderId` | Marks an order as acknowledged. |
| `advancetestorder` | `EXEC` | `merchantId, orderId` | Sandbox only. Moves a test order from state "`inProgress`" to state "`pendingShipment`". |
| `cancel` | `EXEC` | `merchantId, orderId` | Cancels all line items in an order, making a full refund. |
| `cancellineitem` | `EXEC` | `merchantId, orderId` | Cancels a line item, making a full refund. |
| `canceltestorderbycustomer` | `EXEC` | `merchantId, orderId` | Sandbox only. Cancels a test order for customer-initiated cancellation. |
| `captureOrder` | `EXEC` | `merchantId, orderId` | Capture funds from the customer for the current order total. This method should be called after the merchant verifies that they are able and ready to start shipping the order. This method blocks until a response is received from the payment processsor. If this method succeeds, the merchant is guaranteed to receive funds for the order after shipment. If the request fails, it can be retried or the order may be cancelled. This method cannot be called after the entire order is already shipped. A rejected error code is returned when the payment service provider has declined the charge. This indicates a problem between the PSP and either the merchant's or customer's account. Sometimes this error will be resolved by the customer. We recommend retrying these errors once per day or cancelling the order with reason `failedToCaptureFunds` if the items cannot be held. |
| `instorerefundlineitem` | `EXEC` | `merchantId, orderId` | Deprecated. Notifies that item return and refund was handled directly by merchant outside of Google payments processing (for example, cash refund done in store). Note: We recommend calling the returnrefundlineitem method to refund in-store returns. We will issue the refund directly to the customer. This helps to prevent possible differences arising between merchant and Google transaction records. We also recommend having the point of sale system communicate with Google to ensure that customers do not receive a double refund by first refunding through Google then through an in-store return. |
| `refunditem` | `EXEC` | `merchantId, orderId` | Issues a partial or total refund for items and shipment. |
| `refundorder` | `EXEC` | `merchantId, orderId` | Issues a partial or total refund for an order. |
| `rejectreturnlineitem` | `EXEC` | `merchantId, orderId` | Rejects return on an line item. |
| `returnrefundlineitem` | `EXEC` | `merchantId, orderId` | Returns and refunds a line item. Note that this method can only be called on fully shipped orders. The Orderreturns API is the preferred way to handle returns after you receive a return from a customer. You can use Orderreturns.list or Orderreturns.get to search for the return, and then use Orderreturns.processreturn to issue the refund. If the return cannot be found, then we recommend using this API to issue a refund. |
| `setlineitemmetadata` | `EXEC` | `merchantId, orderId` | Sets (or overrides if it already exists) merchant provided annotations in the form of key-value pairs. A common use case would be to supply us with additional structured information about a line item that cannot be provided through other methods. Submitted key-value pairs can be retrieved as part of the orders resource. |
| `shiplineitems` | `EXEC` | `merchantId, orderId` | Marks line item(s) as shipped. |
| `updatelineitemshippingdetails` | `EXEC` | `merchantId, orderId` | Updates ship by and delivery by dates for a line item. |
| `updatemerchantorderid` | `EXEC` | `merchantId, orderId` | Updates the merchant order ID for a given order. |
| `updateshipment` | `EXEC` | `merchantId, orderId` | Updates a shipment's status, carrier, and/or tracking ID. |
