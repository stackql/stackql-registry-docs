---
title: template_group_access_control_entries
hide_title: false
hide_table_of_contents: false
keywords:
  - template_group_access_control_entries
  - pcaconnectorad
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


Used to retrieve a list of <code>template_group_access_control_entries</code> in a region or to create or delete a <code>template_group_access_control_entries</code> resource, use <code>template_group_access_control_entry</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>template_group_access_control_entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::PCAConnectorAD::TemplateGroupAccessControlEntry Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pcaconnectorad.template_group_access_control_entries" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="group_security_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="template_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="AccessRights, GroupDisplayName, region" /></td>
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
group_security_identifier,
template_arn
FROM aws.pcaconnectorad.template_group_access_control_entries
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>template_group_access_control_entry</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.pcaconnectorad.template_group_access_control_entries (
 AccessRights,
 GroupDisplayName,
 region
)
SELECT 
'{{ AccessRights }}',
 '{{ GroupDisplayName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.pcaconnectorad.template_group_access_control_entries (
 AccessRights,
 GroupDisplayName,
 GroupSecurityIdentifier,
 TemplateArn,
 region
)
SELECT 
 '{{ AccessRights }}',
 '{{ GroupDisplayName }}',
 '{{ GroupSecurityIdentifier }}',
 '{{ TemplateArn }}',
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
  - name: template_group_access_control_entry
    props:
      - name: AccessRights
        value:
          Enroll: '{{ Enroll }}'
          AutoEnroll: null
      - name: GroupDisplayName
        value: '{{ GroupDisplayName }}'
      - name: GroupSecurityIdentifier
        value: '{{ GroupSecurityIdentifier }}'
      - name: TemplateArn
        value: '{{ TemplateArn }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.pcaconnectorad.template_group_access_control_entries
WHERE data__Identifier = '<GroupSecurityIdentifier|TemplateArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>template_group_access_control_entries</code> resource, the following permissions are required:

### Create
```json
pca-connector-ad:CreateTemplateGroupAccessControlEntry
```

### Delete
```json
pca-connector-ad:DeleteTemplateGroupAccessControlEntry,
pca-connector-ad:GetTemplateGroupAccessControlEntry
```

### List
```json
pca-connector-ad:ListTemplateGroupAccessControlEntries
```

