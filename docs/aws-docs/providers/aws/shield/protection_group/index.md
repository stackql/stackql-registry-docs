---
title: protection_group
hide_title: false
hide_table_of_contents: false
keywords:
  - protection_group
  - shield
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>protection_group</code> resource, use <code>protection_groups</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>protection_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A grouping of protected resources so they can be handled as a collective. This resource grouping improves the accuracy of detection and reduces false positives.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.shield.protection_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>protection_group_id</code></td><td><code>string</code></td><td>The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it.</td></tr>
<tr><td><code>protection_group_arn</code></td><td><code>string</code></td><td>The ARN (Amazon Resource Name) of the protection group.</td></tr>
<tr><td><code>aggregation</code></td><td><code>string</code></td><td>Defines how AWS Shield combines resource data for the group in order to detect, mitigate, and report events.&lt;br&#x2F;&gt;* Sum - Use the total traffic across the group. This is a good choice for most cases. Examples include Elastic IP addresses for EC2 instances that scale manually or automatically.&lt;br&#x2F;&gt;* Mean - Use the average of the traffic across the group. This is a good choice for resources that share traffic uniformly. Examples include accelerators and load balancers.&lt;br&#x2F;&gt;* Max - Use the highest traffic from each resource. This is useful for resources that don't share traffic and for resources that share that traffic in a non-uniform way. Examples include Amazon CloudFront and origin resources for CloudFront distributions.</td></tr>
<tr><td><code>pattern</code></td><td><code>string</code></td><td>The criteria to use to choose the protected resources for inclusion in the group. You can include all resources that have protections, provide a list of resource Amazon Resource Names (ARNs), or include all resources of a specified resource type.</td></tr>
<tr><td><code>members</code></td><td><code>array</code></td><td>The Amazon Resource Names (ARNs) of the resources to include in the protection group. You must set this when you set `Pattern` to `ARBITRARY` and you must not set it for any other `Pattern` setting.</td></tr>
<tr><td><code>resource_type</code></td><td><code>string</code></td><td>The resource type to include in the protection group. All protected resources of this type are included in the protection group. Newly protected resources of this type are automatically added to the group. You must set this when you set `Pattern` to `BY_RESOURCE_TYPE` and you must not set it for any other `Pattern` setting.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>One or more tag key-value pairs for the Protection object.</td></tr>
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
protection_group_id,
protection_group_arn,
aggregation,
pattern,
members,
resource_type,
tags
FROM aws.shield.protection_group
WHERE data__Identifier = '<ProtectionGroupArn>';
```

## Permissions

To operate on the <code>protection_group</code> resource, the following permissions are required:

### Delete
```json
shield:DeleteProtectionGroup,
shield:UntagResource
```

### Read
```json
shield:DescribeProtectionGroup,
shield:ListTagsForResource
```

### Update
```json
shield:UpdateProtectionGroup,
shield:ListTagsForResource,
shield:TagResource,
shield:UntagResource
```

