---
title: client_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - client_certificates
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
Retrieves a list of <code>client_certificates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>client_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>client_certificates</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigateway.client_certificates</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>client_certificate_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>client_certificates</code> resource, the following permissions are required:

### Create
<pre>
apigateway:POST,
apigateway:GET,
apigateway:PUT</pre>

### List
<pre>
apigateway:GET</pre>


## Example
```sql
SELECT
region,
client_certificate_id
FROM awscc.apigateway.client_certificates
WHERE region = 'us-east-1'
```
