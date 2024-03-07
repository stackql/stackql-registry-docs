---
title: request_validator
hide_title: false
hide_table_of_contents: false
keywords:
  - request_validator
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
Gets an individual <code>request_validator</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>request_validator</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>request_validator</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigateway.request_validator</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>request_validator_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of this RequestValidator</td></tr>
<tr><td><code>rest_api_id</code></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><code>validate_request_body</code></td><td><code>boolean</code></td><td>A Boolean flag to indicate whether to validate a request body according to the configured Model schema.</td></tr>
<tr><td><code>validate_request_parameters</code></td><td><code>boolean</code></td><td>A Boolean flag to indicate whether to validate request parameters (``true``) or not (``false``).</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>request_validator</code> resource, the following permissions are required:

### Update
<pre>
apigateway:PATCH,
apigateway:GET</pre>

### Delete
<pre>
apigateway:DELETE</pre>

### Read
<pre>
apigateway:GET</pre>


## Example
```sql
SELECT
region,
request_validator_id,
name,
rest_api_id,
validate_request_body,
validate_request_parameters
FROM awscc.apigateway.request_validator
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;RestApiId&gt;'
AND data__Identifier = '&lt;RequestValidatorId&gt;'
```
