---
title: provisioning_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - provisioning_templates
  - iot
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


Used to retrieve a list of <code>provisioning_templates</code> in a region or to create or delete a <code>provisioning_templates</code> resource, use <code>provisioning_template</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provisioning_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a fleet provisioning template.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.provisioning_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="template_name" /></td><td><code>string</code></td><td></td></tr>
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
template_name
FROM aws.iot.provisioning_templates
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
 "ProvisioningRoleArn": "{{ ProvisioningRoleArn }}",
 "TemplateBody": "{{ TemplateBody }}"
}
>>>
--required properties only
INSERT INTO aws.iot.provisioning_templates (
 ProvisioningRoleArn,
 TemplateBody,
 region
)
SELECT 
{{ ProvisioningRoleArn }},
 {{ TemplateBody }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "TemplateName": "{{ TemplateName }}",
 "Description": "{{ Description }}",
 "Enabled": "{{ Enabled }}",
 "ProvisioningRoleArn": "{{ ProvisioningRoleArn }}",
 "TemplateBody": "{{ TemplateBody }}",
 "TemplateType": "{{ TemplateType }}",
 "PreProvisioningHook": {
  "TargetArn": "{{ TargetArn }}",
  "PayloadVersion": "{{ PayloadVersion }}"
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
INSERT INTO aws.iot.provisioning_templates (
 TemplateName,
 Description,
 Enabled,
 ProvisioningRoleArn,
 TemplateBody,
 TemplateType,
 PreProvisioningHook,
 Tags,
 region
)
SELECT 
 {{ TemplateName }},
 {{ Description }},
 {{ Enabled }},
 {{ ProvisioningRoleArn }},
 {{ TemplateBody }},
 {{ TemplateType }},
 {{ PreProvisioningHook }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iot.provisioning_templates
WHERE data__Identifier = '<TemplateName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>provisioning_templates</code> resource, the following permissions are required:

### Create
```json
iam:GetRole,
iam:PassRole,
iot:CreateProvisioningTemplate,
iot:DescribeProvisioningTemplate,
iot:TagResource,
iot:ListTagsForResource
```

### Delete
```json
iot:DeleteProvisioningTemplate,
iot:DescribeProvisioningTemplate
```

### List
```json
iot:ListProvisioningTemplates
```

