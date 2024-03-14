---
title: origin_request_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_request_policy
  - cloudfront
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>origin_request_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_request_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>origin_request_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudfront.origin_request_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>last_modified_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>origin_request_policy_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
last_modified_time,
origin_request_policy_config
FROM awscc.cloudfront.origin_request_policy
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>origin_request_policy</code> resource, the following permissions are required:

### Delete
```json
cloudfront:DeleteOriginRequestPolicy,
cloudfront:GetOriginRequestPolicy
```

### Read
```json
cloudfront:GetOriginRequestPolicy
```

### Update
```json
cloudfront:UpdateOriginRequestPolicy,
cloudfront:GetOriginRequestPolicy
```

