---
title: origin_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_endpoints
  - mediapackage
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>origin_endpoints</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>origin_endpoints</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.mediapackage.origin_endpoints</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The ID of the OriginEndpoint.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>origin_endpoints</code> resource, the following permissions are required:

### Create
```json
mediapackage:CreateOriginEndpoint,
mediapackage:DescribeOriginEndpoint,
mediapackage:DescribeChannel,
mediapackage:TagResource,
iam:PassRole,
acm:DescribeCertificate
```

### List
```json
mediapackage:ListOriginEndpoints
```


## Example
```sql
SELECT
region,
id
FROM awscc.mediapackage.origin_endpoints
WHERE region = 'us-east-1'
```
