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


Used to retrieve a list of <code>secrets</code> in a region or to create or delete a <code>secrets</code> resource, use <code>secret</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a new secret. A *secret* can be a password, a set of credentials such as a user name and password, an OAuth token, or other secret information that you store in an encrypted form in Secrets Manager.&lt;br&#x2F;&gt; For RDS master user credentials, see &#91;AWS::RDS::DBCluster MasterUserSecret&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-rds-dbcluster-masterusersecret.html).&lt;br&#x2F;&gt; To retrieve a secret in a CFNshort template, use a *dynamic reference*. For more information, see &#91;Retrieve a secret in an resource&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;secretsmanager&#x2F;latest&#x2F;userguide&#x2F;cfn-example_reference-secret.html).&lt;br&#x2F;&gt; A common scenario is to first create a secret with ``GenerateSecretString``, which generates a password, and then use a dynamic reference to retrieve the username and password from the secret to use as credentials for a new database. See the example *Creating a Redshift cluster and a secret for the admin credentials*.&lt;br&#x2F;&gt; For information about creating a secret in the console, see &#91;Create a secret&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;secretsmanager&#x2F;latest&#x2F;userguide&#x2F;manage_create-basic-secret.html). For information about creating a secret using the CLI or SDK, see &#91;CreateSecret&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;secretsmanager&#x2F;latest&#x2F;apireference&#x2F;API_CreateSecret.html).&lt;br&#x2F;&gt; For information about retrieving a secret in code, see &#91;Retrieve secrets from Secrets Manager&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;secretsmanager&#x2F;latest&#x2F;userguide&#x2F;retrieving-secrets.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.secretsmanager.secrets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id
FROM aws.secretsmanager.secrets
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Description": "{{ Description }}",
 "KmsKeyId": "{{ KmsKeyId }}",
 "SecretString": "{{ SecretString }}",
 "GenerateSecretString": {
  "ExcludeUppercase": "{{ ExcludeUppercase }}",
  "RequireEachIncludedType": "{{ RequireEachIncludedType }}",
  "IncludeSpace": "{{ IncludeSpace }}",
  "ExcludeCharacters": "{{ ExcludeCharacters }}",
  "GenerateStringKey": "{{ GenerateStringKey }}",
  "PasswordLength": "{{ PasswordLength }}",
  "ExcludePunctuation": "{{ ExcludePunctuation }}",
  "ExcludeLowercase": "{{ ExcludeLowercase }}",
  "SecretStringTemplate": "{{ SecretStringTemplate }}",
  "ExcludeNumbers": "{{ ExcludeNumbers }}"
 },
 "ReplicaRegions": [
  {
   "KmsKeyId": "{{ KmsKeyId }}",
   "Region": "{{ Region }}"
  }
 ],
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "Name": "{{ Name }}"
}
>>>
--required properties only
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
{{ Description }},
 {{ KmsKeyId }},
 {{ SecretString }},
 {{ GenerateSecretString }},
 {{ ReplicaRegions }},
 {{ Tags }},
 {{ Name }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Description": "{{ Description }}",
 "KmsKeyId": "{{ KmsKeyId }}",
 "SecretString": "{{ SecretString }}",
 "GenerateSecretString": {
  "ExcludeUppercase": "{{ ExcludeUppercase }}",
  "RequireEachIncludedType": "{{ RequireEachIncludedType }}",
  "IncludeSpace": "{{ IncludeSpace }}",
  "ExcludeCharacters": "{{ ExcludeCharacters }}",
  "GenerateStringKey": "{{ GenerateStringKey }}",
  "PasswordLength": "{{ PasswordLength }}",
  "ExcludePunctuation": "{{ ExcludePunctuation }}",
  "ExcludeLowercase": "{{ ExcludeLowercase }}",
  "SecretStringTemplate": "{{ SecretStringTemplate }}",
  "ExcludeNumbers": "{{ ExcludeNumbers }}"
 },
 "ReplicaRegions": [
  {
   "KmsKeyId": "{{ KmsKeyId }}",
   "Region": "{{ Region }}"
  }
 ],
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "Name": "{{ Name }}"
}
>>>
--all properties
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
 {{ Description }},
 {{ KmsKeyId }},
 {{ SecretString }},
 {{ GenerateSecretString }},
 {{ ReplicaRegions }},
 {{ Tags }},
 {{ Name }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

