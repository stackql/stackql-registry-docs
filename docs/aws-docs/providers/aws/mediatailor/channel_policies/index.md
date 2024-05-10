---
title: channel_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - channel_policies
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


Used to retrieve a list of <code>channel_policies</code> in a region or to create or delete a <code>channel_policies</code> resource, use <code>channel_policy</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaTailor::ChannelPolicy Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediatailor.channel_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="channel_name" /></td><td><code>string</code></td><td></td></tr>
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
channel_name
FROM aws.mediatailor.channel_policies
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
 "ChannelName": "{{ ChannelName }}",
 "Policy": {}
}
>>>
--required properties only
INSERT INTO aws.mediatailor.channel_policies (
 ChannelName,
 Policy,
 region
)
SELECT 
{{ .ChannelName }},
 {{ .Policy }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ChannelName": "{{ ChannelName }}",
 "Policy": {}
}
>>>
--all properties
INSERT INTO aws.mediatailor.channel_policies (
 ChannelName,
 Policy,
 region
)
SELECT 
 {{ .ChannelName }},
 {{ .Policy }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.mediatailor.channel_policies
WHERE data__Identifier = '<ChannelName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>channel_policies</code> resource, the following permissions are required:

### Create
```json
mediatailor:PutChannelPolicy,
mediatailor:GetChannelPolicy
```

### Delete
```json
mediatailor:DeleteChannelPolicy,
mediatailor:GetChannelPolicy
```

