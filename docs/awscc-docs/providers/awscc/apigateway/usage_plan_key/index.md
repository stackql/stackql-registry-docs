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
<tr><td><b>Description</b></td><td>usage_plan_key</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigateway.usage_plan_key</code></td></tr>
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
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
key_id,
key_type,
usage_plan_id,
id
FROM awscc.apigateway.usage_plan_key
WHERE region = 'us-east-1'
AND data__Identifier = '{Id}';
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

