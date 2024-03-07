---
title: apis
hide_title: false
hide_table_of_contents: false
keywords:
  - apis
  - apigatewayv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>apis</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>apis</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigatewayv2.apis</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>apis</code> resource, the following permissions are required:

### Create
<pre>
apigateway:POST,
apigateway:PUT,
s3:getObject</pre>

### List
<pre>
apigateway:GET,
s3:getObject</pre>


## Example
```sql
SELECT
region,
api_id
FROM awscc.apigatewayv2.apis
WHERE region = 'us-east-1'
```
