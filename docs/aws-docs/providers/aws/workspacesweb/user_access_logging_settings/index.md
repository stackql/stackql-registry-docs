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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>user_access_logging_settings</code> resource, use <code>user_access_logging_settings</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_access_logging_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::WorkSpacesWeb::UserAccessLoggingSettings Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspacesweb.user_access_logging_settings" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="associated_portal_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="kinesis_stream_arn" /></td><td><code>string</code></td><td>Kinesis stream ARN to which log events are published.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="user_access_logging_settings_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
associated_portal_arns,
kinesis_stream_arn,
tags,
user_access_logging_settings_arn
FROM aws.workspacesweb.user_access_logging_settings
WHERE region = 'us-east-1' AND data__Identifier = '<UserAccessLoggingSettingsArn>';
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

