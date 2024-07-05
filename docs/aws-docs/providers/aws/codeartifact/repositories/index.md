---
title: repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - repositories
  - codeartifact
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

Creates, updates, deletes or gets a <code>repository</code> resource or lists <code>repositories</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The resource schema to create a CodeArtifact repository.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codeartifact.repositories" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="repository_name" /></td><td><code>string</code></td><td>The name of the repository.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the repository. This is used for GetAtt</td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The name of the domain that contains the repository.</td></tr>
<tr><td><CopyableCode code="domain_owner" /></td><td><code>string</code></td><td>The 12-digit account ID of the AWS account that owns the domain.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A text description of the repository.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the repository.</td></tr>
<tr><td><CopyableCode code="external_connections" /></td><td><code>array</code></td><td>A list of external connections associated with the repository.</td></tr>
<tr><td><CopyableCode code="upstreams" /></td><td><code>array</code></td><td>A list of upstream repositories associated with the repository.</td></tr>
<tr><td><CopyableCode code="permissions_policy_document" /></td><td><code>object</code></td><td>The access control resource policy on the provided repository.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="RepositoryName, DomainName, region" /></td>
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
Gets all <code>repositories</code> in a region.
```sql
SELECT
region,
repository_name,
name,
domain_name,
domain_owner,
description,
arn,
external_connections,
upstreams,
permissions_policy_document,
tags
FROM aws.codeartifact.repositories
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>repository</code>.
```sql
SELECT
region,
repository_name,
name,
domain_name,
domain_owner,
description,
arn,
external_connections,
upstreams,
permissions_policy_document,
tags
FROM aws.codeartifact.repositories
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>repository</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.codeartifact.repositories (
 RepositoryName,
 DomainName,
 region
)
SELECT 
'{{ RepositoryName }}',
 '{{ DomainName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.codeartifact.repositories (
 RepositoryName,
 DomainName,
 Description,
 ExternalConnections,
 Upstreams,
 PermissionsPolicyDocument,
 Tags,
 region
)
SELECT 
 '{{ RepositoryName }}',
 '{{ DomainName }}',
 '{{ Description }}',
 '{{ ExternalConnections }}',
 '{{ Upstreams }}',
 '{{ PermissionsPolicyDocument }}',
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
  - name: repository
    props:
      - name: RepositoryName
        value: '{{ RepositoryName }}'
      - name: DomainName
        value: '{{ DomainName }}'
      - name: Description
        value: '{{ Description }}'
      - name: ExternalConnections
        value:
          - '{{ ExternalConnections[0] }}'
      - name: Upstreams
        value:
          - '{{ Upstreams[0] }}'
      - name: PermissionsPolicyDocument
        value: {}
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
DELETE FROM aws.codeartifact.repositories
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>repositories</code> resource, the following permissions are required:

### Create
```json
codeartifact:CreateRepository,
codeartifact:DescribeRepository,
codeartifact:PutRepositoryPermissionsPolicy,
codeartifact:AssociateExternalConnection,
codeartifact:AssociateWithDownstreamRepository,
codeartifact:TagResource
```

### Read
```json
codeartifact:DescribeRepository,
codeartifact:GetRepositoryPermissionsPolicy,
codeartifact:ListTagsForResource
```

### Update
```json
codeartifact:PutRepositoryPermissionsPolicy,
codeartifact:DeleteRepositoryPermissionsPolicy,
codeartifact:AssociateExternalConnection,
codeartifact:DisassociateExternalConnection,
codeartifact:UpdateRepository,
codeartifact:DescribeRepository,
codeartifact:AssociateWithDownstreamRepository,
codeartifact:TagResource,
codeartifact:UntagResource
```

### Delete
```json
codeartifact:DeleteRepository,
codeartifact:DescribeRepository
```

### List
```json
codeartifact:ListRepositories
```

