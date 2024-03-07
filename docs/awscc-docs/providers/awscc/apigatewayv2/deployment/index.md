---
title: deployment
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment
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
Gets an individual <code>deployment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>deployment</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigatewayv2.deployment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>deployment_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description for the deployment resource.</td></tr>
<tr><td><code>stage_name</code></td><td><code>string</code></td><td>The name of an existing stage to associate with the deployment.</td></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td>The API identifier.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
deployment_id,
description,
stage_name,
api_id
FROM awscc.apigatewayv2.deployment
WHERE region = 'us-east-1'
AND data__Identifier = '{ApiId}';
AND data__Identifier = '{DeploymentId}';
```

## Permissions

To operate on the <code>deployment</code> resource, the following permissions are required:

### Update
```json
apigateway:PATCH,
apigateway:GET,
apigateway:PUT
```

### Read
```json
apigateway:GET
```

### Delete
```json
apigateway:GET,
apigateway:DELETE
```

