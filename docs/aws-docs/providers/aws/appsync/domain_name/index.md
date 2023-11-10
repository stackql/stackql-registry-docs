---
title: domain_name
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_name
  - appsync
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>domain_name</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_name</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>domain_name</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appsync.domain_name</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>certificate_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>app_sync_domain_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>hosted_zone_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
domain_name,
description,
certificate_arn,
app_sync_domain_name,
hosted_zone_id
FROM aws.appsync.domain_name
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DomainName&gt;'
```
