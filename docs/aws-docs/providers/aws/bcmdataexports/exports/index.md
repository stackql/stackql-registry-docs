---
title: exports
hide_title: false
hide_table_of_contents: false
keywords:
  - exports
  - bcmdataexports
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


Used to retrieve a list of <code>exports</code> in a region or to create or delete a <code>exports</code> resource, use <code>export</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>exports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::BCMDataExports::Export Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.bcmdataexports.exports" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="export_arn" /></td><td><code>string</code></td><td></td></tr>
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
export_arn
FROM aws.bcmdataexports.exports
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
 "Export": {
  "Export": null
 }
}
>>>
--required properties only
INSERT INTO aws.bcmdataexports.exports (
 Export,
 region
)
SELECT 
{{ .Export }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Export": {
  "Export": null,
  "Tags": [
   {
    "Key": "{{ Key }}",
    "Value": "{{ Value }}"
   }
  ]
 },
 "Tags": [
  null
 ]
}
>>>
--all properties
INSERT INTO aws.bcmdataexports.exports (
 Export,
 Tags,
 region
)
SELECT 
 {{ .Export }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.bcmdataexports.exports
WHERE data__Identifier = '<ExportArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>exports</code> resource, the following permissions are required:

### Create
```json
bcm-data-exports:CreateExport,
bcm-data-exports:GetExport,
bcm-data-exports:ListTagsForResource,
bcm-data-exports:TagResource,
cur:PutReportDefinition
```

### Delete
```json
bcm-data-exports:DeleteExport
```

### List
```json
bcm-data-exports:ListExports
```

