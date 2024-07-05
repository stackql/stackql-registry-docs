---
title: secret_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - secret_tags
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

Expands all tag keys and values for <code>secrets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secret_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a new secret. A *secret* can be a password, a set of credentials such as a user name and password, an OAuth token, or other secret information that you store in an encrypted form in Secrets Manager.<br />For RDS master user credentials, see &#91;AWS::RDS::DBCluster MasterUserSecret&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-masterusersecret.html).<br />To retrieve a secret in a CFNshort template, use a *dynamic reference*. For more information, see &#91;Retrieve a secret in an resource&#93;(https://docs.aws.amazon.com/secretsmanager/latest/userguide/cfn-example_reference-secret.html).<br />A common scenario is to first create a secret with <code>GenerateSecretString</code>, which generates a password, and then use a dynamic reference to retrieve the username and password from the secret to use as credentials for a new database. See the example *Creating a Redshift cluster and a secret for the admin credentials*.<br />For information about creating a secret in the console, see &#91;Create a secret&#93;(https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html). For information about creating a secret using the CLI or SDK, see &#91;CreateSecret&#93;(https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html).<br />For information about retrieving a secret in code, see &#91;Retrieve secrets from Secrets Manager&#93;(https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.secretsmanager.secret_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the secret.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The ARN, key ID, or alias of the KMS key that Secrets Manager uses to encrypt the secret value in the secret. An alias is always prefixed by <code>alias/</code>, for example <code>alias/aws/secretsmanager</code>. For more information, see &#91;About aliases&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/alias-about.html).<br />To use a KMS key in a different account, use the key ARN or the alias ARN.<br />If you don't specify this value, then Secrets Manager uses the key <code>aws/secretsmanager</code>. If that key doesn't yet exist, then Secrets Manager creates it for you automatically the first time it encrypts the secret value.<br />If the secret is in a different AWS account from the credentials calling the API, then you can't use <code>aws/secretsmanager</code> to encrypt the secret, and you must create and use a customer managed KMS key.</td></tr>
<tr><td><CopyableCode code="secret_string" /></td><td><code>string</code></td><td>The text to encrypt and store in the secret. We recommend you use a JSON structure of key/value pairs for your secret value. To generate a random password, use <code>GenerateSecretString</code> instead. If you omit both <code>GenerateSecretString</code> and <code>SecretString</code>, you create an empty secret. When you make a change to this property, a new secret version is created.</td></tr>
<tr><td><CopyableCode code="generate_secret_string" /></td><td><code>object</code></td><td>A structure that specifies how to generate a password to encrypt and store in the secret. To include a specific string in the secret, use <code>SecretString</code> instead. If you omit both <code>GenerateSecretString</code> and <code>SecretString</code>, you create an empty secret. When you make a change to this property, a new secret version is created.<br />We recommend that you specify the maximum length and include every character type that the system you are generating a password for can support.</td></tr>
<tr><td><CopyableCode code="replica_regions" /></td><td><code>array</code></td><td>A custom type that specifies a <code>Region</code> and the <code>KmsKeyId</code> for a replica secret.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the new secret.<br />The secret name can contain ASCII letters, numbers, and the following characters: /_+=.@-<br />Do not end your secret name with a hyphen followed by six characters. If you do so, you risk confusion and unexpected results when searching for a secret by partial ARN. Secrets Manager automatically adds a hyphen and six random characters after the secret name at the end of the ARN.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>secrets</code> in a region.
```sql
SELECT
region,
description,
kms_key_id,
secret_string,
generate_secret_string,
replica_regions,
id,
name,
tag_key,
tag_value
FROM aws.secretsmanager.secret_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>secret_tags</code> resource, see <a href="/providers/aws/secretsmanager/secrets/#permissions"><code>secrets</code></a>


