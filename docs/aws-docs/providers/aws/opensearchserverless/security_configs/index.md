---
title: security_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - security_configs
  - opensearchserverless
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

Creates, updates, deletes or gets a <code>security_config</code> resource or lists <code>security_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Amazon OpenSearchServerless security config resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.opensearchserverless.security_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Security config description</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The identifier of the security config</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The friendly name of the security config</td></tr>
<tr><td><CopyableCode code="saml_options" /></td><td><code>object</code></td><td>Describes saml options in form of key value map</td></tr>
<tr><td><CopyableCode code="iam_identity_center_options" /></td><td><code>object</code></td><td>Describes IAM Identity Center options for an OpenSearch Serverless security configuration in the form of a key-value map</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>Config type for security config</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securityconfig.html"><code>AWS::OpenSearchServerless::SecurityConfig</code></a>.

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
Gets all <code>security_configs</code> in a region.
```sql
SELECT
region,
description,
id,
name,
saml_options,
iam_identity_center_options,
type
FROM aws.opensearchserverless.security_configs
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>security_config</code>.
```sql
SELECT
region,
description,
id,
name,
saml_options,
iam_identity_center_options,
type
FROM aws.opensearchserverless.security_configs
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_config</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.opensearchserverless.security_configs (
 Description,
 Name,
 SamlOptions,
 IamIdentityCenterOptions,
 Type,
 region
)
SELECT 
'{{ Description }}',
 '{{ Name }}',
 '{{ SamlOptions }}',
 '{{ IamIdentityCenterOptions }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.opensearchserverless.security_configs (
 Description,
 Name,
 SamlOptions,
 IamIdentityCenterOptions,
 Type,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Name }}',
 '{{ SamlOptions }}',
 '{{ IamIdentityCenterOptions }}',
 '{{ Type }}',
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
  - name: security_config
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: SamlOptions
        value:
          Metadata: '{{ Metadata }}'
          UserAttribute: '{{ UserAttribute }}'
          GroupAttribute: '{{ GroupAttribute }}'
          SessionTimeout: '{{ SessionTimeout }}'
      - name: IamIdentityCenterOptions
        value:
          InstanceArn: '{{ InstanceArn }}'
          ApplicationArn: '{{ ApplicationArn }}'
          ApplicationName: '{{ ApplicationName }}'
          ApplicationDescription: '{{ ApplicationDescription }}'
          UserAttribute: '{{ UserAttribute }}'
          GroupAttribute: '{{ GroupAttribute }}'
      - name: Type
        value: '{{ Type }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.opensearchserverless.security_configs
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>security_configs</code> resource, the following permissions are required:

### Create
```json
aoss:CreateSecurityConfig,
sso:CreateApplication,
sso:ListApplications,
sso:DeleteApplication,
sso:PutApplicationAssignmentConfiguration,
sso:PutApplicationAuthenticationMethod,
sso:PutApplicationGrant
```

### Read
```json
aoss:GetSecurityConfig
```

### Update
```json
aoss:GetSecurityConfig,
aoss:UpdateSecurityConfig
```

### Delete
```json
aoss:DeleteSecurityConfig,
sso:ListApplicationAssignments,
sso:DeleteApplicationAssignment,
sso:DeleteApplication
```

### List
```json
aoss:ListSecurityConfigs
```
