---
title: agreements
hide_title: false
hide_table_of_contents: false
keywords:
  - agreements
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


Used to retrieve a list of <code>agreements</code> in a region or to create or delete a <code>agreements</code> resource, use <code>agreement</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agreements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Transfer::Agreement</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.agreements" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="agreement_id" /></td><td><code>string</code></td><td>A unique identifier for the agreement.</td></tr>
<tr><td><CopyableCode code="server_id" /></td><td><code>string</code></td><td>A unique identifier for the server.</td></tr>
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
agreement_id,
server_id
FROM aws.transfer.agreements
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>agreement</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- agreement.iql (required properties only)
INSERT INTO aws.transfer.agreements (
 ServerId,
 LocalProfileId,
 PartnerProfileId,
 BaseDirectory,
 AccessRole,
 region
)
SELECT 
'{{ ServerId }}',
 '{{ LocalProfileId }}',
 '{{ PartnerProfileId }}',
 '{{ BaseDirectory }}',
 '{{ AccessRole }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- agreement.iql (all properties)
INSERT INTO aws.transfer.agreements (
 Description,
 ServerId,
 LocalProfileId,
 PartnerProfileId,
 BaseDirectory,
 AccessRole,
 Status,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ ServerId }}',
 '{{ LocalProfileId }}',
 '{{ PartnerProfileId }}',
 '{{ BaseDirectory }}',
 '{{ AccessRole }}',
 '{{ Status }}',
 '{{ Tags }}',
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
  - name: agreement
    props:
      - name: Description
        value: '{{ Description }}'
      - name: ServerId
        value: '{{ ServerId }}'
      - name: LocalProfileId
        value: '{{ LocalProfileId }}'
      - name: PartnerProfileId
        value: '{{ PartnerProfileId }}'
      - name: BaseDirectory
        value: '{{ BaseDirectory }}'
      - name: AccessRole
        value: '{{ AccessRole }}'
      - name: Status
        value: '{{ Status }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.transfer.agreements
WHERE data__Identifier = '<AgreementId|ServerId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>agreements</code> resource, the following permissions are required:

### Create
```json
transfer:CreateAgreement,
transfer:TagResource,
iam:PassRole
```

### Delete
```json
transfer:DeleteAgreement
```

### List
```json
transfer:ListAgreements
```

