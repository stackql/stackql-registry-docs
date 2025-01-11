---
title: user_pool_identity_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_identity_providers
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

Creates, updates, deletes or gets an <code>user_pool_identity_provider</code> resource or lists <code>user_pool_identity_providers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_identity_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPoolIdentityProvider</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.user_pool_identity_providers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="user_pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="provider_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="provider_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="provider_details" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="idp_identifiers" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="attribute_mapping" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolidentityprovider.html"><code>AWS::Cognito::UserPoolIdentityProvider</code></a>.

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
    <td><CopyableCode code="UserPoolId, ProviderName, ProviderType, ProviderDetails, region" /></td>
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
Gets all <code>user_pool_identity_providers</code> in a region.
```sql
SELECT
region,
user_pool_id,
provider_name,
provider_type,
provider_details,
idp_identifiers,
attribute_mapping
FROM aws.cognito.user_pool_identity_providers
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>user_pool_identity_provider</code>.
```sql
SELECT
region,
user_pool_id,
provider_name,
provider_type,
provider_details,
idp_identifiers,
attribute_mapping
FROM aws.cognito.user_pool_identity_providers
WHERE region = 'us-east-1' AND data__Identifier = '<UserPoolId>|<ProviderName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user_pool_identity_provider</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cognito.user_pool_identity_providers (
 UserPoolId,
 ProviderName,
 ProviderType,
 ProviderDetails,
 region
)
SELECT 
'{{ UserPoolId }}',
 '{{ ProviderName }}',
 '{{ ProviderType }}',
 '{{ ProviderDetails }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cognito.user_pool_identity_providers (
 UserPoolId,
 ProviderName,
 ProviderType,
 ProviderDetails,
 IdpIdentifiers,
 AttributeMapping,
 region
)
SELECT 
 '{{ UserPoolId }}',
 '{{ ProviderName }}',
 '{{ ProviderType }}',
 '{{ ProviderDetails }}',
 '{{ IdpIdentifiers }}',
 '{{ AttributeMapping }}',
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
  - name: user_pool_identity_provider
    props:
      - name: UserPoolId
        value: '{{ UserPoolId }}'
      - name: ProviderName
        value: '{{ ProviderName }}'
      - name: ProviderType
        value: '{{ ProviderType }}'
      - name: ProviderDetails
        value: {}
      - name: IdpIdentifiers
        value:
          - '{{ IdpIdentifiers[0] }}'
      - name: AttributeMapping
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cognito.user_pool_identity_providers
WHERE data__Identifier = '<UserPoolId|ProviderName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>user_pool_identity_providers</code> resource, the following permissions are required:

### Create
```json
cognito-idp:CreateIdentityProvider,
cognito-idp:DescribeIdentityProvider
```

### Read
```json
cognito-idp:DescribeIdentityProvider
```

### Update
```json
cognito-idp:UpdateIdentityProvider,
cognito-idp:DescribeIdentityProvider
```

### Delete
```json
cognito-idp:DeleteIdentityProvider,
cognito-idp:DescribeIdentityProvider
```

### List
```json
cognito-idp:ListIdentityProviders
```
