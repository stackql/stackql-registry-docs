---
title: permission
hide_title: false
hide_table_of_contents: false
keywords:
  - permission
  - lambda
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>permission</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permission</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>permission</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lambda.permission</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>function_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>action</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>event_source_token</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>function_url_auth_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source_account</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>principal_org_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>principal</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
function_name,
action,
event_source_token,
function_url_auth_type,
source_arn,
source_account,
principal_org_id,
id,
principal
FROM aws.lambda.permission
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
