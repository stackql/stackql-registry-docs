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

Creates, updates, deletes or gets a <code>provisioning_template</code> resource or lists <code>provisioning_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provisioning_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a fleet provisioning template.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.provisioning_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="template_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="template_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="provisioning_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="template_body" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="template_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pre_provisioning_hook" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="ProvisioningRoleArn, TemplateBody, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>provisioning_templates</code> in a region.
```sql
SELECT
region,
template_name
FROM aws.iot.provisioning_templates
WHERE region = 'us-east-1';
```
Gets all properties from a <code>provisioning_template</code>.
```sql
SELECT
region,
template_arn,
template_name,
description,
enabled,
provisioning_role_arn,
template_body,
template_type,
pre_provisioning_hook,
tags
FROM aws.iot.provisioning_templates
WHERE region = 'us-east-1' AND data__Identifier = '<TemplateName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>provisioning_template</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.iot.provisioning_templates (
 ProvisioningRoleArn,
 TemplateBody,
 region
)
SELECT 
'{{ ProvisioningRoleArn }}',
 '{{ TemplateBody }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ TemplateName }}',
 '{{ Description }}',
 '{{ Enabled }}',
 '{{ ProvisioningRoleArn }}',
 '{{ TemplateBody }}',
 '{{ TemplateType }}',
 '{{ PreProvisioningHook }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: provisioning_template
    props:
      - name: TemplateName
        value: '{{ TemplateName }}'
      - name: Description
        value: '{{ Description }}'
      - name: Enabled
        value: '{{ Enabled }}'
      - name: ProvisioningRoleArn
        value: '{{ ProvisioningRoleArn }}'
      - name: TemplateBody
        value: '{{ TemplateBody }}'
      - name: TemplateType
        value: '{{ TemplateType }}'
      - name: PreProvisioningHook
        value:
          TargetArn: '{{ TargetArn }}'
          PayloadVersion: '{{ PayloadVersion }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
iot:DescribeProvisioningTemplate,
iot:ListTagsForResource
```

### Update
```json
iam:GetRole,
iam:PassRole,
iot:UpdateProvisioningTemplate,
iot:CreateProvisioningTemplateVersion,
iot:ListProvisioningTemplateVersions,
iot:DeleteProvisioningTemplateVersion,
iot:DescribeProvisioningTemplate,
iot:TagResource,
iot:UntagResource,
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

