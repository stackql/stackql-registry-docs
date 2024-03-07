---
title: rest_apis
hide_title: false
hide_table_of_contents: false
keywords:
  - rest_apis
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
Retrieves a list of <code>rest_apis</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rest_apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>rest_apis</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigateway.rest_apis</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>rest_api_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
rest_api_id
FROM awscc.apigateway.rest_apis
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>rest_apis</code> resource, the following permissions are required:

### Create
```json
apigateway:GET,
apigateway:POST,
apigateway:PUT,
apigateway:PATCH,
apigateway:UpdateRestApiPolicy,
s3:GetObject,
iam:PassRole
```

### List
```json
apigateway:GET
```

