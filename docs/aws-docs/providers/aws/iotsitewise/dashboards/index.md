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


Used to retrieve a list of <code>dashboards</code> in a region or to create or delete a <code>dashboards</code> resource, use <code>dashboard</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTSiteWise::Dashboard</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotsitewise.dashboards" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="dashboard_id" /></td><td><code>string</code></td><td>The ID of the dashboard.</td></tr>
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
dashboard_id
FROM aws.iotsitewise.dashboards
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "DashboardName": "{{ DashboardName }}",
 "DashboardDescription": "{{ DashboardDescription }}",
 "DashboardDefinition": "{{ DashboardDefinition }}"
}
>>>
--required properties only
INSERT INTO aws.iotsitewise.dashboards (
 DashboardName,
 DashboardDescription,
 DashboardDefinition,
 region
)
SELECT 
{{ DashboardName }},
 {{ DashboardDescription }},
 {{ DashboardDefinition }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ProjectId": "{{ ProjectId }}",
 "DashboardName": "{{ DashboardName }}",
 "DashboardDescription": "{{ DashboardDescription }}",
 "DashboardDefinition": "{{ DashboardDefinition }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.iotsitewise.dashboards (
 ProjectId,
 DashboardName,
 DashboardDescription,
 DashboardDefinition,
 Tags,
 region
)
SELECT 
 {{ ProjectId }},
 {{ DashboardName }},
 {{ DashboardDescription }},
 {{ DashboardDefinition }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
iotsitewise:DescribeDashboard,
iotsitewise:DeleteDashboard
```

### List
```json
iotsitewise:ListDashboards
```

