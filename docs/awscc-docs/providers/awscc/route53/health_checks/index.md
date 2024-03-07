---
title: health_checks
hide_title: false
hide_table_of_contents: false
keywords:
  - health_checks
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
Retrieves a list of <code>health_checks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>health_checks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>health_checks</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53.health_checks</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>health_check_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
health_check_id
FROM awscc.route53.health_checks

```

## Permissions

To operate on the <code>health_checks</code> resource, the following permissions are required:

### Create
```json
route53:CreateHealthCheck,
route53:ChangeTagsForResource,
cloudwatch:DescribeAlarms,
route53-recovery-control-config:DescribeRoutingControl
```

### List
```json
route53:ListHealthChecks,
route53:ListTagsForResource
```

