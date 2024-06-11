---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
  - secretsmanager
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

Creates, updates, deletes or gets a <code>secret</code> resource or lists <code>secrets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a new secret. A *secret* can be a password, a set of credentials such as a user name and password, an OAuth token, or other secret information that you store in an encrypted form in Secrets Manager. For RDS master user credentials, see &#91;AWS::RDS::DBCluster MasterUserSecret&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-masterusersecret.html). To retrieve a secret in a CFNshort template, use a *dynamic reference*. For more information, see &#91;Retrieve a secret in an resource&#93;(https://docs.aws.amazon.com/secretsmanager/latest/userguide/cfn-example_reference-secret.html). A common scenario is to first create a secret with <code>GenerateSecretString</code>, which generates a password, and then use a dynamic reference to retrieve the username and password from the secret to use as credentials for a new database. See the example *Creating a Redshift cluster and a secret for the admin credentials*. For information about creating a secret in the console, see &#91;Create a secret&#93;(https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html). For information about creating a secret using the CLI or SDK, see &#91;CreateSecret&#93;(https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html). For information about retrieving a secret in code, see &#91;Retrieve secrets from Secrets Manager&#93;(https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.secretsmanager.secrets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the secret.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The ARN, key ID, or alias of the KMS key that Secrets Manager uses to encrypt the secret value in the secret. An alias is always prefixed by <code>alias/</code>, for example <code>alias/aws/secretsmanager</code>. For more information, see &#91;About aliases&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/alias-about.html). To use a KMS key in a different account, use the key ARN or the alias ARN. If you don't specify this value, then Secrets Manager uses the key <code>aws/secretsmanager</code>. If that key doesn't yet exist, then Secrets Manager creates it for you automatically the first time it encrypts the secret value. If the secret is in a different AWS account from the credentials calling the API, then you can't use <code>aws/secretsmanager</code> to encrypt the secret, and you must create and use a customer managed KMS key.</td></tr>
<tr><td><CopyableCode code="secret_string" /></td><td><code>string</code></td><td>The text to encrypt and store in the secret. We recommend you use a JSON structure of key/value pairs for your secret value. To generate a random password, use <code>GenerateSecretString</code> instead. If you omit both <code>GenerateSecretString</code> and <code>SecretString</code>, you create an empty secret. When you make a change to this property, a new secret version is created.</td></tr>
<tr><td><CopyableCode code="generate_secret_string" /></td><td><code>object</code></td><td>A structure that specifies how to generate a password to encrypt and store in the secret. To include a specific string in the secret, use <code>SecretString</code> instead. If you omit both <code>GenerateSecretString</code> and <code>SecretString</code>, you create an empty secret. When you make a change to this property, a new secret version is created. We recommend that you specify the maximum length and include every character type that the system you are generating a password for can support.</td></tr>
<tr><td><CopyableCode code="replica_regions" /></td><td><code>array</code></td><td>A custom type that specifies a <code>Region</code> and the <code>KmsKeyId</code> for a replica secret.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of tags to attach to the secret. Each tag is a key and value pair of strings in a JSON text string, for example: <code>&#91;&#123;"Key":"CostCenter","Value":"12345"&#125;,&#123;"Key":"environment","Value":"production"&#125;&#93;</code> Secrets Manager tag key names are case sensitive. A tag with the key "ABC" is a different tag from one with key "abc". Stack-level tags, tags you apply to the CloudFormation stack, are also attached to the secret. If you check tags in permissions policies as part of your security strategy, then adding or removing a tag can change permissions. If the completion of this operation would result in you losing your permissions for this secret, then Secrets Manager blocks the operation and returns an <code>Access Denied</code> error. For more information, see &#91;Control access to secrets using tags&#93;(https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html#tag-secrets-abac) and &#91;Limit access to identities with tags that match secrets' tags&#93;(https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html#auth-and-access_tags2). For information about how to format a JSON parameter for the various command line tool environments, see &#91;Using JSON for Parameters&#93;(https://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json). If your command-line tool or SDK requires quotation marks around the parameter, you should use single quotes to avoid confusion with the double quotes required in the JSON text. The following restrictions apply to tags: + Maximum number of tags per secret: 50 + Maximum key length: 127 Unicode characters in UTF-8 + Maximum value length: 255 Unicode characters in UTF-8 + Tag keys and values are case sensitive. + Do not use the <code>aws:</code> prefix in your tag names or values because AWS reserves it for AWS use. You can't edit or delete tag names or values with this prefix. Tags with this prefix do not count against your tags per secret limit. + If you use your tagging schema across multiple services and resources, other services might have restrictions on allowed characters. Generally allowed characters: letters, spaces, and numbers representable in UTF-8, plus the following special characters: + - = . _ : / @.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the new secret. The secret name can contain ASCII letters, numbers, and the following characters: /_+=.@- Do not end your secret name with a hyphen followed by six characters. If you do so, you risk confusion and unexpected results when searching for a secret by partial ARN. Secrets Manager automatically adds a hyphen and six random characters after the secret name at the end of the ARN.</td></tr>
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
List all <code>secrets</code> in a region.
```sql
SELECT
region,
id
FROM aws.secretsmanager.secrets
WHERE region = 'us-east-1';
```
Gets all properties from a <code>secret</code>.
```sql
SELECT
region,
description,
kms_key_id,
secret_string,
generate_secret_string,
replica_regions,
id,
tags,
name
FROM aws.secretsmanager.secrets
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>secret</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.secretsmanager.secrets (
 Description,
 KmsKeyId,
 SecretString,
 GenerateSecretString,
 ReplicaRegions,
 Tags,
 Name,
 region
)
SELECT 
'{{ Description }}',
 '{{ KmsKeyId }}',
 '{{ SecretString }}',
 '{{ GenerateSecretString }}',
 '{{ ReplicaRegions }}',
 '{{ Tags }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.secretsmanager.secrets (
 Description,
 KmsKeyId,
 SecretString,
 GenerateSecretString,
 ReplicaRegions,
 Tags,
 Name,
 region
)
SELECT 
 '{{ Description }}',
 '{{ KmsKeyId }}',
 '{{ SecretString }}',
 '{{ GenerateSecretString }}',
 '{{ ReplicaRegions }}',
 '{{ Tags }}',
 '{{ Name }}',
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
  - name: secret
    props:
      - name: Description
        value: '{{ Description }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: SecretString
        value: '{{ SecretString }}'
      - name: GenerateSecretString
        value:
          ExcludeUppercase: '{{ ExcludeUppercase }}'
          RequireEachIncludedType: '{{ RequireEachIncludedType }}'
          IncludeSpace: '{{ IncludeSpace }}'
          ExcludeCharacters: '{{ ExcludeCharacters }}'
          GenerateStringKey: '{{ GenerateStringKey }}'
          PasswordLength: '{{ PasswordLength }}'
          ExcludePunctuation: '{{ ExcludePunctuation }}'
          ExcludeLowercase: '{{ ExcludeLowercase }}'
          SecretStringTemplate: '{{ SecretStringTemplate }}'
          ExcludeNumbers: '{{ ExcludeNumbers }}'
      - name: ReplicaRegions
        value:
          - KmsKeyId: '{{ KmsKeyId }}'
            Region: '{{ Region }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: Name
        value: '{{ Name }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.secretsmanager.secrets
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>secrets</code> resource, the following permissions are required:

### Create
```json
secretsmanager:DescribeSecret,
secretsmanager:GetRandomPassword,
secretsmanager:CreateSecret,
secretsmanager:TagResource
```

### Delete
```json
secretsmanager:DeleteSecret,
secretsmanager:DescribeSecret,
secretsmanager:RemoveRegionsFromReplication
```

### List
```json
secretsmanager:ListSecrets
```

### Read
```json
secretsmanager:DescribeSecret,
secretsmanager:GetSecretValue
```

### Update
```json
secretsmanager:UpdateSecret,
secretsmanager:TagResource,
secretsmanager:UntagResource,
secretsmanager:GetRandomPassword,
secretsmanager:GetSecretValue,
secretsmanager:ReplicateSecretToRegions,
secretsmanager:RemoveRegionsFromReplication
```

