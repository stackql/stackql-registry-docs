---
title: user_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - user_settings
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

Creates, updates, deletes or gets an <code>user_setting</code> resource or lists <code>user_settings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::WorkSpacesWeb::UserSettings Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspacesweb.user_settings" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="additional_encryption_context" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="associated_portal_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="cookie_synchronization_configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="copy_allowed" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="customer_managed_key" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="disconnect_timeout_in_minutes" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="download_allowed" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="idle_disconnect_timeout_in_minutes" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="paste_allowed" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="print_allowed" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="upload_allowed" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="user_settings_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="CopyAllowed, DownloadAllowed, PasteAllowed, PrintAllowed, UploadAllowed, region" /></td>
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
List all <code>user_settings</code> in a region.
```sql
SELECT
region,
user_settings_arn
FROM aws.workspacesweb.user_settings
WHERE region = 'us-east-1';
```
Gets all properties from an <code>user_setting</code>.
```sql
SELECT
region,
additional_encryption_context,
associated_portal_arns,
cookie_synchronization_configuration,
copy_allowed,
customer_managed_key,
disconnect_timeout_in_minutes,
download_allowed,
idle_disconnect_timeout_in_minutes,
paste_allowed,
print_allowed,
tags,
upload_allowed,
user_settings_arn
FROM aws.workspacesweb.user_settings
WHERE region = 'us-east-1' AND data__Identifier = '<UserSettingsArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user_setting</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.workspacesweb.user_settings (
 CopyAllowed,
 DownloadAllowed,
 PasteAllowed,
 PrintAllowed,
 UploadAllowed,
 region
)
SELECT 
'{{ CopyAllowed }}',
 '{{ DownloadAllowed }}',
 '{{ PasteAllowed }}',
 '{{ PrintAllowed }}',
 '{{ UploadAllowed }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.workspacesweb.user_settings (
 AdditionalEncryptionContext,
 CookieSynchronizationConfiguration,
 CopyAllowed,
 CustomerManagedKey,
 DisconnectTimeoutInMinutes,
 DownloadAllowed,
 IdleDisconnectTimeoutInMinutes,
 PasteAllowed,
 PrintAllowed,
 Tags,
 UploadAllowed,
 region
)
SELECT 
 '{{ AdditionalEncryptionContext }}',
 '{{ CookieSynchronizationConfiguration }}',
 '{{ CopyAllowed }}',
 '{{ CustomerManagedKey }}',
 '{{ DisconnectTimeoutInMinutes }}',
 '{{ DownloadAllowed }}',
 '{{ IdleDisconnectTimeoutInMinutes }}',
 '{{ PasteAllowed }}',
 '{{ PrintAllowed }}',
 '{{ Tags }}',
 '{{ UploadAllowed }}',
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
  - name: user_setting
    props:
      - name: AdditionalEncryptionContext
        value: {}
      - name: CookieSynchronizationConfiguration
        value:
          Allowlist:
            - Domain: '{{ Domain }}'
              Name: '{{ Name }}'
              Path: '{{ Path }}'
          Blocklist:
            - null
      - name: CopyAllowed
        value: '{{ CopyAllowed }}'
      - name: CustomerManagedKey
        value: '{{ CustomerManagedKey }}'
      - name: DisconnectTimeoutInMinutes
        value: null
      - name: DownloadAllowed
        value: null
      - name: IdleDisconnectTimeoutInMinutes
        value: null
      - name: PasteAllowed
        value: null
      - name: PrintAllowed
        value: null
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: UploadAllowed
        value: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.workspacesweb.user_settings
WHERE data__Identifier = '<UserSettingsArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>user_settings</code> resource, the following permissions are required:

### Create
```json
workspaces-web:CreateUserSettings,
workspaces-web:GetUserSettings,
workspaces-web:ListTagsForResource,
workspaces-web:TagResource,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Read
```json
workspaces-web:GetUserSettings,
workspaces-web:ListTagsForResource,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Update
```json
workspaces-web:UpdateUserSettings,
workspaces-web:TagResource,
workspaces-web:UntagResource,
workspaces-web:GetUserSettings,
workspaces-web:ListTagsForResource,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Delete
```json
workspaces-web:GetUserSettings,
workspaces-web:DeleteUserSettings,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### List
```json
workspaces-web:ListUserSettings,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

