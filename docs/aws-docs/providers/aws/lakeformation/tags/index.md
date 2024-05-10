---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
  - lakeformation
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


Used to retrieve a list of <code>tags</code> in a region or to create or delete a <code>tags</code> resource, use <code>tag</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource schema representing a Lake Formation Tag.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lakeformation.tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>undefined</code></td><td>The key-name for the LF-tag.</td></tr>
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
tag_key
FROM aws.lakeformation.tags
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
 "TagKey": "{{ TagKey }}",
 "TagValues": [
  "{{ TagValues[0] }}"
 ]
}
>>>
--required properties only
INSERT INTO aws.lakeformation.tags (
 TagKey,
 TagValues,
 region
)
SELECT 
{{ .TagKey }},
 {{ .TagValues }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "CatalogId": "{{ CatalogId }}",
 "TagKey": "{{ TagKey }}",
 "TagValues": [
  "{{ TagValues[0] }}"
 ]
}
>>>
--all properties
INSERT INTO aws.lakeformation.tags (
 CatalogId,
 TagKey,
 TagValues,
 region
)
SELECT 
 {{ .CatalogId }},
 {{ .TagKey }},
 {{ .TagValues }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.lakeformation.tags
WHERE data__Identifier = '<TagKey>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>tags</code> resource, the following permissions are required:

### Create
```json
lakeformation:CreateLFTag
```

### Delete
```json
lakeformation:DeleteLFTag
```

### List
```json
lakeformation:ListLFTags
```

