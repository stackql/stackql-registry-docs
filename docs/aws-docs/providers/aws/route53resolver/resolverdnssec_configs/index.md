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
Used to retrieve a list of <code>resolverdnssec_configs</code> in a region or create a <code>resolverdnssec_configs</code> resource, use <code>resolverdnssec_config</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolverdnssec_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53Resolver::ResolverDNSSECConfig.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53resolver.resolverdnssec_configs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id
FROM aws.route53resolver.resolverdnssec_configs
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>resolverdnssec_configs</code> resource, the following permissions are required:

### Create
```json
resolverdnssec:CreateConfig,
route53resolver:UpdateResolverDnssecConfig,
route53resolver:GetResolverDnssecConfig,
ec2:DescribeVpcs
```

### List
```json
resolverdnssec:ListConfig,
route53resolver:ListResolverDnssecConfigs
```

