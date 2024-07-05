---
title: pricing_rules_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - pricing_rules_list_only
  - billingconductor
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>pricing_rules</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/pricing_rules/"><code>pricing_rules</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pricing_rules_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A markup/discount that is defined for a specific set of services that can later be associated with a pricing plan.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.billingconductor.pricing_rules_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Pricing rule ARN</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Pricing rule name</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Pricing rule description</td></tr>
<tr><td><CopyableCode code="scope" /></td><td><code>string</code></td><td>A term used to categorize the granularity of a Pricing Rule.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>One of MARKUP, DISCOUNT or TIERING that describes the behaviour of the pricing rule.</td></tr>
<tr><td><CopyableCode code="modifier_percentage" /></td><td><code>number</code></td><td>Pricing rule modifier percentage</td></tr>
<tr><td><CopyableCode code="service" /></td><td><code>string</code></td><td>The service which a pricing rule is applied on</td></tr>
<tr><td><CopyableCode code="billing_entity" /></td><td><code>string</code></td><td>The seller of services provided by AWS, their affiliates, or third-party providers selling services via AWS Marketplaces. Supported billing entities are AWS, AWS Marketplace, and AISPL.</td></tr>
<tr><td><CopyableCode code="tiering" /></td><td><code>object</code></td><td>The set of tiering configurations for the pricing rule.</td></tr>
<tr><td><CopyableCode code="usage_type" /></td><td><code>string</code></td><td>The UsageType which a SKU pricing rule is modifying</td></tr>
<tr><td><CopyableCode code="operation" /></td><td><code>string</code></td><td>The Operation which a SKU pricing rule is modifying</td></tr>
<tr><td><CopyableCode code="associated_pricing_plan_count" /></td><td><code>integer</code></td><td>The number of pricing plans associated with pricing rule</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>integer</code></td><td>Creation timestamp in UNIX epoch time format</td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>integer</code></td><td>Latest modified timestamp in UNIX epoch time format</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>pricing_rules</code> in a region.
```sql
SELECT
region,
arn
FROM aws.billingconductor.pricing_rules_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>pricing_rules_list_only</code> resource, see <a href="/providers/aws/billingconductor/pricing_rules/#permissions"><code>pricing_rules</code></a>


