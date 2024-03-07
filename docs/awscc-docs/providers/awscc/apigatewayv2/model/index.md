---
title: model
hide_title: false
hide_table_of_contents: false
keywords:
  - model
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
Gets an individual <code>model</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>model</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigatewayv2.model</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>model_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the model.</td></tr>
<tr><td><code>content_type</code></td><td><code>string</code></td><td>The content-type for the model, for example, "application&#x2F;json".</td></tr>
<tr><td><code>schema</code></td><td><code>object</code></td><td>The schema for the model. For application&#x2F;json models, this should be JSON schema draft 4 model.</td></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td>The API identifier.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the model.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>model</code> resource, the following permissions are required:

### Update
<pre>
apigateway:PATCH,
apigateway:GET,
apigateway:PUT</pre>

### Read
<pre>
apigateway:GET</pre>

### Delete
<pre>
apigateway:GET,
apigateway:DELETE</pre>


## Example
```sql
SELECT
region,
model_id,
description,
content_type,
schema,
api_id,
name
FROM awscc.apigatewayv2.model
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ApiId&gt;'
AND data__Identifier = '&lt;ModelId&gt;'
```
