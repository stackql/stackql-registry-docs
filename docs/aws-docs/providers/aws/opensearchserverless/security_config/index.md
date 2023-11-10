---
title: security_config
hide_title: false
hide_table_of_contents: false
keywords:
  - security_config
  - opensearchserverless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>security_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>security_config</td></tr>
<tr><td><b>Id</b></td><td><code>aws.opensearchserverless.security_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Security config description</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The identifier of the security config</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The friendly name of the security config</td></tr>
<tr><td><code>saml_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
id,
name,
saml_options,
type
FROM aws.opensearchserverless.security_config
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
