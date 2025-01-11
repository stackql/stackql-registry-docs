---
title: sdi_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - sdi_sources
  - medialive
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

Creates, updates, deletes or gets a <code>sdi_source</code> resource or lists <code>sdi_sources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sdi_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaLive::SdiSource Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.medialive.sdi_sources" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The unique arn of the SdiSource.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique identifier of the SdiSource.</td></tr>
<tr><td><CopyableCode code="mode" /></td><td><code>string</code></td><td>The current state of the SdiSource.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the SdiSource.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The current state of the SdiSource.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The interface mode of the SdiSource.</td></tr>
<tr><td><CopyableCode code="inputs" /></td><td><code>array</code></td><td>The list of inputs currently using this SDI source.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of key-value pairs.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-sdisource.html"><code>AWS::MediaLive::SdiSource</code></a>.

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
    <td><CopyableCode code="Name, Type, region" /></td>
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
Gets all <code>sdi_sources</code> in a region.
```sql
SELECT
region,
arn,
id,
mode,
name,
state,
type,
inputs,
tags
FROM aws.medialive.sdi_sources
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>sdi_source</code>.
```sql
SELECT
region,
arn,
id,
mode,
name,
state,
type,
inputs,
tags
FROM aws.medialive.sdi_sources
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sdi_source</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.medialive.sdi_sources (
 Name,
 Type,
 region
)
SELECT 
'{{ Name }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.medialive.sdi_sources (
 Mode,
 Name,
 Type,
 Tags,
 region
)
SELECT 
 '{{ Mode }}',
 '{{ Name }}',
 '{{ Type }}',
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
  - name: sdi_source
    props:
      - name: Mode
        value: '{{ Mode }}'
      - name: Name
        value: '{{ Name }}'
      - name: Type
        value: '{{ Type }}'
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
DELETE FROM aws.medialive.sdi_sources
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>sdi_sources</code> resource, the following permissions are required:

### Create
```json
medialive:CreateSdiSource,
medialive:CreateTags,
medialive:DescribeSdiSource,
medialive:ListTagsForResource
```

### Read
```json
medialive:DescribeSdiSource,
medialive:ListTagsForResource
```

### Update
```json
medialive:UpdateSdiSource,
medialive:DescribeSdiSource,
medialive:CreateTags,
medialive:DeleteTags,
medialive:ListTagsForResource
```

### Delete
```json
medialive:DeleteSdiSource,
medialive:DescribeSdiSource
```

### List
```json
medialive:ListSdiSources
```
