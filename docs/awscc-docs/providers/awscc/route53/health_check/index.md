---
title: health_check
hide_title: false
hide_table_of_contents: false
keywords:
  - health_check
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
Gets an individual <code>health_check</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>health_check</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>health_check</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53.health_check</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>health_check_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>health_check_config</code></td><td><code>object</code></td><td>A complex type that contains information about the health check.</td></tr>
<tr><td><code>health_check_tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
health_check_id,
health_check_config,
health_check_tags
FROM awscc.route53.health_check
WHERE data__Identifier = '<HealthCheckId>';
```

## Permissions

To operate on the <code>health_check</code> resource, the following permissions are required:

### Read
```json
route53:GetHealthCheck,
route53:ListTagsForResource
```

### Update
```json
route53:UpdateHealthCheck,
route53:ChangeTagsForResource,
route53:ListTagsForResource,
cloudwatch:DescribeAlarms
```

### Delete
```json
route53:DeleteHealthCheck
```

