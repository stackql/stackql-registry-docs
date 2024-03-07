---
title: api_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - api_mappings
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
Retrieves a list of <code>api_mappings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>api_mappings</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigatewayv2.api_mappings</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>api_mapping_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td>The domain name.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
api_mapping_id,
domain_name
FROM awscc.apigatewayv2.api_mappings
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>api_mappings</code> resource, the following permissions are required:

### Create
```json
apigateway:POST
```

### List
```json
apigateway:GET
```

