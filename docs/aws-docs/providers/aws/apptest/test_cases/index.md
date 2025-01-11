---
title: test_cases
hide_title: false
hide_table_of_contents: false
keywords:
  - test_cases
  - apptest
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

Creates, updates, deletes or gets a <code>test_case</code> resource or lists <code>test_cases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>test_cases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a Test Case that can be captured and executed</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apptest.test_cases" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_update_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="latest_version" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="steps" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="test_case_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="test_case_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="test_case_version" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apptest-testcase.html"><code>AWS::AppTest::TestCase</code></a>.

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
    <td><CopyableCode code="Name, Steps, region" /></td>
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
Gets all <code>test_cases</code> in a region.
```sql
SELECT
region,
creation_time,
description,
last_update_time,
latest_version,
name,
status,
steps,
tags,
test_case_arn,
test_case_id,
test_case_version
FROM aws.apptest.test_cases
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>test_case</code>.
```sql
SELECT
region,
creation_time,
description,
last_update_time,
latest_version,
name,
status,
steps,
tags,
test_case_arn,
test_case_id,
test_case_version
FROM aws.apptest.test_cases
WHERE region = 'us-east-1' AND data__Identifier = '<TestCaseId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>test_case</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apptest.test_cases (
 Name,
 Steps,
 region
)
SELECT 
'{{ Name }}',
 '{{ Steps }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apptest.test_cases (
 Description,
 Name,
 Steps,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Name }}',
 '{{ Steps }}',
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
  - name: test_case
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: Steps
        value:
          - Name: '{{ Name }}'
            Description: '{{ Description }}'
            Action: null
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apptest.test_cases
WHERE data__Identifier = '<TestCaseId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>test_cases</code> resource, the following permissions are required:

### Create
```json
apptest:CreateTestCase,
apptest:GetTestCase,
apptest:ListTagsForResource
```

### Read
```json
apptest:GetTestCase,
apptest:ListTagsForResource
```

### Update
```json
apptest:UpdateTestCase,
apptest:GetTestCase,
apptest:TagResource,
apptest:UnTagResource,
apptest:ListTagsForResource
```

### Delete
```json
apptest:GetTestCase,
apptest:ListTagsForResource,
apptest:DeleteTestCase
```

### List
```json
apptest:ListTestCases
```
