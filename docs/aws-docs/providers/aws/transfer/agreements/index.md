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

Creates, updates, deletes or gets an <code>agreement</code> resource or lists <code>agreements</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agreements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Transfer::Agreement</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.agreements" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A textual description for the agreement.</td></tr>
<tr><td><CopyableCode code="server_id" /></td><td><code>string</code></td><td>A unique identifier for the server.</td></tr>
<tr><td><CopyableCode code="local_profile_id" /></td><td><code>string</code></td><td>A unique identifier for the local profile.</td></tr>
<tr><td><CopyableCode code="partner_profile_id" /></td><td><code>string</code></td><td>A unique identifier for the partner profile.</td></tr>
<tr><td><CopyableCode code="base_directory" /></td><td><code>string</code></td><td>Specifies the base directory for the agreement.</td></tr>
<tr><td><CopyableCode code="access_role" /></td><td><code>string</code></td><td>Specifies the access role for the agreement.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Specifies the status of the agreement.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Key-value pairs that can be used to group and search for agreements. Tags are metadata attached to agreements for any purpose.</td></tr>
<tr><td><CopyableCode code="agreement_id" /></td><td><code>string</code></td><td>A unique identifier for the agreement.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Specifies the unique Amazon Resource Name (ARN) for the agreement.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html"><code>AWS::Transfer::Agreement</code></a>.

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
    <td><CopyableCode code="ServerId, LocalProfileId, PartnerProfileId, BaseDirectory, AccessRole, region" /></td>
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
Gets all <code>agreements</code> in a region.
```sql
SELECT
region,
description,
server_id,
local_profile_id,
partner_profile_id,
base_directory,
access_role,
status,
tags,
agreement_id,
arn
FROM aws.transfer.agreements
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>agreement</code>.
```sql
SELECT
region,
description,
server_id,
local_profile_id,
partner_profile_id,
base_directory,
access_role,
status,
tags,
agreement_id,
arn
FROM aws.transfer.agreements
WHERE region = 'us-east-1' AND data__Identifier = '<AgreementId>|<ServerId>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
transfer:DescribeAgreement
```

### Update
```json
transfer:UpdateAgreement,
transfer:UnTagResource,
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
