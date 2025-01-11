---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - datazone
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

Creates, updates, deletes or gets a <code>domain</code> resource or lists <code>domains</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A domain is an organizing entity for connecting together assets, users, and their projects</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.domains" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the Amazon DataZone domain.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The timestamp of when the Amazon DataZone domain was last updated.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the Amazon DataZone domain.</td></tr>
<tr><td><CopyableCode code="domain_execution_role" /></td><td><code>string</code></td><td>The domain execution role that is created when an Amazon DataZone domain is created. The domain execution role is created in the AWS account that houses the Amazon DataZone domain.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The id of the Amazon DataZone domain.</td></tr>
<tr><td><CopyableCode code="kms_key_identifier" /></td><td><code>string</code></td><td>The identifier of the AWS Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data.</td></tr>
<tr><td><CopyableCode code="last_updated_at" /></td><td><code>string</code></td><td>The timestamp of when the Amazon DataZone domain was last updated.</td></tr>
<tr><td><CopyableCode code="managed_account_id" /></td><td><code>string</code></td><td>The identifier of the AWS account that manages the domain.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the Amazon DataZone domain.</td></tr>
<tr><td><CopyableCode code="portal_url" /></td><td><code>string</code></td><td>The URL of the data portal for this Amazon DataZone domain.</td></tr>
<tr><td><CopyableCode code="single_sign_on" /></td><td><code>object</code></td><td>The single-sign on configuration of the Amazon DataZone domain.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the Amazon DataZone domain.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags specified for the Amazon DataZone domain.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domain.html"><code>AWS::DataZone::Domain</code></a>.

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
    <td><CopyableCode code="DomainExecutionRole, Name, region" /></td>
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
Gets all <code>domains</code> in a region.
```sql
SELECT
region,
arn,
created_at,
description,
domain_execution_role,
id,
kms_key_identifier,
last_updated_at,
managed_account_id,
name,
portal_url,
single_sign_on,
status,
tags
FROM aws.datazone.domains
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>domain</code>.
```sql
SELECT
region,
arn,
created_at,
description,
domain_execution_role,
id,
kms_key_identifier,
last_updated_at,
managed_account_id,
name,
portal_url,
single_sign_on,
status,
tags
FROM aws.datazone.domains
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>domain</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.datazone.domains (
 DomainExecutionRole,
 Name,
 region
)
SELECT 
'{{ DomainExecutionRole }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.datazone.domains (
 Description,
 DomainExecutionRole,
 KmsKeyIdentifier,
 Name,
 SingleSignOn,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ DomainExecutionRole }}',
 '{{ KmsKeyIdentifier }}',
 '{{ Name }}',
 '{{ SingleSignOn }}',
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
  - name: domain
    props:
      - name: Description
        value: '{{ Description }}'
      - name: DomainExecutionRole
        value: '{{ DomainExecutionRole }}'
      - name: KmsKeyIdentifier
        value: '{{ KmsKeyIdentifier }}'
      - name: Name
        value: '{{ Name }}'
      - name: SingleSignOn
        value:
          Type: '{{ Type }}'
          UserAssignment: '{{ UserAssignment }}'
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
DELETE FROM aws.datazone.domains
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>domains</code> resource, the following permissions are required:

### Create
```json
datazone:CreateDomain,
datazone:UpdateDomain,
datazone:GetDomain,
datazone:TagResource,
sso:CreateManagedApplicationInstance,
sso:DeleteManagedApplicationInstance,
sso:PutApplicationAssignmentConfiguration,
sso:ListInstances,
iam:PassRole
```

### Read
```json
datazone:GetDomain
```

### Update
```json
datazone:UpdateDomain,
datazone:GetDomain,
datazone:TagResource,
datazone:UntagResource,
sso:CreateManagedApplicationInstance,
sso:DeleteManagedApplicationInstance,
sso:PutApplicationAssignmentConfiguration,
sso:ListInstances,
iam:PassRole
```

### Delete
```json
datazone:DeleteDomain,
datazone:GetDomain,
sso:DeleteManagedApplicationInstance,
sso:PutApplicationAssignmentConfiguration,
sso:ListInstances
```

### List
```json
datazone:ListDomains
```
