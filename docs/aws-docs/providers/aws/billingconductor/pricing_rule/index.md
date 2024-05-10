---
title: pricing_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - pricing_rule
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


Gets or updates an individual <code>pricing_rule</code> resource, use <code>pricing_rules</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pricing_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A markup&#x2F;discount that is defined for a specific set of services that can later be associated with a pricing plan.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.billingconductor.pricing_rule" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Pricing rule ARN</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
name,
description,
scope,
type,
modifier_percentage,
service,
billing_entity,
tiering,
usage_type,
operation,
associated_pricing_plan_count,
creation_time,
last_modified_time,
tags
FROM aws.billingconductor.pricing_rule
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## Permissions

To operate on the <code>pricing_rule</code> resource, the following permissions are required:

### Read
```json
billingconductor:ListPricingRules,
billingconductor:ListTagsForResource
```

### Update
```json
billingconductor:UpdatePricingRule,
billingconductor:ListPricingRules,
billingconductor:TagResource,
billingconductor:UntagResource
```

