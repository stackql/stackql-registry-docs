---
title: repricingrules
hide_title: false
hide_table_of_contents: false
keywords:
  - repricingrules
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
<tr><td><b>Name</b></td><td><code>repricingrules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.repricingrules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `merchantId` | `string` | Output only. Immutable. Merchant that owns the repricing rule. |
| `countryCode` | `string` | Required. Immutable. [CLDR country code](http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml) (e.g. "US"). |
| `languageCode` | `string` | Required. Immutable. The two-letter ISO 639-1 language code associated with the repricing rule. |
| `type` | `string` | Required. Immutable. The type of the rule. |
| `paused` | `boolean` | Represents whether a rule is paused. A paused rule will behave like a non-paused rule within CRUD operations, with the major difference that a paused rule will not be evaluated and will have no effect on offers. |
| `ruleId` | `string` | Output only. Immutable. The ID to uniquely identify each repricing rule. |
| `statsBasedRule` | `object` | Definition of stats based rule. |
| `cogsBasedRule` | `object` | A repricing rule that changes the sale price based on cost of goods sale. |
| `restriction` | `object` | Definition of a rule restriction. At least one of the following needs to be true: (1) use_auto_pricing_min_price is true (2) floor.price_delta exists (3) floor.percentage_delta exists If floor.price_delta and floor.percentage_delta are both set on a rule, the highest value will be chosen by the Repricer. In other words, for a product with a price of $50, if the `floor.percentage_delta` is "-10" and the floor.price_delta is "-12", the offer price will only be lowered $5 (10% lower than the original offer price). |
| `effectiveTimePeriod` | `object` |  |
| `eligibleOfferMatcher` | `object` | Matcher that specifies eligible offers. When the USE_FEED_ATTRIBUTE option is selected, only the repricing_rule_id attribute on the product feed is used to specify offer-rule mapping. When the CUSTOM_FILTER option is selected, only the *_matcher fields are used to filter the offers for offer-rule mapping. If the CUSTOM_FILTER option is selected, an offer needs to satisfy each custom filter matcher to be eligible for a rule. Size limit: the sum of the number of entries in all the matchers should not exceed 20. For example, there can be 15 product ids and 5 brands, but not 10 product ids and 11 brands. |
| `title` | `string` | The title for the rule. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `merchantId, ruleId` | Retrieves a repricing rule from your Merchant Center account. |
| `list` | `SELECT` | `merchantId` | Lists the repricing rules in your Merchant Center account. |
| `create` | `INSERT` | `merchantId` | Creates a repricing rule for your Merchant Center account. |
| `delete` | `DELETE` | `merchantId, ruleId` | Deletes a repricing rule in your Merchant Center account. |
| `patch` | `EXEC` | `merchantId, ruleId` | Updates a repricing rule in your Merchant Center account. All mutable fields will be overwritten in each update request. In each update, you must provide all required mutable fields, or an error will be thrown. If you do not provide an optional field in the update request, if that field currently exists, it will be deleted from the rule. |
