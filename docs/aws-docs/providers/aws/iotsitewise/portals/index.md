---
title: portals
hide_title: false
hide_table_of_contents: false
keywords:
  - portals
  - iotsitewise
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


Used to retrieve a list of <code>portals</code> in a region or to create or delete a <code>portals</code> resource, use <code>portal</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>portals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTSiteWise::Portal</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotsitewise.portals" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="portal_id" /></td><td><code>string</code></td><td>The ID of the portal.</td></tr>
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
portal_id
FROM aws.iotsitewise.portals
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
 "PortalContactEmail": "{{ PortalContactEmail }}",
 "PortalName": "{{ PortalName }}",
 "RoleArn": "{{ RoleArn }}"
}
>>>
--required properties only
INSERT INTO aws.iotsitewise.portals (
 PortalContactEmail,
 PortalName,
 RoleArn,
 region
)
SELECT 
{{ PortalContactEmail }},
 {{ PortalName }},
 {{ RoleArn }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "PortalAuthMode": "{{ PortalAuthMode }}",
 "PortalContactEmail": "{{ PortalContactEmail }}",
 "PortalDescription": "{{ PortalDescription }}",
 "PortalName": "{{ PortalName }}",
 "RoleArn": "{{ RoleArn }}",
 "NotificationSenderEmail": "{{ NotificationSenderEmail }}",
 "Alarms": {
  "AlarmRoleArn": "{{ AlarmRoleArn }}",
  "NotificationLambdaArn": "{{ NotificationLambdaArn }}"
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
INSERT INTO aws.iotsitewise.portals (
 PortalAuthMode,
 PortalContactEmail,
 PortalDescription,
 PortalName,
 RoleArn,
 NotificationSenderEmail,
 Alarms,
 Tags,
 region
)
SELECT 
 {{ PortalAuthMode }},
 {{ PortalContactEmail }},
 {{ PortalDescription }},
 {{ PortalName }},
 {{ RoleArn }},
 {{ NotificationSenderEmail }},
 {{ Alarms }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iotsitewise.portals
WHERE data__Identifier = '<PortalId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>portals</code> resource, the following permissions are required:

### Create
```json
iotsitewise:CreatePortal,
iotsitewise:DescribePortal,
iotsitewise:ListTagsForResource,
iotsitewise:TagResource,
iam:PassRole,
sso:CreateManagedApplicationInstance,
sso:DescribeRegisteredRegions
```

### Delete
```json
iotsitewise:DescribePortal,
iotsitewise:DeletePortal,
sso:DeleteManagedApplicationInstance
```

### List
```json
iotsitewise:ListPortals
```

