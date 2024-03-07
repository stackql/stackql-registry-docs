---
title: client_certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - client_certificate
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
Gets an individual <code>client_certificate</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>client_certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>client_certificate</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigateway.client_certificate</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>client_certificate_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the client certificate.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The collection of tags. Each tag element is associated with a given resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>client_certificate</code> resource, the following permissions are required:

### Read
```json
apigateway:GET
```

### Update
```json
apigateway:GET,
apigateway:PATCH,
apigateway:PUT,
apigateway:DELETE
```

### Delete
```json
apigateway:DELETE
```


## Example
```sql
SELECT
region,
client_certificate_id,
description,
tags
FROM awscc.apigateway.client_certificate
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ClientCertificateId&gt;'
```
