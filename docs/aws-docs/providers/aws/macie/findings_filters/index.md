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


Used to retrieve a list of <code>findings_filters</code> in a region or to create or delete a <code>findings_filters</code> resource, use <code>findings_filter</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>findings_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Macie FindingsFilter resource schema.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.macie.findings_filters" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Findings filter ID.</td></tr>
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
id
FROM aws.macie.findings_filters
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- findings_filter.iql (required properties only)
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
-- findings_filter.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
macie2:DeleteFindingsFilter
```

### List
```json
macie2:ListFindingsFilters
```

