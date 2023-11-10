---
title: request_validators
hide_title: false
hide_table_of_contents: false
keywords:
  - request_validators
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
Retrieves a list of <code>request_validators</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>request_validators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>request_validators</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigateway.request_validators</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>rest_api_id</code></td><td><code>string</code></td><td>The identifier of the targeted API entity.</td></tr>
<tr><td><code>request_validator_id</code></td><td><code>string</code></td><td>ID of the request validator.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
rest_api_id,
request_validator_id
FROM aws.apigateway.request_validators
WHERE region = 'us-east-1'
```
