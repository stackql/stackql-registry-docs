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


Used to retrieve a list of <code>app_monitors</code> in a region or to create or delete a <code>app_monitors</code> resource, use <code>app_monitor</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::RUM::AppMonitor</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rum.app_monitors" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the app monitor</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
name
FROM aws.rum.app_monitors
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- app_monitor.iql (required properties only)
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
-- app_monitor.iql (all properties)
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

## `DELETE` Example

```sql
DELETE FROM aws.rum.app_monitors
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>app_monitors</code> resource, the following permissions are required:

### Create
```json
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
cognito-identity:DescribeIdentityPool,
iam:GetRole,
iam:CreateServiceLinkedRole,
rum:PutRumMetricsDestination,
rum:BatchCreateRumMetricDefinitions
```

### Delete
```json
rum:DeleteAppMonitor,
dynamodb:DeleteItem,
dynamodb:Query,
logs:DeleteLogDelivery,
s3:DeleteObject,
s3:DoesObjectExist,
rum:UntagResource,
rum:DeleteRumMetricsDestination,
rum:BatchDeleteRumMetricDefinitions
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

