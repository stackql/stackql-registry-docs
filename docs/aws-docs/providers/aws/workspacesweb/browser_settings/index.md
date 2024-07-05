---
title: browser_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - browser_settings
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

Creates, updates, deletes or gets a <code>browser_setting</code> resource or lists <code>browser_settings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>browser_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::WorkSpacesWeb::BrowserSettings Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspacesweb.browser_settings" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="additional_encryption_context" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="associated_portal_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="browser_policy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="browser_settings_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="customer_managed_key" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>browser_settings</code> in a region.
```sql
SELECT
region,
additional_encryption_context,
associated_portal_arns,
browser_policy,
browser_settings_arn,
customer_managed_key,
tags
FROM aws.workspacesweb.browser_settings
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>browser_setting</code>.
```sql
SELECT
region,
additional_encryption_context,
associated_portal_arns,
browser_policy,
browser_settings_arn,
customer_managed_key,
tags
FROM aws.workspacesweb.browser_settings
WHERE region = 'us-east-1' AND data__Identifier = '<BrowserSettingsArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>browser_setting</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.workspacesweb.browser_settings (
 AdditionalEncryptionContext,
 BrowserPolicy,
 CustomerManagedKey,
 Tags,
 region
)
SELECT 
'{{ AdditionalEncryptionContext }}',
 '{{ BrowserPolicy }}',
 '{{ CustomerManagedKey }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.workspacesweb.browser_settings (
 AdditionalEncryptionContext,
 BrowserPolicy,
 CustomerManagedKey,
 Tags,
 region
)
SELECT 
 '{{ AdditionalEncryptionContext }}',
 '{{ BrowserPolicy }}',
 '{{ CustomerManagedKey }}',
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
  - name: browser_setting
    props:
      - name: AdditionalEncryptionContext
        value: {}
      - name: BrowserPolicy
        value: '{{ BrowserPolicy }}'
      - name: CustomerManagedKey
        value: '{{ CustomerManagedKey }}'
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
DELETE FROM aws.workspacesweb.browser_settings
WHERE data__Identifier = '<BrowserSettingsArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>browser_settings</code> resource, the following permissions are required:

### Create
```json
workspaces-web:CreateBrowserSettings,
workspaces-web:GetBrowserSettings,
workspaces-web:ListTagsForResource,
workspaces-web:TagResource,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Read
```json
workspaces-web:GetBrowserSettings,
workspaces-web:ListBrowserSettings,
workspaces-web:ListTagsForResource,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Update
```json
workspaces-web:UpdateBrowserSettings,
workspaces-web:TagResource,
workspaces-web:UntagResource,
workspaces-web:GetBrowserSettings,
workspaces-web:ListBrowserSettings,
workspaces-web:ListTagsForResource,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Delete
```json
workspaces-web:GetBrowserSettings,
workspaces-web:DeleteBrowserSettings,
kms:CreateGrant,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### List
```json
workspaces-web:ListBrowserSettings
```

