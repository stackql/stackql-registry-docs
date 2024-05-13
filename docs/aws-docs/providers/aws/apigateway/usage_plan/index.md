---
title: usage_plan
hide_title: false
hide_table_of_contents: false
keywords:
  - usage_plan
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


Gets or updates an individual <code>usage_plan</code> resource, use <code>usage_plans</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usage_plan</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::UsagePlan</code> resource creates a usage plan for deployed APIs. A usage plan sets a target for the throttling and quota limits on individual client API keys. For more information, see &#91;Creating and Using API Usage Plans in Amazon API Gateway&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;api-gateway-api-usage-plans.html) in the *API Gateway Developer Guide*.&lt;br&#x2F;&gt; In some cases clients can exceed the targets that you set. Don’t rely on usage plans to control costs. Consider using &#91;&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;cost-management&#x2F;latest&#x2F;userguide&#x2F;budgets-managing-costs.html) to monitor costs and &#91;&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;waf&#x2F;latest&#x2F;developerguide&#x2F;waf-chapter.html) to manage API requests.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.usage_plan" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="api_stages" /></td><td><code>array</code></td><td>The associated API stages of a usage plan.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of a usage plan.</td></tr>
<tr><td><CopyableCode code="quota" /></td><td><code>object</code></td><td>The target maximum number of permitted requests per a given unit time interval.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The collection of tags. Each tag element is associated with a given resource.</td></tr>
<tr><td><CopyableCode code="throttle" /></td><td><code>object</code></td><td>A map containing method level throttling information for API stage in a usage plan.</td></tr>
<tr><td><CopyableCode code="usage_plan_name" /></td><td><code>string</code></td><td>The name of a usage plan.</td></tr>
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
id,
api_stages,
description,
quota,
tags,
throttle,
usage_plan_name
FROM aws.apigateway.usage_plan
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## Permissions

To operate on the <code>usage_plan</code> resource, the following permissions are required:

### Read
```json
apigateway:GET
```

### Update
```json
apigateway:GET,
apigateway:DELETE,
apigateway:PATCH,
apigateway:PUT
```

