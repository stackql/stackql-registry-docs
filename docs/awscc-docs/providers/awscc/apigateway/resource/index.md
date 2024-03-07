---
title: resource
hide_title: false
hide_table_of_contents: false
keywords:
  - resource
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
Gets an individual <code>resource</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigateway.resource</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>resource_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>rest_api_id</code></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><code>parent_id</code></td><td><code>string</code></td><td>The parent resource's identifier.</td></tr>
<tr><td><code>path_part</code></td><td><code>string</code></td><td>The last path segment for this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>resource</code> resource, the following permissions are required:

### Read
<pre>
apigateway:GET</pre>

### Update
<pre>
apigateway:GET,
apigateway:PATCH</pre>

### Delete
<pre>
apigateway:DELETE</pre>


## Example
```sql
SELECT
region,
resource_id,
rest_api_id,
parent_id,
path_part
FROM awscc.apigateway.resource
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;RestApiId&gt;'
AND data__Identifier = '&lt;ResourceId&gt;'
```
