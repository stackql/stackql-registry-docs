---
title: service_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - service_templates
  - proton
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


Used to retrieve a list of <code>service_templates</code> in a region or to create or delete a <code>service_templates</code> resource, use <code>service_template</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Proton::ServiceTemplate Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.proton.service_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Resource Name (ARN) of the service template.&lt;&#x2F;p&gt;</td></tr>
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
FROM aws.proton.service_templates
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
 "Description": "{{ Description }}",
 "DisplayName": "{{ DisplayName }}",
 "EncryptionKey": "{{ EncryptionKey }}",
 "Name": "{{ Name }}",
 "PipelineProvisioning": "{{ PipelineProvisioning }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.proton.service_templates (
 Description,
 DisplayName,
 EncryptionKey,
 Name,
 PipelineProvisioning,
 Tags,
 region
)
SELECT 
{{ .Description }},
 {{ .DisplayName }},
 {{ .EncryptionKey }},
 {{ .Name }},
 {{ .PipelineProvisioning }},
 {{ .Tags }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Description": "{{ Description }}",
 "DisplayName": "{{ DisplayName }}",
 "EncryptionKey": "{{ EncryptionKey }}",
 "Name": "{{ Name }}",
 "PipelineProvisioning": "{{ PipelineProvisioning }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.proton.service_templates (
 Description,
 DisplayName,
 EncryptionKey,
 Name,
 PipelineProvisioning,
 Tags,
 region
)
SELECT 
 {{ .Description }},
 {{ .DisplayName }},
 {{ .EncryptionKey }},
 {{ .Name }},
 {{ .PipelineProvisioning }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.proton.service_templates
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>service_templates</code> resource, the following permissions are required:

### Create
```json
proton:CreateServiceTemplate,
proton:TagResource,
kms:*,
proton:GetServiceTemplate
```

### Delete
```json
proton:DeleteServiceTemplate,
proton:UntagResource,
kms:*,
proton:GetServiceTemplate
```

### List
```json
proton:ListServiceTemplates
```

