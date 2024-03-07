---
title: security_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - security_profile
  - connect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>security_profile</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>security_profile</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.security_profile</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>allowed_access_control_tags</code></td><td><code>array</code></td><td>The list of tags that a security profile uses to restrict access to resources in Amazon Connect.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the security profile.</td></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><code>permissions</code></td><td><code>array</code></td><td>Permissions assigned to the security profile.</td></tr>
<tr><td><code>security_profile_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the security profile.</td></tr>
<tr><td><code>security_profile_name</code></td><td><code>string</code></td><td>The name of the security profile.</td></tr>
<tr><td><code>tag_restricted_resources</code></td><td><code>array</code></td><td>The list of resources that a security profile applies tag restrictions to in Amazon Connect.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags used to organize, track, or control access for this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>security_profile</code> resource, the following permissions are required:

### Read
<pre>
connect:DescribeSecurityProfile,
connect:ListSecurityProfilePermissions</pre>

### Update
<pre>
connect:TagResource,
connect:UpdateSecurityProfile,
connect:UntagResource</pre>

### Delete
<pre>
connect:DeleteSecurityProfile,
connect:UntagResource</pre>


## Example
```sql
SELECT
region,
allowed_access_control_tags,
description,
instance_arn,
permissions,
security_profile_arn,
security_profile_name,
tag_restricted_resources,
tags
FROM awscc.connect.security_profile
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;SecurityProfileArn&gt;'
```
