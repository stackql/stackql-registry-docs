---
title: server
hide_title: false
hide_table_of_contents: false
keywords:
  - server
  - transfer
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>server</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>server</td></tr>
<tr><td><b>Id</b></td><td><code>aws.transfer.server</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>logging_role</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>protocols</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>identity_provider_details</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>endpoint_details</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>pre_authentication_login_banner</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>server_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>post_authentication_login_banner</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>endpoint_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>security_policy_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>protocol_details</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>workflow_details</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>identity_provider_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>certificate</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
logging_role,
protocols,
identity_provider_details,
endpoint_details,
pre_authentication_login_banner,
server_id,
post_authentication_login_banner,
endpoint_type,
security_policy_name,
protocol_details,
workflow_details,
arn,
domain,
identity_provider_type,
tags,
certificate
FROM aws.transfer.server
WHERE region = 'us-east-1'
AND data__Identifier = '<ServerId>'
```
