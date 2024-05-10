---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - workspacesthinclient
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


Used to retrieve a list of <code>environments</code> in a region or to create or delete a <code>environments</code> resource, use <code>environment</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::WorkSpacesThinClient::Environment.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspacesthinclient.environments" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Unique identifier of the environment.</td></tr>
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
id
FROM aws.workspacesthinclient.environments
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
 "DesktopArn": "{{ DesktopArn }}"
}
>>>
--required properties only
INSERT INTO aws.workspacesthinclient.environments (
 DesktopArn,
 region
)
SELECT 
{{ .DesktopArn }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "DesktopArn": "{{ DesktopArn }}",
 "DesktopEndpoint": "{{ DesktopEndpoint }}",
 "SoftwareSetUpdateSchedule": "{{ SoftwareSetUpdateSchedule }}",
 "MaintenanceWindow": {
  "Type": "{{ Type }}",
  "StartTimeHour": "{{ StartTimeHour }}",
  "StartTimeMinute": "{{ StartTimeMinute }}",
  "EndTimeHour": null,
  "EndTimeMinute": null,
  "DaysOfTheWeek": [
   "{{ DaysOfTheWeek[0] }}"
  ],
  "ApplyTimeOf": "{{ ApplyTimeOf }}"
 },
 "SoftwareSetUpdateMode": "{{ SoftwareSetUpdateMode }}",
 "DesiredSoftwareSetId": "{{ DesiredSoftwareSetId }}",
 "KmsKeyArn": "{{ KmsKeyArn }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.workspacesthinclient.environments (
 Name,
 DesktopArn,
 DesktopEndpoint,
 SoftwareSetUpdateSchedule,
 MaintenanceWindow,
 SoftwareSetUpdateMode,
 DesiredSoftwareSetId,
 KmsKeyArn,
 Tags,
 region
)
SELECT 
 {{ .Name }},
 {{ .DesktopArn }},
 {{ .DesktopEndpoint }},
 {{ .SoftwareSetUpdateSchedule }},
 {{ .MaintenanceWindow }},
 {{ .SoftwareSetUpdateMode }},
 {{ .DesiredSoftwareSetId }},
 {{ .KmsKeyArn }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.workspacesthinclient.environments
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>environments</code> resource, the following permissions are required:

### Create
```json
thinclient:CreateEnvironment,
thinclient:TagResource,
thinclient:ListTagsForResource,
appstream:DescribeStacks,
workspaces:DescribeWorkspaceDirectories,
workspaces-web:GetPortal,
workspaces-web:GetUserSettings,
kms:DescribeKey,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```

### Delete
```json
thinclient:DeleteEnvironment,
thinclient:UntagResource,
kms:Decrypt,
kms:RetireGrant
```

### List
```json
thinclient:ListEnvironment,
thinclient:ListTagsForResource,
kms:Decrypt
```

