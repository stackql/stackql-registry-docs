---
title: api_mapping
hide_title: false
hide_table_of_contents: false
keywords:
  - api_mapping
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
Gets or operates on an individual <code>api_mapping</code> resource, use <code>api_mappings</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_mapping</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGatewayV2::ApiMapping`` resource contains an API mapping. An API mapping relates a path of your custom domain name to a stage of your API. A custom domain name can have multiple API mappings, but the paths can't overlap. A custom domain can map only to APIs of the same protocol type. For more information, see &#91;CreateApiMapping&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigatewayv2&#x2F;latest&#x2F;api-reference&#x2F;domainnames-domainname-apimappings.html#CreateApiMapping) in the *Amazon API Gateway V2 API Reference*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.api_mapping</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>api_mapping_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td>The domain name.</td></tr>
<tr><td><code>stage</code></td><td><code>string</code></td><td>The API stage.</td></tr>
<tr><td><code>api_mapping_key</code></td><td><code>string</code></td><td>The API mapping key.</td></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td>The identifier of the API.</td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
api_mapping_id,
domain_name,
stage,
api_mapping_key,
api_id
FROM aws.apigatewayv2.api_mapping
WHERE data__Identifier = '<ApiMappingId>|<DomainName>';
```

## Permissions

To operate on the <code>api_mapping</code> resource, the following permissions are required:

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
apigateway:DELETE
```

