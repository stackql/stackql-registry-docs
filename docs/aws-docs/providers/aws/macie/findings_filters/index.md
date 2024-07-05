---
title: findings_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - findings_filters
  - macie
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

Creates, updates, deletes or gets a <code>findings_filter</code> resource or lists <code>findings_filters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>findings_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Macie FindingsFilter resource schema.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.macie.findings_filters" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Findings filter name</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Findings filter description</td></tr>
<tr><td><CopyableCode code="finding_criteria" /></td><td><code>object</code></td><td>Findings filter criteria.</td></tr>
<tr><td><CopyableCode code="action" /></td><td><code>string</code></td><td>Findings filter action.</td></tr>
<tr><td><CopyableCode code="position" /></td><td><code>integer</code></td><td>Findings filter position.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Findings filter ID.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Findings filter ARN.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
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
    <td><CopyableCode code="Name, FindingCriteria, region" /></td>
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
Gets all <code>findings_filters</code> in a region.
```sql
SELECT
region,
name,
description,
finding_criteria,
action,
position,
id,
arn,
tags
FROM aws.macie.findings_filters
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>findings_filter</code>.
```sql
SELECT
region,
name,
description,
finding_criteria,
action,
position,
id,
arn,
tags
FROM aws.macie.findings_filters
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>findings_filter</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.macie.findings_filters (
 Name,
 FindingCriteria,
 region
)
SELECT 
'{{ Name }}',
 '{{ FindingCriteria }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.macie.findings_filters (
 Name,
 Description,
 FindingCriteria,
 Action,
 Position,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ FindingCriteria }}',
 '{{ Action }}',
 '{{ Position }}',
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
  - name: findings_filter
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: FindingCriteria
        value:
          Criterion: {}
      - name: Action
        value: '{{ Action }}'
      - name: Position
        value: '{{ Position }}'
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
DELETE FROM aws.macie.findings_filters
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>findings_filters</code> resource, the following permissions are required:

### Create
```json
macie2:GetFindingsFilter,
macie2:CreateFindingsFilter,
macie2:TagResource
```

### Read
```json
macie2:GetFindingsFilter
```

### Update
```json
macie2:GetFindingsFilter,
macie2:UpdateFindingsFilter,
macie2:TagResource,
macie2:UntagResource
```

### Delete
```json
macie2:DeleteFindingsFilter
```

### List
```json
macie2:ListFindingsFilters
```

