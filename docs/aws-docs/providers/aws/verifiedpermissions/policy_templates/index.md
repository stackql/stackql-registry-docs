---
title: policy_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_templates
  - verifiedpermissions
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

Creates, updates, deletes or gets a <code>policy_template</code> resource or lists <code>policy_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::VerifiedPermissions::PolicyTemplate Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.verifiedpermissions.policy_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_store_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_template_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="statement" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="Statement, PolicyStoreId, region" /></td>
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
List all <code>policy_templates</code> in a region.
```sql
SELECT
region,
policy_store_id,
policy_template_id
FROM aws.verifiedpermissions.policy_templates
WHERE region = 'us-east-1';
```
Gets all properties from a <code>policy_template</code>.
```sql
SELECT
region,
description,
policy_store_id,
policy_template_id,
statement
FROM aws.verifiedpermissions.policy_templates
WHERE region = 'us-east-1' AND data__Identifier = '<PolicyStoreId>|<PolicyTemplateId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>policy_template</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.verifiedpermissions.policy_templates (
 PolicyStoreId,
 Statement,
 region
)
SELECT 
'{{ PolicyStoreId }}',
 '{{ Statement }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.verifiedpermissions.policy_templates (
 Description,
 PolicyStoreId,
 Statement,
 region
)
SELECT 
 '{{ Description }}',
 '{{ PolicyStoreId }}',
 '{{ Statement }}',
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
  - name: policy_template
    props:
      - name: Description
        value: '{{ Description }}'
      - name: PolicyStoreId
        value: '{{ PolicyStoreId }}'
      - name: Statement
        value: '{{ Statement }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.verifiedpermissions.policy_templates
WHERE data__Identifier = '<PolicyStoreId|PolicyTemplateId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>policy_templates</code> resource, the following permissions are required:

### Create
```json
verifiedpermissions:CreatePolicyTemplate,
verifiedpermissions:GetPolicyTemplate
```

### Read
```json
verifiedpermissions:GetPolicyTemplate
```

### Update
```json
verifiedpermissions:UpdatePolicyTemplate,
verifiedpermissions:GetPolicyTemplate
```

### Delete
```json
verifiedpermissions:DeletePolicyTemplate,
verifiedpermissions:GetPolicyTemplate
```

### List
```json
verifiedpermissions:ListPolicyTemplates,
verifiedpermissions:GetPolicyTemplate
```

