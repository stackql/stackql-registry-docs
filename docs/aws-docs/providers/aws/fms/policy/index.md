---
title: policy
hide_title: false
hide_table_of_contents: false
keywords:
  - policy
  - fms
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>policy</code> resource, use <code>policies</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an AWS Firewall Manager policy.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.fms.policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>exclude_map</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>exclude_resource_tags</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>include_map</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>remediation_enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>resource_tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>resource_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_type_list</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>resource_set_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>security_service_policy_data</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>delete_all_policy_resources</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>resources_clean_up</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
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
exclude_map,
exclude_resource_tags,
include_map,
id,
policy_name,
policy_description,
remediation_enabled,
resource_tags,
resource_type,
resource_type_list,
resource_set_ids,
security_service_policy_data,
arn,
delete_all_policy_resources,
resources_clean_up,
tags
FROM aws.fms.policy
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>policy</code> resource, the following permissions are required:

### Update
```json
fms:PutPolicy,
fms:GetPolicy,
fms:TagResource,
fms:UntagResource,
fms:ListTagsForResource,
waf-regional:ListRuleGroups,
wafv2:CheckCapacity,
wafv2:ListRuleGroups,
wafv2:ListAvailableManagedRuleGroups,
wafv2:ListAvailableManagedRuleGroupVersions,
network-firewall:DescribeRuleGroup,
network-firewall:DescribeRuleGroupMetadata,
route53resolver:ListFirewallRuleGroups,
ec2:DescribeAvailabilityZones,
s3:PutBucketPolicy,
s3:GetBucketPolicy
```

### Read
```json
fms:GetPolicy,
fms:ListTagsForResource
```

### Delete
```json
fms:DeletePolicy
```

