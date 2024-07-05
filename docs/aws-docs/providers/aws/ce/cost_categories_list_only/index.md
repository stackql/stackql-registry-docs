---
title: cost_categories_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - cost_categories_list_only
  - ce
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

Lists <code>cost_categories</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/cost_categories/"><code>cost_categories</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cost_categories_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Cost Category enables you to map your cost and usage into meaningful categories. You can use Cost Category to organize your costs using a rule-based engine.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ce.cost_categories_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Cost category ARN</td></tr>
<tr><td><CopyableCode code="effective_start" /></td><td><code>string</code></td><td>ISO 8601 date time with offset format</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rules" /></td><td><code>string</code></td><td>JSON array format of Expression in Billing and Cost Management API</td></tr>
<tr><td><CopyableCode code="split_charge_rules" /></td><td><code>string</code></td><td>Json array format of CostCategorySplitChargeRule in Billing and Cost Management API</td></tr>
<tr><td><CopyableCode code="default_value" /></td><td><code>string</code></td><td>The default value for the cost category</td></tr>
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
Lists all <code>cost_categories</code> in a region.
```sql
SELECT
region,
arn
FROM aws.ce.cost_categories_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>cost_categories_list_only</code> resource, see <a href="/providers/aws/ce/cost_categories/#permissions"><code>cost_categories</code></a>


