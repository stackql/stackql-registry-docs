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

Creates, updates, deletes or gets a <code>connector</code> resource or lists <code>connectors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Transfer::Connector</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.connectors" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="access_role" /></td><td><code>string</code></td><td>Specifies the access role for the connector.</td></tr>
<tr><td><CopyableCode code="as2_config" /></td><td><code>object</code></td><td>Configuration for an AS2 connector.</td></tr>
<tr><td><CopyableCode code="sftp_config" /></td><td><code>object</code></td><td>Configuration for an SFTP connector.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Specifies the unique Amazon Resource Name (ARN) for the connector.</td></tr>
<tr><td><CopyableCode code="connector_id" /></td><td><code>string</code></td><td>A unique identifier for the connector.</td></tr>
<tr><td><CopyableCode code="logging_role" /></td><td><code>string</code></td><td>Specifies the logging role for the connector.</td></tr>
<tr><td><CopyableCode code="service_managed_egress_ip_addresses" /></td><td><code>array</code></td><td>The list of egress IP addresses of this connector. These IP addresses are assigned automatically when you create the connector.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Key-value pairs that can be used to group and search for connectors. Tags are metadata attached to connectors for any purpose.</td></tr>
<tr><td><CopyableCode code="url" /></td><td><code>string</code></td><td>URL for Connector</td></tr>
<tr><td><CopyableCode code="security_policy_name" /></td><td><code>string</code></td><td>Security policy for SFTP Connector</td></tr>
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
    <td><CopyableCode code="AccessRole, Url, region" /></td>
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
List all <code>connectors</code> in a region.
```sql
SELECT
region,
connector_id
FROM aws.transfer.connectors
WHERE region = 'us-east-1';
```
Gets all properties from a <code>connector</code>.
```sql
SELECT
region,
access_role,
as2_config,
sftp_config,
arn,
connector_id,
logging_role,
service_managed_egress_ip_addresses,
tags,
url,
security_policy_name
FROM aws.transfer.connectors
WHERE region = 'us-east-1' AND data__Identifier = '<ConnectorId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connector</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.transfer.connectors (
 AccessRole,
 Url,
 region
)
SELECT 
'{{ AccessRole }}',
 '{{ Url }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.transfer.connectors (
 AccessRole,
 As2Config,
 SftpConfig,
 LoggingRole,
 Tags,
 Url,
 SecurityPolicyName,
 region
)
SELECT 
 '{{ AccessRole }}',
 '{{ As2Config }}',
 '{{ SftpConfig }}',
 '{{ LoggingRole }}',
 '{{ Tags }}',
 '{{ Url }}',
 '{{ SecurityPolicyName }}',
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
  - name: connector
    props:
      - name: AccessRole
        value: '{{ AccessRole }}'
      - name: As2Config
        value:
          LocalProfileId: '{{ LocalProfileId }}'
          PartnerProfileId: '{{ PartnerProfileId }}'
          MessageSubject: '{{ MessageSubject }}'
          Compression: '{{ Compression }}'
          EncryptionAlgorithm: '{{ EncryptionAlgorithm }}'
          SigningAlgorithm: '{{ SigningAlgorithm }}'
          MdnSigningAlgorithm: '{{ MdnSigningAlgorithm }}'
          MdnResponse: '{{ MdnResponse }}'
          BasicAuthSecretId: '{{ BasicAuthSecretId }}'
      - name: SftpConfig
        value:
          UserSecretId: '{{ UserSecretId }}'
          TrustedHostKeys:
            - '{{ TrustedHostKeys[0] }}'
      - name: LoggingRole
        value: '{{ LoggingRole }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Url
        value: '{{ Url }}'
      - name: SecurityPolicyName
        value: '{{ SecurityPolicyName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
transfer:DescribeConnector
```

### Update
```json
transfer:UpdateConnector,
transfer:UnTagResource,
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

