---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - datazone
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
<tr><td><b>Description</b></td><td>Definition of AWS::DataZone::Environment Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.environments" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The identifier of the Amazon DataZone domain in which the environment is created.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone environment.</td></tr>
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
domain_id,
id
FROM aws.datazone.environments
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
 "DomainIdentifier": "{{ DomainIdentifier }}",
 "EnvironmentProfileIdentifier": "{{ EnvironmentProfileIdentifier }}",
 "Name": "{{ Name }}",
 "ProjectIdentifier": "{{ ProjectIdentifier }}"
}
>>>
--required properties only
INSERT INTO aws.datazone.environments (
 DomainIdentifier,
 EnvironmentProfileIdentifier,
 Name,
 ProjectIdentifier,
 region
)
SELECT 
{{ .DomainIdentifier }},
 {{ .EnvironmentProfileIdentifier }},
 {{ .Name }},
 {{ .ProjectIdentifier }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Description": "{{ Description }}",
 "DomainIdentifier": "{{ DomainIdentifier }}",
 "EnvironmentProfileIdentifier": "{{ EnvironmentProfileIdentifier }}",
 "GlossaryTerms": [
  "{{ GlossaryTerms[0] }}"
 ],
 "Name": "{{ Name }}",
 "ProjectIdentifier": "{{ ProjectIdentifier }}",
 "UserParameters": [
  {
   "Name": "{{ Name }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.datazone.environments (
 Description,
 DomainIdentifier,
 EnvironmentProfileIdentifier,
 GlossaryTerms,
 Name,
 ProjectIdentifier,
 UserParameters,
 region
)
SELECT 
 {{ .Description }},
 {{ .DomainIdentifier }},
 {{ .EnvironmentProfileIdentifier }},
 {{ .GlossaryTerms }},
 {{ .Name }},
 {{ .ProjectIdentifier }},
 {{ .UserParameters }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.datazone.environments
WHERE data__Identifier = '<DomainId|Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>environments</code> resource, the following permissions are required:

### Create
```json
datazone:CreateEnvironment,
datazone:GetEnvironment,
datazone:DeleteEnvironment
```

### Delete
```json
datazone:DeleteEnvironment,
datazone:GetEnvironment
```

### List
```json
datazone:ListEnvironments
```

