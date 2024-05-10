---
title: data_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources
  - datazone
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


Used to retrieve a list of <code>data_sources</code> in a region or to create or delete a <code>data_sources</code> resource, use <code>data_source</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::DataZone::DataSource Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.data_sources" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain where the data source is created.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique identifier of the data source.</td></tr>
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
domain_id,
id
FROM aws.datazone.data_sources
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>data_source</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- data_source.iql (required properties only)
INSERT INTO aws.datazone.data_sources (
 DomainIdentifier,
 EnvironmentIdentifier,
 Name,
 ProjectIdentifier,
 Type,
 region
)
SELECT 
'{{ DomainIdentifier }}',
 '{{ EnvironmentIdentifier }}',
 '{{ Name }}',
 '{{ ProjectIdentifier }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- data_source.iql (all properties)
INSERT INTO aws.datazone.data_sources (
 AssetFormsInput,
 Description,
 DomainIdentifier,
 EnableSetting,
 EnvironmentIdentifier,
 Configuration,
 Name,
 ProjectIdentifier,
 PublishOnImport,
 Recommendation,
 Schedule,
 Type,
 region
)
SELECT 
 '{{ AssetFormsInput }}',
 '{{ Description }}',
 '{{ DomainIdentifier }}',
 '{{ EnableSetting }}',
 '{{ EnvironmentIdentifier }}',
 '{{ Configuration }}',
 '{{ Name }}',
 '{{ ProjectIdentifier }}',
 '{{ PublishOnImport }}',
 '{{ Recommendation }}',
 '{{ Schedule }}',
 '{{ Type }}',
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
  - name: data_source
    props:
      - name: AssetFormsInput
        value:
          - FormName: '{{ FormName }}'
            TypeIdentifier: '{{ TypeIdentifier }}'
            TypeRevision: '{{ TypeRevision }}'
            Content: '{{ Content }}'
      - name: Description
        value: '{{ Description }}'
      - name: DomainIdentifier
        value: '{{ DomainIdentifier }}'
      - name: EnableSetting
        value: '{{ EnableSetting }}'
      - name: EnvironmentIdentifier
        value: '{{ EnvironmentIdentifier }}'
      - name: Configuration
        value: null
      - name: Name
        value: '{{ Name }}'
      - name: ProjectIdentifier
        value: '{{ ProjectIdentifier }}'
      - name: PublishOnImport
        value: '{{ PublishOnImport }}'
      - name: Recommendation
        value:
          EnableBusinessNameGeneration: '{{ EnableBusinessNameGeneration }}'
      - name: Schedule
        value:
          Timezone: '{{ Timezone }}'
          Schedule: '{{ Schedule }}'
      - name: Type
        value: '{{ Type }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.datazone.data_sources
WHERE data__Identifier = '<DomainId|Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>data_sources</code> resource, the following permissions are required:

### Create
```json
datazone:CreateDataSource,
iam:PassRole,
datazone:GetDataSource,
datazone:DeleteDataSource
```

### Delete
```json
datazone:DeleteDataSource,
datazone:GetDataSource
```

### List
```json
datazone:ListDataSources
```

