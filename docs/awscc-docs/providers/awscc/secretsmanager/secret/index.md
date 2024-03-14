---
title: secret
hide_title: false
hide_table_of_contents: false
keywords:
  - secret
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
Gets an individual <code>secret</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secret</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>secret</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.secretsmanager.secret</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the secret.</td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td>The ARN, key ID, or alias of the KMS key that Secrets Manager uses to encrypt the secret value in the secret. An alias is always prefixed by ``alias&#x2F;``, for example ``alias&#x2F;aws&#x2F;secretsmanager``. For more information, see &#91;About aliases&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;alias-about.html).&lt;br&#x2F;&gt; To use a KMS key in a different account, use the key ARN or the alias ARN.&lt;br&#x2F;&gt; If you don't specify this value, then Secrets Manager uses the key ``aws&#x2F;secretsmanager``. If that key doesn't yet exist, then Secrets Manager creates it for you automatically the first time it encrypts the secret value.&lt;br&#x2F;&gt; If the secret is in a different AWS account from the credentials calling the API, then you can't use ``aws&#x2F;secretsmanager`` to encrypt the secret, and you must create and use a customer managed KMS key.</td></tr>
<tr><td><code>secret_string</code></td><td><code>string</code></td><td>The text to encrypt and store in the secret. We recommend you use a JSON structure of key&#x2F;value pairs for your secret value. To generate a random password, use ``GenerateSecretString`` instead. If you omit both ``GenerateSecretString`` and ``SecretString``, you create an empty secret. When you make a change to this property, a new secret version is created.</td></tr>
<tr><td><code>generate_secret_string</code></td><td><code>object</code></td><td>A structure that specifies how to generate a password to encrypt and store in the secret. To include a specific string in the secret, use ``SecretString`` instead. If you omit both ``GenerateSecretString`` and ``SecretString``, you create an empty secret. When you make a change to this property, a new secret version is created.&lt;br&#x2F;&gt; We recommend that you specify the maximum length and include every character type that the system you are generating a password for can support.</td></tr>
<tr><td><code>replica_regions</code></td><td><code>array</code></td><td>A custom type that specifies a ``Region`` and the ``KmsKeyId`` for a replica secret.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of tags to attach to the secret. Each tag is a key and value pair of strings in a JSON text string, for example:&lt;br&#x2F;&gt;  ``&#91;&#123;"Key":"CostCenter","Value":"12345"&#125;,&#123;"Key":"environment","Value":"production"&#125;&#93;`` &lt;br&#x2F;&gt; Secrets Manager tag key names are case sensitive. A tag with the key "ABC" is a different tag from one with key "abc".&lt;br&#x2F;&gt; Stack-level tags, tags you apply to the CloudFormation stack, are also attached to the secret. &lt;br&#x2F;&gt; If you check tags in permissions policies as part of your security strategy, then adding or removing a tag can change permissions. If the completion of this operation would result in you losing your permissions for this secret, then Secrets Manager blocks the operation and returns an ``Access Denied`` error. For more information, see &#91;Control access to secrets using tags&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;secretsmanager&#x2F;latest&#x2F;userguide&#x2F;auth-and-access_examples.html#tag-secrets-abac) and &#91;Limit access to identities with tags that match secrets' tags&#93;(https:&#x2F;&#x2F;docs.aws.amazo</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the new secret.&lt;br&#x2F;&gt; The secret name can contain ASCII letters, numbers, and the following characters: &#x2F;_+=.@-&lt;br&#x2F;&gt; Do not end your secret name with a hyphen followed by six characters. If you do so, you risk confusion and unexpected results when searching for a secret by partial ARN. Secrets Manager automatically adds a hyphen and six random characters after the secret name at the end of the ARN.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.secretsmanager.secret
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>secret</code> resource, the following permissions are required:

### Delete
```json
secretsmanager:DeleteSecret,
secretsmanager:DescribeSecret,
secretsmanager:RemoveRegionsFromReplication
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

