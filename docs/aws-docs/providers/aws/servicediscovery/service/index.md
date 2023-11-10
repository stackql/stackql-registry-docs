---
title: service
hide_title: false
hide_table_of_contents: false
keywords:
  - service
  - servicediscovery
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>service</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>service</td></tr>
<tr><td><b>Id</b></td><td><code>aws.servicediscovery.service</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>health_check_custom_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>dns_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>namespace_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>health_check_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
type,
description,
health_check_custom_config,
dns_config,
id,
namespace_id,
health_check_config,
arn,
tags,
name
FROM aws.servicediscovery.service
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
