---
title: trust_anchors
hide_title: false
hide_table_of_contents: false
keywords:
  - trust_anchors
  - rolesanywhere
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


Used to retrieve a list of <code>trust_anchors</code> in a region or to create or delete a <code>trust_anchors</code> resource, use <code>trust_anchor</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trust_anchors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RolesAnywhere::TrustAnchor Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rolesanywhere.trust_anchors" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="trust_anchor_id" /></td><td><code>string</code></td><td></td></tr>
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
trust_anchor_id
FROM aws.rolesanywhere.trust_anchors
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
 "Name": "{{ Name }}",
 "Source": {
  "SourceType": "{{ SourceType }}",
  "SourceData": null
 }
}
>>>
--required properties only
INSERT INTO aws.rolesanywhere.trust_anchors (
 Name,
 Source,
 region
)
SELECT 
{{ Name }},
 {{ Source }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Enabled": "{{ Enabled }}",
 "Name": "{{ Name }}",
 "NotificationSettings": [
  {
   "Enabled": "{{ Enabled }}",
   "Event": "{{ Event }}",
   "Threshold": null,
   "Channel": "{{ Channel }}"
  }
 ],
 "Source": {
  "SourceType": "{{ SourceType }}",
  "SourceData": null
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.rolesanywhere.trust_anchors (
 Enabled,
 Name,
 NotificationSettings,
 Source,
 Tags,
 region
)
SELECT 
 {{ Enabled }},
 {{ Name }},
 {{ NotificationSettings }},
 {{ Source }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.rolesanywhere.trust_anchors
WHERE data__Identifier = '<TrustAnchorId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>trust_anchors</code> resource, the following permissions are required:

### Create
```json
iam:CreateServiceLinkedRole,
rolesanywhere:CreateTrustAnchor,
rolesanywhere:TagResource,
rolesanywhere:ListTagsForResource
```

### Delete
```json
rolesanywhere:DeleteTrustAnchor
```

### List
```json
rolesanywhere:ListTrustAnchors,
rolesanywhere:ListTagsForResource
```

