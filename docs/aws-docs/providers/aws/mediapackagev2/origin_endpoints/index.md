---
title: origin_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_endpoints
  - mediapackagev2
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
<tr><td><b>Description</b></td><td>&lt;p&gt;Represents an origin endpoint that is associated with a channel, offering a dynamically repackaged version of its content through various streaming media protocols. The content can be efficiently disseminated to end-users via a Content Delivery Network (CDN), like Amazon CloudFront.&lt;&#x2F;p&gt;</td></tr>
<tr><td><b>Id</b></td><td><code>aws.mediapackagev2.origin_endpoints</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Resource Name (ARN) associated with the resource.&lt;&#x2F;p&gt;</td></tr>
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
arn
FROM aws.mediapackagev2.origin_endpoints
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>origin_endpoints</code> resource, the following permissions are required:

### Create
```json
mediapackagev2:TagResource,
mediapackagev2:CreateOriginEndpoint,
iam:PassRole
```

### List
```json
mediapackagev2:ListOriginEndpoints
```

