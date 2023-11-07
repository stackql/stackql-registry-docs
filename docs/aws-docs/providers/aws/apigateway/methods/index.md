---
title: methods
hide_title: false
hide_table_of_contents: false
keywords:
  - methods
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
Retrieves a list of <code>methods</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>methods</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>methods</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigateway.methods</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ApiKeyRequired</code></td><td><code>boolean</code></td><td>Indicates whether the method requires clients to submit a valid API key.</td></tr>
<tr><td><code>AuthorizationScopes</code></td><td><code>array</code></td><td>A list of authorization scopes configured on the method.</td></tr>
<tr><td><code>AuthorizationType</code></td><td><code>string</code></td><td>The method's authorization type.</td></tr>
<tr><td><code>AuthorizerId</code></td><td><code>string</code></td><td>The identifier of the authorizer to use on this method.</td></tr>
<tr><td><code>HttpMethod</code></td><td><code>string</code></td><td>The backend system that the method calls when it receives a request.</td></tr>
<tr><td><code>Integration</code></td><td><code>undefined</code></td><td>The backend system that the method calls when it receives a request.</td></tr>
<tr><td><code>MethodResponses</code></td><td><code>array</code></td><td>The responses that can be sent to the client who calls the method.</td></tr>
<tr><td><code>OperationName</code></td><td><code>string</code></td><td>A friendly operation name for the method.</td></tr>
<tr><td><code>RequestModels</code></td><td><code>object</code></td><td>The resources that are used for the request's content type. Specify request models as key-value pairs (string-to-string mapping), with a content type as the key and a Model resource name as the value.</td></tr>
<tr><td><code>RequestParameters</code></td><td><code>object</code></td><td>The request parameters that API Gateway accepts. Specify request parameters as key-value pairs (string-to-Boolean mapping), with a source as the key and a Boolean as the value.</td></tr>
<tr><td><code>RequestValidatorId</code></td><td><code>string</code></td><td>The ID of the associated request validator.</td></tr>
<tr><td><code>ResourceId</code></td><td><code>string</code></td><td>The ID of an API Gateway resource.</td></tr>
<tr><td><code>RestApiId</code></td><td><code>string</code></td><td>The ID of the RestApi resource in which API Gateway creates the method.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.apigateway.methods<br/>WHERE region = 'us-east-1'
</pre>
