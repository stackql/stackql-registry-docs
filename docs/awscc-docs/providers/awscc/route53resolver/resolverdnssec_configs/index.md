---
title: resolverdnssec_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - resolverdnssec_configs
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
Retrieves a list of <code>resolverdnssec_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolverdnssec_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resolverdnssec_configs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53resolver.resolverdnssec_configs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>resolverdnssec_configs</code> resource, the following permissions are required:

### Create
<pre>
resolverdnssec:CreateConfig,
route53resolver:UpdateResolverDnssecConfig,
route53resolver:GetResolverDnssecConfig,
ec2:DescribeVpcs</pre>

### List
<pre>
resolverdnssec:ListConfig,
route53resolver:ListResolverDnssecConfigs</pre>


## Example
```sql
SELECT
region,
id
FROM awscc.route53resolver.resolverdnssec_configs
WHERE region = 'us-east-1'
```
