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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>security_profile</code> resource, use <code>security_profiles</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::SecurityProfile</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.security_profile" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="allowed_access_control_tags" /></td><td><code>array</code></td><td>The list of tags that a security profile uses to restrict access to resources in Amazon Connect.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the security profile.</td></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="permissions" /></td><td><code>array</code></td><td>Permissions assigned to the security profile.</td></tr>
<tr><td><CopyableCode code="security_profile_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the security profile.</td></tr>
<tr><td><CopyableCode code="security_profile_name" /></td><td><code>string</code></td><td>The name of the security profile.</td></tr>
<tr><td><CopyableCode code="tag_restricted_resources" /></td><td><code>array</code></td><td>The list of resources that a security profile applies tag restrictions to in Amazon Connect.</td></tr>
<tr><td><CopyableCode code="hierarchy_restricted_resources" /></td><td><code>array</code></td><td>The list of resources that a security profile applies hierarchy restrictions to in Amazon Connect.</td></tr>
<tr><td><CopyableCode code="allowed_access_control_hierarchy_group_id" /></td><td><code>string</code></td><td>The identifier of the hierarchy group that a security profile uses to restrict access to resources in Amazon Connect.</td></tr>
<tr><td><CopyableCode code="applications" /></td><td><code>array</code></td><td>A list of third-party applications that the security profile will give access to.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags used to organize, track, or control access for this resource.</td></tr>
<tr><td><CopyableCode code="last_modified_region" /></td><td><code>string</code></td><td>The AWS Region where this resource was last modified.</td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>number</code></td><td>The timestamp when this resource was last modified.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
hierarchy_restricted_resources,
allowed_access_control_hierarchy_group_id,
applications,
tags,
last_modified_region,
last_modified_time
FROM aws.connect.security_profile
WHERE data__Identifier = '<SecurityProfileArn>';
```

## Permissions

To operate on the <code>security_profile</code> resource, the following permissions are required:

### Read
```json
connect:DescribeSecurityProfile,
connect:ListSecurityProfileApplications,
connect:ListSecurityProfilePermissions
```

### Update
```json
connect:TagResource,
connect:UpdateSecurityProfile,
connect:UntagResource
```

### Delete
```json
connect:DeleteSecurityProfile,
connect:UntagResource
```
