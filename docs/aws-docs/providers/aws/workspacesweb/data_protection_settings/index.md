---
title: data_protection_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - data_protection_settings
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

Creates, updates, deletes or gets a <code>data_protection_setting</code> resource or lists <code>data_protection_settings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_protection_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::WorkSpacesWeb::DataProtectionSettings Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspacesweb.data_protection_settings" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="additional_encryption_context" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="associated_portal_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="customer_managed_key" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_protection_settings_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="inline_redaction_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-dataprotectionsetting.html"><code>AWS::WorkSpacesWeb::DataProtectionSettings</code></a>.

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
Gets all <code>data_protection_settings</code> in a region.
```sql
SELECT
region,
additional_encryption_context,
associated_portal_arns,
creation_date,
customer_managed_key,
data_protection_settings_arn,
description,
display_name,
inline_redaction_configuration,
tags
FROM aws.workspacesweb.data_protection_settings
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>data_protection_setting</code>.
```sql
SELECT
region,
additional_encryption_context,
associated_portal_arns,
creation_date,
customer_managed_key,
data_protection_settings_arn,
description,
display_name,
inline_redaction_configuration,
tags
FROM aws.workspacesweb.data_protection_settings
WHERE region = 'us-east-1' AND data__Identifier = '<DataProtectionSettingsArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_protection_setting</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.workspacesweb.data_protection_settings (
 AdditionalEncryptionContext,
 CustomerManagedKey,
 Description,
 DisplayName,
 InlineRedactionConfiguration,
 Tags,
 region
)
SELECT 
'{{ AdditionalEncryptionContext }}',
 '{{ CustomerManagedKey }}',
 '{{ Description }}',
 '{{ DisplayName }}',
 '{{ InlineRedactionConfiguration }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.workspacesweb.data_protection_settings (
 AdditionalEncryptionContext,
 CustomerManagedKey,
 Description,
 DisplayName,
 InlineRedactionConfiguration,
 Tags,
 region
)
SELECT 
 '{{ AdditionalEncryptionContext }}',
 '{{ CustomerManagedKey }}',
 '{{ Description }}',
 '{{ DisplayName }}',
 '{{ InlineRedactionConfiguration }}',
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
  - name: data_protection_setting
    props:
      - name: AdditionalEncryptionContext
        value: {}
      - name: CustomerManagedKey
        value: '{{ CustomerManagedKey }}'
      - name: Description
        value: '{{ Description }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: InlineRedactionConfiguration
        value:
          InlineRedactionPatterns:
            - BuiltInPatternId: '{{ BuiltInPatternId }}'
              CustomPattern:
                PatternName: '{{ PatternName }}'
                PatternRegex: '{{ PatternRegex }}'
                PatternDescription: '{{ PatternDescription }}'
                KeywordRegex: '{{ KeywordRegex }}'
              RedactionPlaceHolder:
                RedactionPlaceHolderType: '{{ RedactionPlaceHolderType }}'
                RedactionPlaceHolderText: '{{ RedactionPlaceHolderText }}'
              EnforcedUrls:
                - '{{ EnforcedUrls[0] }}'
              ExemptUrls:
                - '{{ ExemptUrls[0] }}'
              ConfidenceLevel: null
          GlobalEnforcedUrls:
            - '{{ GlobalEnforcedUrls[0] }}'
          GlobalExemptUrls:
            - '{{ GlobalExemptUrls[0] }}'
          GlobalConfidenceLevel: null
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
DELETE FROM aws.workspacesweb.data_protection_settings
WHERE data__Identifier = '<DataProtectionSettingsArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>data_protection_settings</code> resource, the following permissions are required:

### Create
```json
workspaces-web:CreateDataProtectionSettings,
workspaces-web:GetDataProtectionSettings,
workspaces-web:ListDataProtectionSettings,
workspaces-web:ListTagsForResource,
workspaces-web:TagResource,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt,
kms:GenerateDataKeyWithoutPlaintext,
kms:ReEncryptTo,
kms:ReEncryptFrom
```

### Read
```json
workspaces-web:GetDataProtectionSettings,
workspaces-web:ListDataProtectionSettings,
workspaces-web:ListTagsForResource,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Update
```json
workspaces-web:UpdateDataProtectionSettings,
workspaces-web:GetDataProtectionSettings,
workspaces-web:ListDataProtectionSettings,
workspaces-web:TagResource,
workspaces-web:UntagResource,
workspaces-web:ListTagsForResource,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Delete
```json
workspaces-web:GetDataProtectionSettings,
workspaces-web:ListDataProtectionSettings,
workspaces-web:DeleteDataProtectionSettings,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### List
```json
workspaces-web:ListDataProtectionSettings,
kms:Decrypt,
kms:DescribeKey
```
