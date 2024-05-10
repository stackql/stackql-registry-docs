---
title: usage_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - usage_plans
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


Used to retrieve a list of <code>usage_plans</code> in a region or to create or delete a <code>usage_plans</code> resource, use <code>usage_plan</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usage_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGateway::UsagePlan`` resource creates a usage plan for deployed APIs. A usage plan sets a target for the throttling and quota limits on individual client API keys. For more information, see &#91;Creating and Using API Usage Plans in Amazon API Gateway&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;api-gateway-api-usage-plans.html) in the *API Gateway Developer Guide*.&lt;br&#x2F;&gt; In some cases clients can exceed the targets that you set. Don’t rely on usage plans to control costs. Consider using &#91;&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;cost-management&#x2F;latest&#x2F;userguide&#x2F;budgets-managing-costs.html) to monitor costs and &#91;&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;waf&#x2F;latest&#x2F;developerguide&#x2F;waf-chapter.html) to manage API requests.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.usage_plans" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id
FROM aws.apigateway.usage_plans
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>usage_plan</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
-- usage_plan.iql (required properties only)
INSERT INTO aws.apigateway.usage_plans (
 ApiStages,
 Description,
 Quota,
 Tags,
 Throttle,
 UsagePlanName,
 region
)
SELECT 
'{{ ApiStages }}',
 '{{ Description }}',
 '{{ Quota }}',
 '{{ Tags }}',
 '{{ Throttle }}',
 '{{ UsagePlanName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- usage_plan.iql (all properties)
INSERT INTO aws.apigateway.usage_plans (
 ApiStages,
 Description,
 Quota,
 Tags,
 Throttle,
 UsagePlanName,
 region
)
SELECT 
 '{{ ApiStages }}',
 '{{ Description }}',
 '{{ Quota }}',
 '{{ Tags }}',
 '{{ Throttle }}',
 '{{ UsagePlanName }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: usage_plan
    props:
      - name: ApiStages
        value:
          - ApiId: '{{ ApiId }}'
            Stage: '{{ Stage }}'
            Throttle: {}
      - name: Description
        value: '{{ Description }}'
      - name: Quota
        value:
          Limit: '{{ Limit }}'
          Offset: '{{ Offset }}'
          Period: '{{ Period }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: Throttle
        value:
          BurstLimit: '{{ BurstLimit }}'
          RateLimit: null
      - name: UsagePlanName
        value: '{{ UsagePlanName }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.apigateway.usage_plans
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>usage_plans</code> resource, the following permissions are required:

### Create
```json
apigateway:POST,
apigateway:GET,
apigateway:PUT
```

### Delete
```json
apigateway:DELETE,
apigateway:GET,
apigateway:PATCH
```

### List
```json
apigateway:GET
```

