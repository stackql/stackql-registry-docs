---
title: environment_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_templates
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

Creates, updates, deletes or gets an <code>environment_template</code> resource or lists <code>environment_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Proton::EnvironmentTemplate Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.proton.environment_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The Amazon Resource Name (ARN) of the environment template.</p></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td><p>A description of the environment template.</p></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td><p>The environment template name as displayed in the developer interface.</p></td></tr>
<tr><td><CopyableCode code="encryption_key" /></td><td><code>string</code></td><td><p>A customer provided encryption key that Proton uses to encrypt data.</p></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="provisioning" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td><p>An optional list of metadata items that you can associate with the Proton environment template. A tag is a key-value pair.</p><br/>         <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the<br/>        <i>Proton User Guide</i>.</p></td></tr>
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
    <td><CopyableCode code="region" /></td>
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
List all <code>environment_templates</code> in a region.
```sql
SELECT
region,
arn
FROM aws.proton.environment_templates
WHERE region = 'us-east-1';
```
Gets all properties from an <code>environment_template</code>.
```sql
SELECT
region,
arn,
description,
display_name,
encryption_key,
name,
provisioning,
tags
FROM aws.proton.environment_templates
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>environment_template</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.proton.environment_templates (
 Description,
 DisplayName,
 EncryptionKey,
 Name,
 Provisioning,
 Tags,
 region
)
SELECT 
'{{ Description }}',
 '{{ DisplayName }}',
 '{{ EncryptionKey }}',
 '{{ Name }}',
 '{{ Provisioning }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.proton.environment_templates (
 Description,
 DisplayName,
 EncryptionKey,
 Name,
 Provisioning,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ DisplayName }}',
 '{{ EncryptionKey }}',
 '{{ Name }}',
 '{{ Provisioning }}',
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
  - name: environment_template
    props:
      - name: Description
        value: '{{ Description }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: EncryptionKey
        value: '{{ EncryptionKey }}'
      - name: Name
        value: '{{ Name }}'
      - name: Provisioning
        value: '{{ Provisioning }}'
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
DELETE FROM aws.proton.environment_templates
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>environment_templates</code> resource, the following permissions are required:

### Create
```json
proton:CreateEnvironmentTemplate,
proton:TagResource,
proton:GetEnvironmentTemplate,
kms:*
```

### Read
```json
proton:GetEnvironmentTemplate,
proton:ListTagsForResource,
kms:*
```

### Update
```json
proton:CreateEnvironmentTemplate,
proton:ListTagsForResource,
proton:TagResource,
proton:UntagResource,
proton:UpdateEnvironmentTemplate,
proton:GetEnvironmentTemplate,
kms:*
```

### Delete
```json
proton:DeleteEnvironmentTemplate,
proton:GetEnvironmentTemplate,
kms:*
```

### List
```json
proton:ListEnvironmentTemplates
```

