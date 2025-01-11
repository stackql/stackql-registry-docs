---
title: managed_login_brandings
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_login_brandings
  - cognito
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

Creates, updates, deletes or gets a <code>managed_login_branding</code> resource or lists <code>managed_login_brandings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_login_brandings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::ManagedLoginBranding</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.managed_login_brandings" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="user_pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="client_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="use_cognito_provided_values" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="settings" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="assets" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="managed_login_branding_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="return_merged_resources" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-managedloginbranding.html"><code>AWS::Cognito::ManagedLoginBranding</code></a>.

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
    <td><CopyableCode code="UserPoolId, region" /></td>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from an individual <code>managed_login_branding</code>.
```sql
SELECT
region,
user_pool_id,
client_id,
use_cognito_provided_values,
settings,
assets,
managed_login_branding_id,
return_merged_resources
FROM aws.cognito.managed_login_brandings
WHERE region = 'us-east-1' AND data__Identifier = '<UserPoolId>|<ManagedLoginBrandingId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_login_branding</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cognito.managed_login_brandings (
 UserPoolId,
 region
)
SELECT 
'{{ UserPoolId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cognito.managed_login_brandings (
 UserPoolId,
 ClientId,
 UseCognitoProvidedValues,
 Settings,
 Assets,
 ReturnMergedResources,
 region
)
SELECT 
 '{{ UserPoolId }}',
 '{{ ClientId }}',
 '{{ UseCognitoProvidedValues }}',
 '{{ Settings }}',
 '{{ Assets }}',
 '{{ ReturnMergedResources }}',
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
  - name: managed_login_branding
    props:
      - name: UserPoolId
        value: '{{ UserPoolId }}'
      - name: ClientId
        value: '{{ ClientId }}'
      - name: UseCognitoProvidedValues
        value: '{{ UseCognitoProvidedValues }}'
      - name: Settings
        value: {}
      - name: Assets
        value:
          - Category: '{{ Category }}'
            ColorMode: '{{ ColorMode }}'
            Extension: '{{ Extension }}'
            Bytes: '{{ Bytes }}'
            ResourceId: '{{ ResourceId }}'
      - name: ReturnMergedResources
        value: '{{ ReturnMergedResources }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cognito.managed_login_brandings
WHERE data__Identifier = '<UserPoolId|ManagedLoginBrandingId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>managed_login_brandings</code> resource, the following permissions are required:

### Create
```json
cognito-idp:CreateManagedLoginBranding
```

### Read
```json
cognito-idp:DescribeManagedLoginBranding
```

### Update
```json
cognito-idp:UpdateManagedLoginBranding
```

### Delete
```json
cognito-idp:DeleteManagedLoginBranding
```
