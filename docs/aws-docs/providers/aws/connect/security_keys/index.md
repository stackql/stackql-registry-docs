---
title: security_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - security_keys
  - connect
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

Creates, updates, deletes or gets a <code>security_key</code> resource or lists <code>security_keys</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::SecurityKey</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.security_keys" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="key" /></td><td><code>string</code></td><td>A valid security key in PEM format.</td></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>string</code></td><td>Amazon Connect instance identifier</td></tr>
<tr><td><CopyableCode code="association_id" /></td><td><code>string</code></td><td>An associationID is automatically generated when a storage config is associated with an instance</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securitykey.html"><code>AWS::Connect::SecurityKey</code></a>.

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
    <td><CopyableCode code="Key, InstanceId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>security_keys</code> in a region.
```sql
SELECT
region,
key,
instance_id,
association_id
FROM aws.connect.security_keys
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>security_key</code>.
```sql
SELECT
region,
key,
instance_id,
association_id
FROM aws.connect.security_keys
WHERE region = 'us-east-1' AND data__Identifier = '<InstanceId>|<AssociationId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_key</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.connect.security_keys (
 Key,
 InstanceId,
 region
)
SELECT 
'{{ Key }}',
 '{{ InstanceId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connect.security_keys (
 Key,
 InstanceId,
 region
)
SELECT 
 '{{ Key }}',
 '{{ InstanceId }}',
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
  - name: security_key
    props:
      - name: Key
        value: '{{ Key }}'
      - name: InstanceId
        value: '{{ InstanceId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.connect.security_keys
WHERE data__Identifier = '<InstanceId|AssociationId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>security_keys</code> resource, the following permissions are required:

### Create
```json
connect:AssociateSecurityKey
```

### Read
```json
connect:ListSecurityKeys
```

### Delete
```json
connect:DisassociateSecurityKey
```

### List
```json
connect:ListSecurityKeys
```
