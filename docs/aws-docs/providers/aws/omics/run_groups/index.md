---
title: run_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - run_groups
  - omics
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

Creates, updates, deletes or gets a <code>run_group</code> resource or lists <code>run_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>run_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Omics::RunGroup Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.omics.run_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="max_cpus" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="max_gpus" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="max_duration" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="max_runs" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A map of resource tags</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html"><code>AWS::Omics::RunGroup</code></a>.

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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>run_groups</code> in a region.
```sql
SELECT
region,
arn,
creation_time,
id,
max_cpus,
max_gpus,
max_duration,
max_runs,
name,
tags
FROM aws.omics.run_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>run_group</code>.
```sql
SELECT
region,
arn,
creation_time,
id,
max_cpus,
max_gpus,
max_duration,
max_runs,
name,
tags
FROM aws.omics.run_groups
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>run_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.omics.run_groups (
 MaxCpus,
 MaxGpus,
 MaxDuration,
 MaxRuns,
 Name,
 Tags,
 region
)
SELECT 
'{{ MaxCpus }}',
 '{{ MaxGpus }}',
 '{{ MaxDuration }}',
 '{{ MaxRuns }}',
 '{{ Name }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.omics.run_groups (
 MaxCpus,
 MaxGpus,
 MaxDuration,
 MaxRuns,
 Name,
 Tags,
 region
)
SELECT 
 '{{ MaxCpus }}',
 '{{ MaxGpus }}',
 '{{ MaxDuration }}',
 '{{ MaxRuns }}',
 '{{ Name }}',
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
  - name: run_group
    props:
      - name: MaxCpus
        value: null
      - name: MaxGpus
        value: null
      - name: MaxDuration
        value: null
      - name: MaxRuns
        value: null
      - name: Name
        value: '{{ Name }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.omics.run_groups
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>run_groups</code> resource, the following permissions are required:

### Create
```json
omics:CreateRunGroup,
omics:TagResource
```

### Read
```json
omics:GetRunGroup
```

### Update
```json
omics:UpdateRunGroup,
omics:TagResource,
omics:GetRunGroup,
omics:ListTagsForResource,
omics:UntagResource
```

### Delete
```json
omics:DeleteRunGroup,
omics:GetRunGroup
```

### List
```json
omics:ListRunGroups
```
