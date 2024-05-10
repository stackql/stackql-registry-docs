---
title: live_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - live_sources
  - mediatailor
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


Used to retrieve a list of <code>live_sources</code> in a region or to create or delete a <code>live_sources</code> resource, use <code>live_source</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>live_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaTailor::LiveSource Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediatailor.live_sources" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="live_source_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source_location_name" /></td><td><code>string</code></td><td></td></tr>
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
live_source_name,
source_location_name
FROM aws.mediatailor.live_sources
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
 "HttpPackageConfigurations": [
  {
   "Path": "{{ Path }}",
   "SourceGroup": "{{ SourceGroup }}",
   "Type": "{{ Type }}"
  }
 ],
 "LiveSourceName": "{{ LiveSourceName }}",
 "SourceLocationName": "{{ SourceLocationName }}"
}
>>>
--required properties only
INSERT INTO aws.mediatailor.live_sources (
 HttpPackageConfigurations,
 LiveSourceName,
 SourceLocationName,
 region
)
SELECT 
{{ .HttpPackageConfigurations }},
 {{ .LiveSourceName }},
 {{ .SourceLocationName }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "HttpPackageConfigurations": [
  {
   "Path": "{{ Path }}",
   "SourceGroup": "{{ SourceGroup }}",
   "Type": "{{ Type }}"
  }
 ],
 "LiveSourceName": "{{ LiveSourceName }}",
 "SourceLocationName": "{{ SourceLocationName }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.mediatailor.live_sources (
 HttpPackageConfigurations,
 LiveSourceName,
 SourceLocationName,
 Tags,
 region
)
SELECT 
 {{ .HttpPackageConfigurations }},
 {{ .LiveSourceName }},
 {{ .SourceLocationName }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.mediatailor.live_sources
WHERE data__Identifier = '<LiveSourceName|SourceLocationName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>live_sources</code> resource, the following permissions are required:

### Create
```json
mediatailor:CreateLiveSource,
mediatailor:DescribeLiveSource,
mediatailor:TagResource
```

### Delete
```json
mediatailor:DeleteLiveSource,
mediatailor:DescribeLiveSource
```

### List
```json
mediatailor:ListLiveSources
```

