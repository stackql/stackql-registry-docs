---
title: domain_name_api_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_name_api_associations
  - appsync
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

Creates, updates, deletes or gets a <code>domain_name_api_association</code> resource or lists <code>domain_name_api_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_name_api_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppSync::DomainNameApiAssociation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appsync.domain_name_api_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="api_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="api_association_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainnameapiassociation.html"><code>AWS::AppSync::DomainNameApiAssociation</code></a>.

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
    <td><CopyableCode code="DomainName, ApiId, region" /></td>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from an individual <code>domain_name_api_association</code>.
```sql
SELECT
region,
domain_name,
api_id,
api_association_identifier
FROM aws.appsync.domain_name_api_associations
WHERE region = 'us-east-1' AND data__Identifier = '<ApiAssociationIdentifier>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>domain_name_api_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.appsync.domain_name_api_associations (
 DomainName,
 ApiId,
 region
)
SELECT 
'{{ DomainName }}',
 '{{ ApiId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.appsync.domain_name_api_associations (
 DomainName,
 ApiId,
 region
)
SELECT 
 '{{ DomainName }}',
 '{{ ApiId }}',
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
  - name: domain_name_api_association
    props:
      - name: DomainName
        value: '{{ DomainName }}'
      - name: ApiId
        value: '{{ ApiId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.appsync.domain_name_api_associations
WHERE data__Identifier = '<ApiAssociationIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>domain_name_api_associations</code> resource, the following permissions are required:

### Create
```json
appsync:AssociateApi,
appsync:GetApiAssociation
```

### Delete
```json
appsync:DisassociateApi,
appsync:GetApiAssociation
```

### Update
```json
appsync:AssociateApi,
appsync:GetApiAssociation
```

### Read
```json
appsync:GetApiAssociation
```
