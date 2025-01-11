---
title: app_monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - app_monitors
  - rum
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

Creates, updates, deletes or gets an <code>app_monitor</code> resource or lists <code>app_monitors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::RUM::AppMonitor</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rum.app_monitors" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique ID of the new app monitor.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the app monitor</td></tr>
<tr><td><CopyableCode code="domain" /></td><td><code>string</code></td><td>The top-level internet domain name for which your application has administrative authority.</td></tr>
<tr><td><CopyableCode code="cw_log_enabled" /></td><td><code>boolean</code></td><td>Data collected by RUM is kept by RUM for 30 days and then deleted. This parameter specifies whether RUM sends a copy of this telemetry data to CWLlong in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur CWLlong charges. If you omit this parameter, the default is false</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Assigns one or more tags (key-value pairs) to the app monitor. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.You can associate as many as 50 tags with an app monitor.</td></tr>
<tr><td><CopyableCode code="app_monitor_configuration" /></td><td><code>object</code></td><td>AppMonitor configuration</td></tr>
<tr><td><CopyableCode code="custom_events" /></td><td><code>object</code></td><td>AppMonitor custom events configuration</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rum-appmonitor.html"><code>AWS::RUM::AppMonitor</code></a>.

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
    <td><CopyableCode code="Name, Domain, region" /></td>
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
Gets all <code>app_monitors</code> in a region.
```sql
SELECT
region,
id,
name,
domain,
cw_log_enabled,
tags,
app_monitor_configuration,
custom_events
FROM aws.rum.app_monitors
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>app_monitor</code>.
```sql
SELECT
region,
id,
name,
domain,
cw_log_enabled,
tags,
app_monitor_configuration,
custom_events
FROM aws.rum.app_monitors
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>app_monitor</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.rum.app_monitors (
 Name,
 Domain,
 region
)
SELECT 
'{{ Name }}',
 '{{ Domain }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.rum.app_monitors (
 Name,
 Domain,
 CwLogEnabled,
 Tags,
 AppMonitorConfiguration,
 CustomEvents,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Domain }}',
 '{{ CwLogEnabled }}',
 '{{ Tags }}',
 '{{ AppMonitorConfiguration }}',
 '{{ CustomEvents }}',
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
  - name: app_monitor
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Domain
        value: '{{ Domain }}'
      - name: CwLogEnabled
        value: '{{ CwLogEnabled }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: AppMonitorConfiguration
        value:
          IdentityPoolId: '{{ IdentityPoolId }}'
          ExcludedPages:
            - '{{ ExcludedPages[0] }}'
          IncludedPages: null
          FavoritePages:
            - '{{ FavoritePages[0] }}'
          SessionSampleRate: null
          GuestRoleArn: '{{ GuestRoleArn }}'
          AllowCookies: '{{ AllowCookies }}'
          Telemetries:
            - '{{ Telemetries[0] }}'
          EnableXRay: '{{ EnableXRay }}'
          MetricDestinations:
            - Destination: '{{ Destination }}'
              DestinationArn: '{{ DestinationArn }}'
              IamRoleArn: '{{ IamRoleArn }}'
              MetricDefinitions:
                - Name: '{{ Name }}'
                  Namespace: '{{ Namespace }}'
                  ValueKey: '{{ ValueKey }}'
                  UnitLabel: '{{ UnitLabel }}'
                  DimensionKeys: {}
                  EventPattern: '{{ EventPattern }}'
      - name: CustomEvents
        value:
          Status: '{{ Status }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.rum.app_monitors
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>app_monitors</code> resource, the following permissions are required:

### Create
```json
rum:GetAppMonitor,
rum:CreateAppMonitor,
dynamodb:GetItem,
dynamodb:PutItem,
s3:GetObject,
s3:PutObject,
s3:GetObjectAcl,
s3:DoesObjectExist,
logs:CreateLogDelivery,
logs:CreateLogGroup,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
logs:PutRetentionPolicy,
rum:TagResource,
rum:ListTagsForResource,
cognito-identity:DescribeIdentityPool,
iam:GetRole,
iam:CreateServiceLinkedRole,
iam:PassRole,
rum:PutRumMetricsDestination,
rum:BatchCreateRumMetricDefinitions,
rum:ListRumMetricsDestinations,
rum:BatchGetRumMetricDefinitions
```

### Read
```json
rum:GetAppMonitor,
dynamodb:GetItem,
s3:GetObject,
s3:DoesObjectExist,
s3:GetObjectAcl,
rum:ListTagsForResource,
rum:ListRumMetricsDestinations,
rum:BatchGetRumMetricDefinitions
```

### Update
```json
rum:GetAppMonitor,
rum:UpdateAppMonitor,
dynamodb:GetItem,
dynamodb:PutItem,
dynamodb:UpdateItem,
dynamodb:Query,
s3:GetObject,
s3:PutObject,
s3:GetObjectAcl,
s3:DoesObjectExist,
logs:CreateLogDelivery,
logs:CreateLogGroup,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
logs:PutRetentionPolicy,
rum:TagResource,
rum:UntagResource,
rum:ListTagsForResource,
iam:GetRole,
iam:CreateServiceLinkedRole,
iam:PassRole,
rum:PutRumMetricsDestination,
rum:DeleteRumMetricsDestination,
rum:ListRumMetricsDestinations,
rum:BatchCreateRumMetricDefinitions,
rum:BatchDeleteRumMetricDefinitions,
rum:BatchGetRumMetricDefinitions,
rum:UpdateRumMetricDefinition
```

### Delete
```json
rum:GetAppMonitor,
rum:DeleteAppMonitor,
dynamodb:DeleteItem,
dynamodb:Query,
logs:DeleteLogDelivery,
s3:DeleteObject,
s3:DoesObjectExist,
rum:UntagResource,
rum:ListTagsForResource,
rum:DeleteRumMetricsDestination,
rum:BatchDeleteRumMetricDefinitions,
rum:ListRumMetricsDestinations,
rum:BatchGetRumMetricDefinitions
```

### List
```json
rum:ListAppMonitors,
dynamodb:DescribeTable,
rum:GetAppMonitor,
dynamodb:GetItem,
dynamodb:BatchGetItem,
dynamodb:Query,
s3:GetObject,
s3:DoesObjectExist,
s3:GetObjectAcl,
logs:DescribeLogGroups,
rum:ListTagsForResource
```
