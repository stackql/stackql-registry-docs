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
<tr><td><b>Id</b></td><td><code>aws.apigateway.request_validator</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>RequestValidatorId</code></td><td><code>string</code></td><td>ID of the request validator.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Name of the request validator.</td></tr>
<tr><td><code>RestApiId</code></td><td><code>string</code></td><td>The identifier of the targeted API entity.</td></tr>
<tr><td><code>ValidateRequestBody</code></td><td><code>boolean</code></td><td>Indicates whether to validate the request body according to the configured schema for the targeted API and method. </td></tr>
<tr><td><code>ValidateRequestParameters</code></td><td><code>boolean</code></td><td>Indicates whether to validate request parameters.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.apigateway.request_validator
WHERE region = 'us-east-1' AND data__Identifier = '&lt;RestApiId&gt;' AND data__Identifier = '&lt;RequestValidatorId&gt;'
</pre>
