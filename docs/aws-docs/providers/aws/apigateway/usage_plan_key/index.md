---
title: usage_plan_key
hide_title: false
hide_table_of_contents: false
keywords:
  - usage_plan_key
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
Gets an individual <code>usage_plan_key</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usage_plan_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGateway::UsagePlanKey`` resource associates an API key with a usage plan. This association determines which users the usage plan is applied to.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigateway.usage_plan_key</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>key_id</code></td><td><code>string</code></td><td>The Id of the UsagePlanKey resource.</td></tr>
<tr><td><code>key_type</code></td><td><code>string</code></td><td>The type of a UsagePlanKey resource for a plan customer.</td></tr>
<tr><td><code>usage_plan_id</code></td><td><code>string</code></td><td>The Id of the UsagePlan resource representing the usage plan containing the UsagePlanKey resource representing a plan customer.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
key_id,
key_type,
usage_plan_id,
id
FROM aws.apigateway.usage_plan_key
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>usage_plan_key</code> resource, the following permissions are required:

### Read
```json
apigateway:GET
```

### Delete
```json
apigateway:DELETE,
apigateway:GET
```

