---
title: custom_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_permissions
  - quicksight
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

Creates, updates, deletes or gets a <code>custom_permission</code> resource or lists <code>custom_permissions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::CustomPermissions Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.custom_permissions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="capabilities" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_permissions_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-custompermission.html"><code>AWS::QuickSight::CustomPermissions</code></a>.

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
    <td><CopyableCode code="AwsAccountId, CustomPermissionsName, region" /></td>
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
Gets all <code>custom_permissions</code> in a region.
```sql
SELECT
region,
arn,
aws_account_id,
capabilities,
custom_permissions_name,
tags
FROM aws.quicksight.custom_permissions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>custom_permission</code>.
```sql
SELECT
region,
arn,
aws_account_id,
capabilities,
custom_permissions_name,
tags
FROM aws.quicksight.custom_permissions
WHERE region = 'us-east-1' AND data__Identifier = '<AwsAccountId>|<CustomPermissionsName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_permission</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.quicksight.custom_permissions (
 AwsAccountId,
 CustomPermissionsName,
 region
)
SELECT 
'{{ AwsAccountId }}',
 '{{ CustomPermissionsName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.quicksight.custom_permissions (
 AwsAccountId,
 Capabilities,
 CustomPermissionsName,
 Tags,
 region
)
SELECT 
 '{{ AwsAccountId }}',
 '{{ Capabilities }}',
 '{{ CustomPermissionsName }}',
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
  - name: custom_permission
    props:
      - name: AwsAccountId
        value: '{{ AwsAccountId }}'
      - name: Capabilities
        value:
          ExportToCsv: '{{ ExportToCsv }}'
          ExportToExcel: null
          CreateAndUpdateThemes: null
          AddOrRunAnomalyDetectionForAnalyses: null
          ShareAnalyses: null
          CreateAndUpdateDatasets: null
          ShareDatasets: null
          SubscribeDashboardEmailReports: null
          CreateAndUpdateDashboardEmailReports: null
          ShareDashboards: null
          CreateAndUpdateThresholdAlerts: null
          RenameSharedFolders: null
          CreateSharedFolders: null
          CreateAndUpdateDataSources: null
          ShareDataSources: null
          ViewAccountSPICECapacity: null
          CreateSPICEDataset: null
      - name: CustomPermissionsName
        value: '{{ CustomPermissionsName }}'
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
DELETE FROM aws.quicksight.custom_permissions
WHERE data__Identifier = '<AwsAccountId|CustomPermissionsName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>custom_permissions</code> resource, the following permissions are required:

### Create
```json
quicksight:CreateCustomPermissions,
quicksight:TagResource
```

### Read
```json
quicksight:DescribeCustomPermissions,
quicksight:ListTagsForResource
```

### Update
```json
quicksight:UpdateCustomPermissions,
quicksight:TagResource,
quicksight:UntagResource,
quicksight:ListTagsForResource
```

### Delete
```json
quicksight:DeleteCustomPermissions
```

### List
```json
quicksight:ListCustomPermissions
```
