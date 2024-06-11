---
title: dashboards
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboards
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

Creates, updates, deletes or gets a <code>dashboard</code> resource or lists <code>dashboards</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTSiteWise::Dashboard</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotsitewise.dashboards" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="project_id" /></td><td><code>string</code></td><td>The ID of the project in which to create the dashboard.</td></tr>
<tr><td><CopyableCode code="dashboard_id" /></td><td><code>string</code></td><td>The ID of the dashboard.</td></tr>
<tr><td><CopyableCode code="dashboard_name" /></td><td><code>string</code></td><td>A friendly name for the dashboard.</td></tr>
<tr><td><CopyableCode code="dashboard_description" /></td><td><code>string</code></td><td>A description for the dashboard.</td></tr>
<tr><td><CopyableCode code="dashboard_definition" /></td><td><code>string</code></td><td>The dashboard definition specified in a JSON literal.</td></tr>
<tr><td><CopyableCode code="dashboard_arn" /></td><td><code>string</code></td><td>The ARN of the dashboard.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the dashboard.</td></tr>
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
    <td><CopyableCode code="DashboardDefinition, DashboardDescription, DashboardName, region" /></td>
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
List all <code>dashboards</code> in a region.
```sql
SELECT
region,
dashboard_id
FROM aws.iotsitewise.dashboards
WHERE region = 'us-east-1';
```
Gets all properties from a <code>dashboard</code>.
```sql
SELECT
region,
project_id,
dashboard_id,
dashboard_name,
dashboard_description,
dashboard_definition,
dashboard_arn,
tags
FROM aws.iotsitewise.dashboards
WHERE region = 'us-east-1' AND data__Identifier = '<DashboardId>';
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
INSERT INTO aws.iotsitewise.dashboards (
 DashboardName,
 DashboardDescription,
 DashboardDefinition,
 region
)
SELECT 
'{{ DashboardName }}',
 '{{ DashboardDescription }}',
 '{{ DashboardDefinition }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotsitewise.dashboards (
 ProjectId,
 DashboardName,
 DashboardDescription,
 DashboardDefinition,
 Tags,
 region
)
SELECT 
 '{{ ProjectId }}',
 '{{ DashboardName }}',
 '{{ DashboardDescription }}',
 '{{ DashboardDefinition }}',
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
      - name: ProjectId
        value: '{{ ProjectId }}'
      - name: DashboardName
        value: '{{ DashboardName }}'
      - name: DashboardDescription
        value: '{{ DashboardDescription }}'
      - name: DashboardDefinition
        value: '{{ DashboardDefinition }}'
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
DELETE FROM aws.iotsitewise.dashboards
WHERE data__Identifier = '<DashboardId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>dashboards</code> resource, the following permissions are required:

### Create
```json
iotsitewise:CreateDashboard,
iotsitewise:DescribeDashboard,
iotsitewise:ListTagsForResource,
iotsitewise:TagResource,
iotsitewise:DescribeAsset,
iotsitewise:DescribeAssetModel,
iotsitewise:ListAssetModelProperties,
iotsitewise:ListAssetModelCompositeModels
```

### Read
```json
iotsitewise:DescribeDashboard,
iotsitewise:ListTagsForResource
```

### Update
```json
iotsitewise:DescribeDashboard,
iotsitewise:UpdateDashboard,
iotsitewise:TagResource,
iotsitewise:UntagResource,
iotsitewise:ListTagsForResource,
iotsitewise:DescribeAsset,
iotsitewise:DescribeAssetModel,
iotsitewise:ListAssetModelProperties,
iotsitewise:ListAssetModelCompositeModels
```

### Delete
```json
iotsitewise:DescribeDashboard,
iotsitewise:DeleteDashboard
```

### List
```json
iotsitewise:ListDashboards
```

