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
<tr><td><b>Id</b></td><td><code>awscc.apigateway.methods</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>rest_api_id</code></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><code>resource_id</code></td><td><code>string</code></td><td>The Resource identifier for the MethodResponse resource.</td></tr>
<tr><td><code>http_method</code></td><td><code>string</code></td><td>The method's HTTP verb.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
rest_api_id,
resource_id,
http_method
FROM awscc.apigateway.methods
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>methods</code> resource, the following permissions are required:

### Create
```json
apigateway:PUT,
apigateway:GET,
iam:PassRole
```

