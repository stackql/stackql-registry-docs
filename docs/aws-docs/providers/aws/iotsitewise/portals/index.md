---
title: portals
hide_title: false
hide_table_of_contents: false
keywords:
  - portals
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

Creates, updates, deletes or gets a <code>portal</code> resource or lists <code>portals</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>portals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTSiteWise::Portal</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotsitewise.portals" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="portal_auth_mode" /></td><td><code>string</code></td><td>The service to use to authenticate users to the portal. Choose from SSO or IAM. You can't change this value after you create a portal.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="PortalContactEmail, PortalName, RoleArn, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>portals</code> in a region.
```sql
SELECT
region,
portal_id
FROM aws.iotsitewise.portals
WHERE region = 'us-east-1';
```
Gets all properties from a <code>portal</code>.
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
FROM aws.iotsitewise.portals
WHERE region = 'us-east-1' AND data__Identifier = '<PortalId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>portal</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.iotsitewise.portals (
 PortalContactEmail,
 PortalName,
 RoleArn,
 region
)
SELECT 
'{{ PortalContactEmail }}',
 '{{ PortalName }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotsitewise.portals (
 PortalAuthMode,
 PortalContactEmail,
 PortalDescription,
 PortalName,
 RoleArn,
 NotificationSenderEmail,
 Alarms,
 Tags,
 region
)
SELECT 
 '{{ PortalAuthMode }}',
 '{{ PortalContactEmail }}',
 '{{ PortalDescription }}',
 '{{ PortalName }}',
 '{{ RoleArn }}',
 '{{ NotificationSenderEmail }}',
 '{{ Alarms }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: portal
    props:
      - name: PortalAuthMode
        value: '{{ PortalAuthMode }}'
      - name: PortalContactEmail
        value: '{{ PortalContactEmail }}'
      - name: PortalDescription
        value: '{{ PortalDescription }}'
      - name: PortalName
        value: '{{ PortalName }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: NotificationSenderEmail
        value: '{{ NotificationSenderEmail }}'
      - name: Alarms
        value:
          AlarmRoleArn: '{{ AlarmRoleArn }}'
          NotificationLambdaArn: '{{ NotificationLambdaArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iotsitewise.portals
WHERE data__Identifier = '<PortalId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>portals</code> resource, the following permissions are required:

### Create
```json
iotsitewise:CreatePortal,
iotsitewise:DescribePortal,
iotsitewise:ListTagsForResource,
iotsitewise:TagResource,
iam:PassRole,
sso:CreateManagedApplicationInstance,
sso:DescribeRegisteredRegions
```

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

### Delete
```json
iotsitewise:DescribePortal,
iotsitewise:DeletePortal,
sso:DeleteManagedApplicationInstance
```

### List
```json
iotsitewise:ListPortals
```

