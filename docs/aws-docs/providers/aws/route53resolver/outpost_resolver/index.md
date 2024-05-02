---
title: outpost_resolver
hide_title: false
hide_table_of_contents: false
keywords:
  - outpost_resolver
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
Gets an individual <code>outpost_resolver</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>outpost_resolver</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53Resolver::OutpostResolver.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53resolver.outpost_resolver</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id</td></tr>
<tr><td><code>creator_request_id</code></td><td><code>string</code></td><td>The id of the creator request.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The OutpostResolver name.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The OutpostResolver ARN.</td></tr>
<tr><td><code>outpost_arn</code></td><td><code>string</code></td><td>The Outpost ARN.</td></tr>
<tr><td><code>preferred_instance_type</code></td><td><code>string</code></td><td>The OutpostResolver instance type.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The OutpostResolver status, possible values are CREATING, OPERATIONAL, UPDATING, DELETING, ACTION_NEEDED, FAILED_CREATION and FAILED_DELETION.</td></tr>
<tr><td><code>status_message</code></td><td><code>string</code></td><td>The OutpostResolver status message.</td></tr>
<tr><td><code>instance_count</code></td><td><code>integer</code></td><td>The number of OutpostResolvers.</td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>The OutpostResolver creation time</td></tr>
<tr><td><code>modification_time</code></td><td><code>string</code></td><td>The OutpostResolver last modified time</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
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
creator_request_id,
name,
arn,
outpost_arn,
preferred_instance_type,
status,
status_message,
instance_count,
creation_time,
modification_time,
tags
FROM aws.route53resolver.outpost_resolver
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>outpost_resolver</code> resource, the following permissions are required:

### Read
```json
route53resolver:GetOutpostResolver,
route53resolver:ListTagsForResource
```

### Update
```json
route53resolver:UpdateOutpostResolver,
route53resolver:GetOutpostResolver,
route53resolver:UntagResource,
route53resolver:TagResource,
route53resolver:ListTagsForResource
```

### Delete
```json
route53resolver:DeleteOutpostResolver,
route53resolver:GetOutpostResolver,
route53resolver:ListOutpostResolvers,
route53resolver:ListResolverEndpoints
```

