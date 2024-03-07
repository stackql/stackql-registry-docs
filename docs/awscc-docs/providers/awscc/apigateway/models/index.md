---
title: models
hide_title: false
hide_table_of_contents: false
keywords:
  - models
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
Retrieves a list of <code>models</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>models</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigateway.models</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>rest_api_id</code></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>A name for the model. If you don't specify a name, CFN generates a unique physical ID and uses that ID for the model name. For more information, see &#91;Name Type&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-name.html).&lt;br&#x2F;&gt;  If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>models</code> resource, the following permissions are required:

### Create
<pre>
apigateway:POST,
apigateway:GET</pre>

### List
<pre>
apigateway:GET</pre>


## Example
```sql
SELECT
region,
rest_api_id,
name
FROM awscc.apigateway.models
WHERE region = 'us-east-1'
```
