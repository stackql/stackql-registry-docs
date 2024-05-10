---
title: connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors
  - transfer
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


Used to retrieve a list of <code>connectors</code> in a region or to create or delete a <code>connectors</code> resource, use <code>connector</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Transfer::Connector</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.connectors" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="connector_id" /></td><td><code>string</code></td><td>A unique identifier for the connector.</td></tr>
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
connector_id
FROM aws.transfer.connectors
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
 "AccessRole": "{{ AccessRole }}",
 "Url": "{{ Url }}"
}
>>>
--required properties only
INSERT INTO aws.transfer.connectors (
 AccessRole,
 Url,
 region
)
SELECT 
{{ .AccessRole }},
 {{ .Url }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AccessRole": "{{ AccessRole }}",
 "As2Config": {
  "LocalProfileId": "{{ LocalProfileId }}",
  "PartnerProfileId": "{{ PartnerProfileId }}",
  "MessageSubject": "{{ MessageSubject }}",
  "Compression": "{{ Compression }}",
  "EncryptionAlgorithm": "{{ EncryptionAlgorithm }}",
  "SigningAlgorithm": "{{ SigningAlgorithm }}",
  "MdnSigningAlgorithm": "{{ MdnSigningAlgorithm }}",
  "MdnResponse": "{{ MdnResponse }}",
  "BasicAuthSecretId": "{{ BasicAuthSecretId }}"
 },
 "SftpConfig": {
  "UserSecretId": "{{ UserSecretId }}",
  "TrustedHostKeys": [
   "{{ TrustedHostKeys[0] }}"
  ]
 },
 "LoggingRole": "{{ LoggingRole }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "Url": "{{ Url }}"
}
>>>
--all properties
INSERT INTO aws.transfer.connectors (
 AccessRole,
 As2Config,
 SftpConfig,
 LoggingRole,
 Tags,
 Url,
 region
)
SELECT 
 {{ .AccessRole }},
 {{ .As2Config }},
 {{ .SftpConfig }},
 {{ .LoggingRole }},
 {{ .Tags }},
 {{ .Url }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.transfer.connectors
WHERE data__Identifier = '<ConnectorId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>connectors</code> resource, the following permissions are required:

### Create
```json
transfer:CreateConnector,
transfer:TagResource,
iam:PassRole
```

### Delete
```json
transfer:DeleteConnector
```

### List
```json
transfer:ListConnectors
```

