---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
  - ivs
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


Used to retrieve a list of <code>channels</code> in a region or to create or delete a <code>channels</code> resource, use <code>channel</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IVS::Channel</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivs.channels" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Channel ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
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
arn
FROM aws.ivs.channels
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
{}
>>>
--required properties only
INSERT INTO aws.ivs.channels (
 ,
 region
)
SELECT 
{{ . }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Authorized": "{{ Authorized }}",
 "InsecureIngest": "{{ InsecureIngest }}",
 "LatencyMode": "{{ LatencyMode }}",
 "Type": "{{ Type }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "RecordingConfigurationArn": "{{ RecordingConfigurationArn }}",
 "Preset": "{{ Preset }}"
}
>>>
--all properties
INSERT INTO aws.ivs.channels (
 Name,
 Authorized,
 InsecureIngest,
 LatencyMode,
 Type,
 Tags,
 RecordingConfigurationArn,
 Preset,
 region
)
SELECT 
 {{ .Name }},
 {{ .Authorized }},
 {{ .InsecureIngest }},
 {{ .LatencyMode }},
 {{ .Type }},
 {{ .Tags }},
 {{ .RecordingConfigurationArn }},
 {{ .Preset }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ivs.channels
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>channels</code> resource, the following permissions are required:

### Create
```json
ivs:CreateChannel,
ivs:TagResource
```

### Delete
```json
ivs:DeleteChannel,
ivs:UnTagResource
```

### List
```json
ivs:ListChannels,
ivs:ListTagsForResource
```

