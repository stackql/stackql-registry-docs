---
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - deadline
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

Creates, updates, deletes or gets a <code>monitor</code> resource or lists <code>monitors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Deadline::Monitor Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.deadline.monitors" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_center_application_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_center_instance_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="monitor_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subdomain" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-deadline-monitor.html"><code>AWS::Deadline::Monitor</code></a>.

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
    <td><CopyableCode code="DisplayName, IdentityCenterInstanceArn, RoleArn, Subdomain, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>monitors</code> in a region.
```sql
SELECT
region,
display_name,
identity_center_application_arn,
identity_center_instance_arn,
monitor_id,
role_arn,
subdomain,
url,
arn
FROM aws.deadline.monitors
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>monitor</code>.
```sql
SELECT
region,
display_name,
identity_center_application_arn,
identity_center_instance_arn,
monitor_id,
role_arn,
subdomain,
url,
arn
FROM aws.deadline.monitors
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>monitor</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.deadline.monitors (
 DisplayName,
 IdentityCenterInstanceArn,
 RoleArn,
 Subdomain,
 region
)
SELECT 
'{{ DisplayName }}',
 '{{ IdentityCenterInstanceArn }}',
 '{{ RoleArn }}',
 '{{ Subdomain }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.deadline.monitors (
 DisplayName,
 IdentityCenterInstanceArn,
 RoleArn,
 Subdomain,
 region
)
SELECT 
 '{{ DisplayName }}',
 '{{ IdentityCenterInstanceArn }}',
 '{{ RoleArn }}',
 '{{ Subdomain }}',
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
  - name: monitor
    props:
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: IdentityCenterInstanceArn
        value: '{{ IdentityCenterInstanceArn }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Subdomain
        value: '{{ Subdomain }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.deadline.monitors
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>monitors</code> resource, the following permissions are required:

### Create
```json
deadline:CreateMonitor,
deadline:GetMonitor,
iam:PassRole,
kms:CreateGrant,
sso:CreateApplication,
sso:DeleteApplication,
sso:PutApplicationAssignmentConfiguration,
sso:PutApplicationAuthenticationMethod,
sso:PutApplicationGrant
```

### Read
```json
deadline:GetMonitor
```

### Update
```json
deadline:GetMonitor,
deadline:UpdateMonitor,
iam:PassRole,
kms:CreateGrant,
sso:PutApplicationGrant,
sso:UpdateApplication
```

### Delete
```json
deadline:DeleteMonitor,
deadline:GetMonitor,
sso:DeleteApplication
```

### List
```json
deadline:ListMonitors
```
