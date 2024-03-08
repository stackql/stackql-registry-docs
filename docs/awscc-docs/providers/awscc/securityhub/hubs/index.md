---
title: hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - hubs
  - securityhub
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>hubs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>hubs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.securityhub.hubs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>An ARN is automatically created for the customer.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
a_rn
FROM awscc.securityhub.hubs
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>hubs</code> resource, the following permissions are required:

### Create
```json
securityhub:EnableSecurityHub,
securityhub:UpdateSecurityHubConfiguration,
securityhub:TagResource,
securityhub:ListTagsForResource
```

### List
```json
securityhub:DescribeHub,
securityhub:ListTagsForResource
```

