---
title: restore_testing_selections
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_testing_selections
  - backup
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


Used to retrieve a list of <code>restore_testing_selections</code> in a region or to create or delete a <code>restore_testing_selections</code> resource, use <code>restore_testing_selection</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restore_testing_selections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Backup::RestoreTestingSelection</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.backup.restore_testing_selections" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="restore_testing_plan_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="restore_testing_selection_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="IamRoleArn, ProtectedResourceType, RestoreTestingPlanName, RestoreTestingSelectionName, region" /></td>
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
restore_testing_plan_name,
restore_testing_selection_name
FROM aws.backup.restore_testing_selections
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>restore_testing_selection</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.backup.restore_testing_selections (
 IamRoleArn,
 ProtectedResourceType,
 RestoreTestingPlanName,
 RestoreTestingSelectionName,
 region
)
SELECT 
'{{ IamRoleArn }}',
 '{{ ProtectedResourceType }}',
 '{{ RestoreTestingPlanName }}',
 '{{ RestoreTestingSelectionName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.backup.restore_testing_selections (
 IamRoleArn,
 ProtectedResourceArns,
 ProtectedResourceConditions,
 ProtectedResourceType,
 RestoreMetadataOverrides,
 RestoreTestingPlanName,
 RestoreTestingSelectionName,
 ValidationWindowHours,
 region
)
SELECT 
 '{{ IamRoleArn }}',
 '{{ ProtectedResourceArns }}',
 '{{ ProtectedResourceConditions }}',
 '{{ ProtectedResourceType }}',
 '{{ RestoreMetadataOverrides }}',
 '{{ RestoreTestingPlanName }}',
 '{{ RestoreTestingSelectionName }}',
 '{{ ValidationWindowHours }}',
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
  - name: restore_testing_selection
    props:
      - name: IamRoleArn
        value: '{{ IamRoleArn }}'
      - name: ProtectedResourceArns
        value:
          - '{{ ProtectedResourceArns[0] }}'
      - name: ProtectedResourceConditions
        value:
          StringEquals:
            - Key: '{{ Key }}'
              Value: '{{ Value }}'
          StringNotEquals:
            - null
      - name: ProtectedResourceType
        value: '{{ ProtectedResourceType }}'
      - name: RestoreMetadataOverrides
        value: {}
      - name: RestoreTestingPlanName
        value: '{{ RestoreTestingPlanName }}'
      - name: RestoreTestingSelectionName
        value: '{{ RestoreTestingSelectionName }}'
      - name: ValidationWindowHours
        value: '{{ ValidationWindowHours }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.backup.restore_testing_selections
WHERE data__Identifier = '<RestoreTestingPlanName|RestoreTestingSelectionName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>restore_testing_selections</code> resource, the following permissions are required:

### Create
```json
backup:CreateRestoreTestingSelection,
backup:GetRestoreTestingSelection,
iam:PassRole
```

### Delete
```json
backup:DeleteRestoreTestingSelection,
backup:GetRestoreTestingSelection
```

### List
```json
backup:ListRestoreTestingSelections
```

