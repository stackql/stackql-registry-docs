---
title: view_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - view_versions
  - connect
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


Used to retrieve a list of <code>view_versions</code> in a region or to create or delete a <code>view_versions</code> resource, use <code>view_version</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>view_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::ViewVersion</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.view_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="view_version_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the created view version.</td></tr>
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
view_version_arn
FROM aws.connect.view_versions
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
 "ViewArn": "{{ ViewArn }}"
}
>>>
--required properties only
INSERT INTO aws.connect.view_versions (
 ViewArn,
 region
)
SELECT 
{{ .ViewArn }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ViewArn": "{{ ViewArn }}",
 "VersionDescription": "{{ VersionDescription }}",
 "ViewContentSha256": "{{ ViewContentSha256 }}"
}
>>>
--all properties
INSERT INTO aws.connect.view_versions (
 ViewArn,
 VersionDescription,
 ViewContentSha256,
 region
)
SELECT 
 {{ .ViewArn }},
 {{ .VersionDescription }},
 {{ .ViewContentSha256 }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.connect.view_versions
WHERE data__Identifier = '<ViewVersionArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>view_versions</code> resource, the following permissions are required:

### Create
```json
connect:CreateViewVersion
```

### List
```json
connect:ListViewVersions
```

### Delete
```json
connect:DeleteViewVersion
```

