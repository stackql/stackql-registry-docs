---
title: stages
hide_title: false
hide_table_of_contents: false
keywords:
  - stages
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
Retrieves a list of <code>stages</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGateway::Stage`` resource creates a stage for a deployment.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigateway.stages</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>rest_api_id</code></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><code>stage_name</code></td><td><code>string</code></td><td>The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
rest_api_id,
stage_name
FROM aws.apigateway.stages
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>stages</code> resource, the following permissions are required:

### Create
```json
apigateway:POST,
apigateway:PATCH,
apigateway:GET,
apigateway:PUT
```

### List
```json
apigateway:GET
```

