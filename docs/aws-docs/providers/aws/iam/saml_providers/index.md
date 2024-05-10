---
title: saml_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - saml_providers
  - iam
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


Used to retrieve a list of <code>saml_providers</code> in a region or to create or delete a <code>saml_providers</code> resource, use <code>saml_provider</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>saml_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IAM::SAMLProvider</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.saml_providers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the SAML provider</td></tr>
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
arn
FROM aws.iam.saml_providers
;
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
 "SamlMetadataDocument": "{{ SamlMetadataDocument }}"
}
>>>
--required properties only
INSERT INTO aws.iam.saml_providers (
 SamlMetadataDocument,
 region
)
SELECT 
{{ .SamlMetadataDocument }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "SamlMetadataDocument": "{{ SamlMetadataDocument }}",
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.iam.saml_providers (
 Name,
 SamlMetadataDocument,
 Tags,
 region
)
SELECT 
 {{ .Name }},
 {{ .SamlMetadataDocument }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iam.saml_providers
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>saml_providers</code> resource, the following permissions are required:

### Create
```json
iam:CreateSAMLProvider,
iam:GetSAMLProvider,
iam:TagSAMLProvider
```

### Delete
```json
iam:DeleteSAMLProvider
```

### List
```json
iam:ListSAMLProviders,
iam:GetSAMLProvider
```

