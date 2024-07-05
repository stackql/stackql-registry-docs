---
title: usage_plan_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - usage_plan_tags
  - apigateway
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

Expands all tag keys and values for <code>usage_plans</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usage_plan_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::UsagePlan</code> resource creates a usage plan for deployed APIs. A usage plan sets a target for the throttling and quota limits on individual client API keys. For more information, see &#91;Creating and Using API Usage Plans in Amazon API Gateway&#93;(https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html) in the *API Gateway Developer Guide*.<br />In some cases clients can exceed the targets that you set. Don’t rely on usage plans to control costs. Consider using &#91;&#93;(https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) to monitor costs and &#91;&#93;(https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) to manage API requests.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.usage_plan_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="api_stages" /></td><td><code>array</code></td><td>The associated API stages of a usage plan.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of a usage plan.</td></tr>
<tr><td><CopyableCode code="quota" /></td><td><code>object</code></td><td>The target maximum number of permitted requests per a given unit time interval.</td></tr>
<tr><td><CopyableCode code="throttle" /></td><td><code>object</code></td><td>A map containing method level throttling information for API stage in a usage plan.</td></tr>
<tr><td><CopyableCode code="usage_plan_name" /></td><td><code>string</code></td><td>The name of a usage plan.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>usage_plans</code> in a region.
```sql
SELECT
region,
id,
api_stages,
description,
quota,
throttle,
usage_plan_name,
tag_key,
tag_value
FROM aws.apigateway.usage_plan_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>usage_plan_tags</code> resource, see <a href="/providers/aws/apigateway/usage_plans/#permissions"><code>usage_plans</code></a>


