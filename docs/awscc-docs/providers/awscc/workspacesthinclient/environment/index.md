---
title: environment
hide_title: false
hide_table_of_contents: false
keywords:
  - environment
  - workspacesthinclient
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>environment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>environment</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.workspacesthinclient.environment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Unique identifier of the environment.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the environment.</td></tr>
<tr><td><code>desktop_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the desktop to stream from Amazon WorkSpaces, WorkSpaces Web, or AppStream 2.0.</td></tr>
<tr><td><code>desktop_endpoint</code></td><td><code>string</code></td><td>The URL for the identity provider login (only for environments that use AppStream 2.0).</td></tr>
<tr><td><code>desktop_type</code></td><td><code>string</code></td><td>The type of VDI.</td></tr>
<tr><td><code>activation_code</code></td><td><code>string</code></td><td>Activation code for devices associated with environment.</td></tr>
<tr><td><code>registered_devices_count</code></td><td><code>integer</code></td><td>Number of devices registered to the environment.</td></tr>
<tr><td><code>software_set_update_schedule</code></td><td><code>string</code></td><td>An option to define if software updates should be applied within a maintenance window.</td></tr>
<tr><td><code>maintenance_window</code></td><td><code>object</code></td><td>A specification for a time window to apply software updates.</td></tr>
<tr><td><code>software_set_update_mode</code></td><td><code>string</code></td><td>An option to define which software updates to apply.</td></tr>
<tr><td><code>desired_software_set_id</code></td><td><code>string</code></td><td>The ID of the software set to apply.</td></tr>
<tr><td><code>pending_software_set_id</code></td><td><code>string</code></td><td>The ID of the software set that is pending to be installed.</td></tr>
<tr><td><code>pending_software_set_version</code></td><td><code>string</code></td><td>The version of the software set that is pending to be installed.</td></tr>
<tr><td><code>software_set_compliance_status</code></td><td><code>string</code></td><td>Describes if the software currently installed on all devices in the environment is a supported version.</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The timestamp in unix epoch format when environment was created.</td></tr>
<tr><td><code>updated_at</code></td><td><code>string</code></td><td>The timestamp in unix epoch format when environment was last updated.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The environment ARN.</td></tr>
<tr><td><code>kms_key_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the AWS Key Management Service key used to encrypt the environment.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>environment</code> resource, the following permissions are required:

### Read
<pre>
thinclient:GetEnvironment,
thinclient:ListTagsForResource,
kms:DescribeKey,
kms:Encrypt,
kms:Decrypt</pre>

### Update
<pre>
appstream:DescribeStacks,
workspaces:DescribeWorkspaceDirectories,
workspaces-web:GetPortal,
workspaces-web:GetUserSettings,
thinclient:UpdateEnvironment,
thinclient:GetEnvironment,
thinclient:TagResource,
thinclient:UntagResource,
thinclient:ListTagsForResource,
kms:DescribeKey,
kms:Encrypt,
kms:Decrypt,
kms:CreateGrant,
kms:RetireGrant</pre>

### Delete
<pre>
thinclient:DeleteEnvironment,
thinclient:UntagResource,
kms:DescribeKey,
kms:RetireGrant</pre>


## Example
```sql
SELECT
region,
id,
name,
desktop_arn,
desktop_endpoint,
desktop_type,
activation_code,
registered_devices_count,
software_set_update_schedule,
maintenance_window,
software_set_update_mode,
desired_software_set_id,
pending_software_set_id,
pending_software_set_version,
software_set_compliance_status,
created_at,
updated_at,
arn,
kms_key_arn,
tags
FROM awscc.workspacesthinclient.environment
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
