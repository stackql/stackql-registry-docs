---
title: resolverdnssec_config
hide_title: false
hide_table_of_contents: false
keywords:
  - resolverdnssec_config
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
Gets or operates on an individual <code>resolverdnssec_config</code> resource, use <code>resolverdnssec_configs</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolverdnssec_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53Resolver::ResolverDNSSECConfig.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53resolver.resolverdnssec_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id</td></tr>
<tr><td><code>owner_id</code></td><td><code>string</code></td><td>AccountId</td></tr>
<tr><td><code>resource_id</code></td><td><code>string</code></td><td>ResourceId</td></tr>
<tr><td><code>validation_status</code></td><td><code>string</code></td><td>ResolverDNSSECValidationStatus, possible values are ENABLING, ENABLED, DISABLING AND DISABLED.</td></tr>
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
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id,
owner_id,
resource_id,
validation_status
FROM aws.route53resolver.resolverdnssec_config
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>resolverdnssec_config</code> resource, the following permissions are required:

### Read
```json
resolverdnssec:GetConfig,
route53resolver:ListResolverDnssecConfigs
```

### Delete
```json
resolverdnssec:DeleteConfig,
route53resolver:UpdateResolverDnssecConfig,
route53resolver:ListResolverDnssecConfigs,
ec2:DescribeVpcs
```

