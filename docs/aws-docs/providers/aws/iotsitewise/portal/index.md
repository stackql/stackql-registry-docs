---
title: portal
hide_title: false
hide_table_of_contents: false
keywords:
  - portal
  - iotsitewise
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


Gets or updates an individual <code>portal</code> resource, use <code>portals</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>portal</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTSiteWise::Portal</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotsitewise.portal" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="portal_auth_mode" /></td><td><code>string</code></td><td>The service to use to authenticate users to the portal. Choose from SSO or IAM. You can't change this value after you create a portal.</td></tr>
<tr><td><CopyableCode code="portal_arn" /></td><td><code>string</code></td><td>The ARN of the portal, which has the following format.</td></tr>
<tr><td><CopyableCode code="portal_client_id" /></td><td><code>string</code></td><td>The AWS SSO application generated client ID (used with AWS SSO APIs).</td></tr>
<tr><td><CopyableCode code="portal_contact_email" /></td><td><code>string</code></td><td>The AWS administrator's contact email address.</td></tr>
<tr><td><CopyableCode code="portal_description" /></td><td><code>string</code></td><td>A description for the portal.</td></tr>
<tr><td><CopyableCode code="portal_id" /></td><td><code>string</code></td><td>The ID of the portal.</td></tr>
<tr><td><CopyableCode code="portal_name" /></td><td><code>string</code></td><td>A friendly name for the portal.</td></tr>
<tr><td><CopyableCode code="portal_start_url" /></td><td><code>string</code></td><td>The public root URL for the AWS IoT AWS IoT SiteWise Monitor application portal.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of a service role that allows the portal's users to access your AWS IoT SiteWise resources on your behalf.</td></tr>
<tr><td><CopyableCode code="notification_sender_email" /></td><td><code>string</code></td><td>The email address that sends alarm notifications.</td></tr>
<tr><td><CopyableCode code="alarms" /></td><td><code>object</code></td><td>Contains the configuration information of an alarm created in an AWS IoT SiteWise Monitor portal. You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the portal.</td></tr>
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
portal_auth_mode,
portal_arn,
portal_client_id,
portal_contact_email,
portal_description,
portal_id,
portal_name,
portal_start_url,
role_arn,
notification_sender_email,
alarms,
tags
FROM aws.iotsitewise.portal
WHERE region = 'us-east-1' AND data__Identifier = '<PortalId>';
```


## Permissions

To operate on the <code>portal</code> resource, the following permissions are required:

### Read
```json
iotsitewise:DescribePortal,
iotsitewise:ListTagsForResource
```

### Update
```json
iotsitewise:DescribePortal,
iotsitewise:ListTagsForResource,
iotsitewise:TagResource,
iotsitewise:UpdatePortal,
iotsitewise:UntagResource,
iam:PassRole,
sso:GetManagedApplicationInstance,
sso:UpdateApplicationInstanceDisplayData
```

