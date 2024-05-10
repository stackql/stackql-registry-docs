---
title: origin_endpoint_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_endpoint_policies
  - mediapackagev2
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


Used to retrieve a list of <code>origin_endpoint_policies</code> in a region or to create or delete a <code>origin_endpoint_policies</code> resource, use <code>origin_endpoint_policy</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_endpoint_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>&lt;p&gt;Represents a resource policy that allows or denies access to an origin endpoint.&lt;&#x2F;p&gt;</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackagev2.origin_endpoint_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="channel_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="channel_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="origin_endpoint_name" /></td><td><code>string</code></td><td></td></tr>
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
channel_group_name,
channel_name,
origin_endpoint_name
FROM aws.mediapackagev2.origin_endpoint_policies
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
 "ChannelGroupName": "{{ ChannelGroupName }}",
 "ChannelName": "{{ ChannelName }}",
 "OriginEndpointName": "{{ OriginEndpointName }}",
 "Policy": {}
}
>>>
--required properties only
INSERT INTO aws.mediapackagev2.origin_endpoint_policies (
 ChannelGroupName,
 ChannelName,
 OriginEndpointName,
 Policy,
 region
)
SELECT 
{{ .ChannelGroupName }},
 {{ .ChannelName }},
 {{ .OriginEndpointName }},
 {{ .Policy }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ChannelGroupName": "{{ ChannelGroupName }}",
 "ChannelName": "{{ ChannelName }}",
 "OriginEndpointName": "{{ OriginEndpointName }}",
 "Policy": {}
}
>>>
--all properties
INSERT INTO aws.mediapackagev2.origin_endpoint_policies (
 ChannelGroupName,
 ChannelName,
 OriginEndpointName,
 Policy,
 region
)
SELECT 
 {{ .ChannelGroupName }},
 {{ .ChannelName }},
 {{ .OriginEndpointName }},
 {{ .Policy }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.mediapackagev2.origin_endpoint_policies
WHERE data__Identifier = '<ChannelGroupName|ChannelName|OriginEndpointName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>origin_endpoint_policies</code> resource, the following permissions are required:

### Create
```json
mediapackagev2:GetOriginEndpointPolicy,
mediapackagev2:PutOriginEndpointPolicy
```

### Delete
```json
mediapackagev2:GetOriginEndpointPolicy,
mediapackagev2:DeleteOriginEndpointPolicy
```

