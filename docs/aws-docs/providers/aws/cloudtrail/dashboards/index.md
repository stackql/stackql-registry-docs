---
title: dashboards
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboards
  - cloudtrail
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

Creates, updates, deletes or gets a <code>dashboard</code> resource or lists <code>dashboards</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The Amazon CloudTrail dashboard resource allows customers to manage managed dashboards and create custom dashboards. You can manually refresh custom and managed dashboards. For custom dashboards, you can also set up an automatic refresh schedule and modify dashboard widgets.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudtrail.dashboards" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="widgets" /></td><td><code>array</code></td><td>List of widgets on the dashboard</td></tr>
<tr><td><CopyableCode code="created_timestamp" /></td><td><code>string</code></td><td>The timestamp of the dashboard creation.</td></tr>
<tr><td><CopyableCode code="dashboard_arn" /></td><td><code>string</code></td><td>The ARN of the dashboard.</td></tr>
<tr><td><CopyableCode code="refresh_schedule" /></td><td><code>object</code></td><td>Configures the automatic refresh schedule for the dashboard. Includes the frequency unit (DAYS or HOURS) and value, as well as the status (ENABLED or DISABLED) of the refresh schedule.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the dashboard.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the dashboard. Values are CREATING, CREATED, UPDATING, UPDATED and DELETING.</td></tr>
<tr><td><CopyableCode code="termination_protection_enabled" /></td><td><code>boolean</code></td><td>Indicates whether the dashboard is protected from termination.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the dashboard. Values are CUSTOM and MANAGED.</td></tr>
<tr><td><CopyableCode code="updated_timestamp" /></td><td><code>string</code></td><td>The timestamp showing when the dashboard was updated, if applicable. UpdatedTimestamp is always either the same or newer than the time shown in CreatedTimestamp.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-dashboard.html"><code>AWS::CloudTrail::Dashboard</code></a>.

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
    <td><CopyableCode code=", region" /></td>
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
Gets all <code>dashboards</code> in a region.
```sql
SELECT
region,
widgets,
created_timestamp,
dashboard_arn,
refresh_schedule,
name,
status,
termination_protection_enabled,
type,
updated_timestamp,
tags
FROM aws.cloudtrail.dashboards
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>dashboard</code>.
```sql
SELECT
region,
widgets,
created_timestamp,
dashboard_arn,
refresh_schedule,
name,
status,
termination_protection_enabled,
type,
updated_timestamp,
tags
FROM aws.cloudtrail.dashboards
WHERE region = 'us-east-1' AND data__Identifier = '<DashboardArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dashboard</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cloudtrail.dashboards (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudtrail.dashboards (
 Widgets,
 RefreshSchedule,
 Name,
 TerminationProtectionEnabled,
 Tags,
 region
)
SELECT 
 '{{ Widgets }}',
 '{{ RefreshSchedule }}',
 '{{ Name }}',
 '{{ TerminationProtectionEnabled }}',
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
  - name: dashboard
    props:
      - name: Widgets
        value:
          - QueryStatement: '{{ QueryStatement }}'
            QueryParameters:
              - '{{ QueryParameters[0] }}'
            ViewProperties: {}
      - name: RefreshSchedule
        value:
          Frequency:
            Unit: '{{ Unit }}'
            Value: '{{ Value }}'
          TimeOfDay: '{{ TimeOfDay }}'
          Status: '{{ Status }}'
      - name: Name
        value: '{{ Name }}'
      - name: TerminationProtectionEnabled
        value: '{{ TerminationProtectionEnabled }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cloudtrail.dashboards
WHERE data__Identifier = '<DashboardArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>dashboards</code> resource, the following permissions are required:

### Create
```json
CloudTrail:CreateDashboard,
CloudTrail:AddTags,
CloudTrail:StartQuery,
CloudTrail:StartDashboardRefresh
```

### Read
```json
CloudTrail:GetDashboard,
CloudTrail:ListDashboards,
CloudTrail:ListTags
```

### Update
```json
CloudTrail:UpdateDashboard,
CloudTrail:AddTags,
CloudTrail:RemoveTags,
CloudTrail:StartQuery,
CloudTrail:StartDashboardRefresh
```

### Delete
```json
CloudTrail:DeleteDashboard,
CloudTrail:UpdateDashboard
```

### List
```json
CloudTrail:ListDashboards,
CloudTrail:GetDashboard,
CloudTrail:ListTags
```
