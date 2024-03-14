---
title: user_access_logging_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - user_access_logging_settings
  - workspacesweb
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>user_access_logging_settings</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_access_logging_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>user_access_logging_settings</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.workspacesweb.user_access_logging_settings</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>associated_portal_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>kinesis_stream_arn</code></td><td><code>string</code></td><td>Kinesis stream ARN to which log events are published.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>user_access_logging_settings_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
associated_portal_arns,
kinesis_stream_arn,
tags,
user_access_logging_settings_arn
FROM awscc.workspacesweb.user_access_logging_settings
WHERE data__Identifier = '<UserAccessLoggingSettingsArn>';
```

## Permissions

To operate on the <code>user_access_logging_settings</code> resource, the following permissions are required:

### Read
```json
workspaces-web:GetUserAccessLoggingSettings,
workspaces-web:ListTagsForResource
```

### Update
```json
workspaces-web:UpdateUserAccessLoggingSettings,
workspaces-web:TagResource,
workspaces-web:UntagResource,
workspaces-web:GetUserAccessLoggingSettings,
workspaces-web:ListTagsForResource,
kinesis:PutRecord,
kinesis:PutRecords
```

### Delete
```json
workspaces-web:GetUserAccessLoggingSettings,
workspaces-web:DeleteUserAccessLoggingSettings
```

