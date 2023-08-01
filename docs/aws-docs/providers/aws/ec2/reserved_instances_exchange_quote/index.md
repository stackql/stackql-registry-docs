---
title: reserved_instances_exchange_quote
hide_title: false
hide_table_of_contents: false
keywords:
  - reserved_instances_exchange_quote
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reserved_instances_exchange_quote</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.reserved_instances_exchange_quote</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `validationFailureReason` | `string` | Describes the reason why the exchange cannot be completed. |
| `reservedInstanceValueSet` | `array` | The configuration of your Convertible Reserved Instances. |
| `currencyCode` | `string` | The currency of the transaction. |
| `outputReservedInstancesWillExpireAt` | `string` | The new end date of the reservation term. |
| `targetConfigurationValueRollup` | `object` | The cost associated with the Reserved Instance. |
| `isValidExchange` | `boolean` | If &lt;code&gt;true&lt;/code&gt;, the exchange is valid. If &lt;code&gt;false&lt;/code&gt;, the exchange cannot be completed. |
| `reservedInstanceValueRollup` | `object` | The cost associated with the Reserved Instance. |
| `paymentDue` | `string` | The total true upfront charge for the exchange. |
| `targetConfigurationValueSet` | `array` | The values of the target Convertible Reserved Instances. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `reserved_instances_exchange_quote_Get` | `SELECT` | `ReservedInstanceId, region` | Returns a quote and exchange information for exchanging one or more specified Convertible Reserved Instances for a new Convertible Reserved Instance. If the exchange cannot be performed, the reason is returned in the response. Use &lt;a&gt;AcceptReservedInstancesExchangeQuote&lt;/a&gt; to perform the exchange. |
| `reserved_instances_exchange_quote_Accept` | `EXEC` | `ReservedInstanceId, region` | Accepts the Convertible Reserved Instance exchange quote described in the &lt;a&gt;GetReservedInstancesExchangeQuote&lt;/a&gt; call. |
