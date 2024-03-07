---
title: hosted_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - hosted_zones
  - route53
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>hosted_zones</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hosted_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>hosted_zones</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53.hosted_zones</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id
FROM awscc.route53.hosted_zones

```

## Permissions

To operate on the <code>hosted_zones</code> resource, the following permissions are required:

### Create
```json
route53:CreateHostedZone,
route53:CreateQueryLoggingConfig,
route53:ChangeTagsForResource,
route53:GetChange,
route53:AssociateVPCWithHostedZone,
ec2:DescribeVpcs
```

### List
```json
route53:GetHostedZone,
route53:ListHostedZones,
route53:ListHostedZonesByName,
route53:ListQueryLoggingConfigs,
route53:ListTagsForResource
```

