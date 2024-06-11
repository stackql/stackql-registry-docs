---
title: ip_access_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_access_settings
  - workspacesweb
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

Creates, updates, deletes or gets an <code>ip_access_setting</code> resource or lists <code>ip_access_settings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_access_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::WorkSpacesWeb::IpAccessSettings Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspacesweb.ip_access_settings" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="additional_encryption_context" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="associated_portal_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="customer_managed_key" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ip_access_settings_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ip_rules" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="IpRules, region" /></td>
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
List all <code>ip_access_settings</code> in a region.
```sql
SELECT
region,
ip_access_settings_arn
FROM aws.workspacesweb.ip_access_settings
WHERE region = 'us-east-1';
```
Gets all properties from an <code>ip_access_setting</code>.
```sql
SELECT
region,
additional_encryption_context,
associated_portal_arns,
creation_date,
customer_managed_key,
description,
display_name,
ip_access_settings_arn,
ip_rules,
tags
FROM aws.workspacesweb.ip_access_settings
WHERE region = 'us-east-1' AND data__Identifier = '<IpAccessSettingsArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ip_access_setting</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.workspacesweb.ip_access_settings (
 IpRules,
 region
)
SELECT 
'{{ IpRules }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.workspacesweb.ip_access_settings (
 AdditionalEncryptionContext,
 CustomerManagedKey,
 Description,
 DisplayName,
 IpRules,
 Tags,
 region
)
SELECT 
 '{{ AdditionalEncryptionContext }}',
 '{{ CustomerManagedKey }}',
 '{{ Description }}',
 '{{ DisplayName }}',
 '{{ IpRules }}',
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
  - name: ip_access_setting
    props:
      - name: AdditionalEncryptionContext
        value: {}
      - name: CustomerManagedKey
        value: '{{ CustomerManagedKey }}'
      - name: Description
        value: '{{ Description }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: IpRules
        value:
          - IpRange: '{{ IpRange }}'
            Description: '{{ Description }}'
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
DELETE FROM aws.workspacesweb.ip_access_settings
WHERE data__Identifier = '<IpAccessSettingsArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>ip_access_settings</code> resource, the following permissions are required:

### Create
```json
workspaces-web:CreateIpAccessSettings,
workspaces-web:GetIpAccessSettings,
workspaces-web:ListIpAccessSettings,
workspaces-web:ListTagsForResource,
workspaces-web:TagResource,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Read
```json
workspaces-web:GetIpAccessSettings,
workspaces-web:ListIpAccessSettings,
workspaces-web:ListTagsForResource,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Update
```json
workspaces-web:UpdateIpAccessSettings,
workspaces-web:TagResource,
workspaces-web:UntagResource,
workspaces-web:GetIpAccessSettings,
workspaces-web:ListIpAccessSettings,
workspaces-web:ListTagsForResource,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Delete
```json
workspaces-web:GetIpAccessSettings,
workspaces-web:ListIpAccessSettings,
workspaces-web:DeleteIpAccessSettings,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### List
```json
workspaces-web:ListIpAccessSettings
```

