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
Gets an individual <code>usage_plan</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usage_plan</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>usage_plan</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigateway.usage_plan</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>api_stages</code></td><td><code>array</code></td><td>The associated API stages of a usage plan.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of a usage plan.</td></tr>
<tr><td><code>quota</code></td><td><code>object</code></td><td>The target maximum number of permitted requests per a given unit time interval.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The collection of tags. Each tag element is associated with a given resource.</td></tr>
<tr><td><code>throttle</code></td><td><code>object</code></td><td>A map containing method level throttling information for API stage in a usage plan.</td></tr>
<tr><td><code>usage_plan_name</code></td><td><code>string</code></td><td>The name of a usage plan.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.apigateway.usage_plan
WHERE data__Identifier = '<Id>';
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

### Delete
```json
apigateway:DELETE,
apigateway:GET,
apigateway:PATCH
```

