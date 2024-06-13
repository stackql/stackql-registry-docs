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

Creates, updates, deletes or gets an <code>usage_plan</code> resource or lists <code>usage_plans</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usage_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::UsagePlan</code> resource creates a usage plan for deployed APIs. A usage plan sets a target for the throttling and quota limits on individual client API keys. For more information, see &#91;Creating and Using API Usage Plans in Amazon API Gateway&#93;(https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html) in the *API Gateway Developer Guide*.<br />In some cases clients can exceed the targets that you set. Don’t rely on usage plans to control costs. Consider using &#91;&#93;(https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) to monitor costs and &#91;&#93;(https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) to manage API requests.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.usage_plans" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>usage_plans</code> in a region.
```sql
SELECT
region,
id
FROM aws.apigateway.usage_plans
WHERE region = 'us-east-1';
```
Gets all properties from an <code>usage_plan</code>.
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
FROM aws.apigateway.usage_plans
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

