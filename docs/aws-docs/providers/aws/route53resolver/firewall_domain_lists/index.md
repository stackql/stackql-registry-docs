---
title: firewall_domain_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_domain_lists
  - route53resolver
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>firewall_domain_lists</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_domain_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>firewall_domain_lists</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53resolver.firewall_domain_lists</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>ResourceId</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id
FROM aws.route53resolver.firewall_domain_lists
WHERE region = 'us-east-1'
```
