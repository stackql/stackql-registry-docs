---
title: public_dns_namespace
hide_title: false
hide_table_of_contents: false
keywords:
  - public_dns_namespace
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
Gets an individual <code>public_dns_namespace</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>public_dns_namespace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>public_dns_namespace</td></tr>
<tr><td><b>Id</b></td><td><code>aws.servicediscovery.public_dns_namespace</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>hosted_zone_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>properties</code></td><td><code>object</code></td><td></td></tr>
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
description,
hosted_zone_id,
id,
arn,
properties,
tags,
name
FROM aws.servicediscovery.public_dns_namespace
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
