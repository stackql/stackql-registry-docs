---
title: documentation_part
hide_title: false
hide_table_of_contents: false
keywords:
  - documentation_part
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
Gets an individual <code>documentation_part</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>documentation_part</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>documentation_part</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigateway.documentation_part</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>documentation_part_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>location</code></td><td><code>object</code></td><td>The location of the targeted API entity of the to-be-created documentation part.</td></tr>
<tr><td><code>properties</code></td><td><code>string</code></td><td>The new documentation content map of the targeted API entity. Enclosed key-value pairs are API-specific, but only OpenAPI-compliant key-value pairs can be exported and, hence, published.</td></tr>
<tr><td><code>rest_api_id</code></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
documentation_part_id,
location,
properties,
rest_api_id
FROM awscc.apigateway.documentation_part
WHERE data__Identifier = '<DocumentationPartId>|<RestApiId>';
```

## Permissions

To operate on the <code>documentation_part</code> resource, the following permissions are required:

### Read
```json
apigateway:GET
```

### Update
```json
apigateway:GET,
apigateway:PATCH
```

### Delete
```json
apigateway:DELETE
```

