---
title: base_path_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - base_path_mappings
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
Retrieves a list of <code>base_path_mappings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>base_path_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>base_path_mappings</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigateway.base_path_mappings</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>BasePath</code></td><td><code>string</code></td><td>The base path name that callers of the API must provide in the URL after the domain name.</td></tr>
<tr><td><code>DomainName</code></td><td><code>string</code></td><td>The DomainName of an AWS::ApiGateway::DomainName resource.</td></tr>
<tr><td><code>RestApiId</code></td><td><code>string</code></td><td>The ID of the API.</td></tr>
<tr><td><code>Stage</code></td><td><code>string</code></td><td>The name of the API's stage.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.apigateway.base_path_mappings
WHERE region = 'us-east-1'
</pre>
