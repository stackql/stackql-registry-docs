---
title: configuration_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_profiles
  - appconfig
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


Used to retrieve a list of <code>configuration_profiles</code> in a region or to create or delete a <code>configuration_profiles</code> resource, use <code>configuration_profile</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appconfig.configuration_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td>The application ID.</td></tr>
<tr><td><CopyableCode code="configuration_profile_id" /></td><td><code>string</code></td><td>The configuration profile ID</td></tr>
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
application_id,
configuration_profile_id
FROM aws.appconfig.configuration_profiles
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
 "LocationUri": "{{ LocationUri }}",
 "ApplicationId": "{{ ApplicationId }}",
 "Name": "{{ Name }}"
}
>>>
--required properties only
INSERT INTO aws.appconfig.configuration_profiles (
 LocationUri,
 ApplicationId,
 Name,
 region
)
SELECT 
{{ .LocationUri }},
 {{ .ApplicationId }},
 {{ .Name }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "LocationUri": "{{ LocationUri }}",
 "Type": "{{ Type }}",
 "KmsKeyIdentifier": "{{ KmsKeyIdentifier }}",
 "Description": "{{ Description }}",
 "Validators": [
  {
   "Type": "{{ Type }}",
   "Content": "{{ Content }}"
  }
 ],
 "RetrievalRoleArn": "{{ RetrievalRoleArn }}",
 "ApplicationId": "{{ ApplicationId }}",
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "Name": "{{ Name }}"
}
>>>
--all properties
INSERT INTO aws.appconfig.configuration_profiles (
 LocationUri,
 Type,
 KmsKeyIdentifier,
 Description,
 Validators,
 RetrievalRoleArn,
 ApplicationId,
 Tags,
 Name,
 region
)
SELECT 
 {{ .LocationUri }},
 {{ .Type }},
 {{ .KmsKeyIdentifier }},
 {{ .Description }},
 {{ .Validators }},
 {{ .RetrievalRoleArn }},
 {{ .ApplicationId }},
 {{ .Tags }},
 {{ .Name }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.appconfig.configuration_profiles
WHERE data__Identifier = '<ApplicationId|ConfigurationProfileId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>configuration_profiles</code> resource, the following permissions are required:

### Create
```json
appconfig:CreateConfigurationProfile,
appconfig:GetConfigurationProfile,
appconfig:TagResource,
appconfig:ListTagsForResource,
iam:PassRole
```

### List
```json
appconfig:ListConfigurationProfiles
```

### Delete
```json
appconfig:DeleteConfigurationProfile
```

