---
title: security_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - security_configuration
  - emr
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>security_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>security_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.emr.security_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the security configuration.</td></tr>
<tr><td><code>security_configuration</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
security_configuration
FROM aws.emr.security_configuration
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Name&gt;'
```
