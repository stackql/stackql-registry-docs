---
title: version
hide_title: false
hide_table_of_contents: false
keywords:
  - version
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
Gets an individual <code>version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>version</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lambda.version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>function_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>provisioned_concurrency_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>code_sha256</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
function_name,
provisioned_concurrency_config,
description,
id,
code_sha256,
version
FROM aws.lambda.version
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```