---
title: studio
hide_title: false
hide_table_of_contents: false
keywords:
  - studio
  - emr
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

Gets or operates on an individual <code>studio</code> resource, use <code>studios</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studio</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EMR::Studio</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.emr.studio" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the EMR Studio.</td></tr>
<tr><td><CopyableCode code="auth_mode" /></td><td><code>string</code></td><td>Specifies whether the Studio authenticates users using single sign-on (SSO) or IAM. Amazon EMR Studio currently only supports SSO authentication.</td></tr>
<tr><td><CopyableCode code="default_s3_location" /></td><td><code>string</code></td><td>The default Amazon S3 location to back up EMR Studio Workspaces and notebook files. A Studio user can select an alternative Amazon S3 location when creating a Workspace.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A detailed description of the Studio.</td></tr>
<tr><td><CopyableCode code="engine_security_group_id" /></td><td><code>string</code></td><td>The ID of the Amazon EMR Studio Engine security group. The Engine security group allows inbound network traffic from the Workspace security group, and it must be in the same VPC specified by VpcId.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A descriptive name for the Amazon EMR Studio.</td></tr>
<tr><td><CopyableCode code="service_role" /></td><td><code>string</code></td><td>The IAM role that will be assumed by the Amazon EMR Studio. The service role provides a way for Amazon EMR Studio to interoperate with other AWS services.</td></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td>The ID of the EMR Studio.</td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td>A list of up to 5 subnet IDs to associate with the Studio. The subnets must belong to the VPC specified by VpcId. Studio users can create a Workspace in any of the specified subnets.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of tags to associate with the Studio. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters, and an optional value string with a maximum of 256 characters.</td></tr>
<tr><td><CopyableCode code="url" /></td><td><code>string</code></td><td>The unique Studio access URL.</td></tr>
<tr><td><CopyableCode code="user_role" /></td><td><code>string</code></td><td>The IAM user role that will be assumed by users and groups logged in to a Studio. The permissions attached to this IAM role can be scoped down for each user or group using session policies.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the Amazon Virtual Private Cloud (Amazon VPC) to associate with the Studio.</td></tr>
<tr><td><CopyableCode code="workspace_security_group_id" /></td><td><code>string</code></td><td>The ID of the Amazon EMR Studio Workspace security group. The Workspace security group allows outbound network traffic to resources in the Engine security group, and it must be in the same VPC specified by VpcId.</td></tr>
<tr><td><CopyableCode code="idp_auth_url" /></td><td><code>string</code></td><td>Your identity provider's authentication endpoint. Amazon EMR Studio redirects federated users to this endpoint for authentication when logging in to a Studio with the Studio URL.</td></tr>
<tr><td><CopyableCode code="idp_relay_state_parameter_name" /></td><td><code>string</code></td><td>The name of relay state parameter for external Identity Provider.</td></tr>
<tr><td><CopyableCode code="trusted_identity_propagation_enabled" /></td><td><code>boolean</code></td><td>A Boolean indicating whether to enable Trusted identity propagation for the Studio. The default value is false.</td></tr>
<tr><td><CopyableCode code="idc_user_assignment" /></td><td><code>string</code></td><td>Specifies whether IAM Identity Center user assignment is REQUIRED or OPTIONAL. If the value is set to REQUIRED, users must be explicitly assigned to the Studio application to access the Studio.</td></tr>
<tr><td><CopyableCode code="idc_instance_arn" /></td><td><code>string</code></td><td>The ARN of the IAM Identity Center instance to create the Studio application.</td></tr>
<tr><td><CopyableCode code="encryption_key_arn" /></td><td><code>string</code></td><td>The AWS KMS key identifier (ARN) used to encrypt AWS EMR Studio workspace and notebook files when backed up to AWS S3.</td></tr>
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
arn,
auth_mode,
default_s3_location,
description,
engine_security_group_id,
name,
service_role,
studio_id,
subnet_ids,
tags,
url,
user_role,
vpc_id,
workspace_security_group_id,
idp_auth_url,
idp_relay_state_parameter_name,
trusted_identity_propagation_enabled,
idc_user_assignment,
idc_instance_arn,
encryption_key_arn
FROM aws.emr.studio
WHERE data__Identifier = '<StudioId>';
```

## Permissions

To operate on the <code>studio</code> resource, the following permissions are required:

### Read
```json
elasticmapreduce:DescribeStudio,
sso:GetManagedApplicationInstance
```

### Update
```json
elasticmapreduce:UpdateStudio,
elasticmapreduce:DescribeStudio,
elasticmapreduce:AddTags,
elasticmapreduce:RemoveTags
```

### Delete
```json
elasticmapreduce:DeleteStudio,
elasticmapreduce:DescribeStudio,
sso:DeleteManagedApplicationInstance
```

