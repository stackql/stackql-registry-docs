---
title: package_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - package_groups
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

Creates, updates, deletes or gets a <code>package_group</code> resource or lists <code>package_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>package_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The resource schema to create a CodeArtifact package group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codeartifact.package_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The name of the domain that contains the package group.</td></tr>
<tr><td><CopyableCode code="domain_owner" /></td><td><code>string</code></td><td>The 12-digit account ID of the AWS account that owns the domain.</td></tr>
<tr><td><CopyableCode code="pattern" /></td><td><code>string</code></td><td>The package group pattern that is used to gather packages.</td></tr>
<tr><td><CopyableCode code="contact_info" /></td><td><code>string</code></td><td>The contact info of the package group.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The text description of the package group.</td></tr>
<tr><td><CopyableCode code="origin_configuration" /></td><td><code>object</code></td><td>The package origin configuration of the package group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to the package group.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the package group.</td></tr>
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
    <td><CopyableCode code="Pattern, DomainName, region" /></td>
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
Gets all <code>package_groups</code> in a region.
```sql
SELECT
region,
domain_name,
domain_owner,
pattern,
contact_info,
description,
origin_configuration,
tags,
arn
FROM aws.codeartifact.package_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>package_group</code>.
```sql
SELECT
region,
domain_name,
domain_owner,
pattern,
contact_info,
description,
origin_configuration,
tags,
arn
FROM aws.codeartifact.package_groups
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>package_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.codeartifact.package_groups (
 DomainName,
 Pattern,
 region
)
SELECT 
'{{ DomainName }}',
 '{{ Pattern }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.codeartifact.package_groups (
 DomainName,
 DomainOwner,
 Pattern,
 ContactInfo,
 Description,
 OriginConfiguration,
 Tags,
 region
)
SELECT 
 '{{ DomainName }}',
 '{{ DomainOwner }}',
 '{{ Pattern }}',
 '{{ ContactInfo }}',
 '{{ Description }}',
 '{{ OriginConfiguration }}',
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
  - name: package_group
    props:
      - name: DomainName
        value: '{{ DomainName }}'
      - name: DomainOwner
        value: '{{ DomainOwner }}'
      - name: Pattern
        value: '{{ Pattern }}'
      - name: ContactInfo
        value: '{{ ContactInfo }}'
      - name: Description
        value: '{{ Description }}'
      - name: OriginConfiguration
        value:
          Restrictions:
            Publish:
              RestrictionMode: '{{ RestrictionMode }}'
              Repositories:
                - '{{ Repositories[0] }}'
            ExternalUpstream: null
            InternalUpstream: null
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
DELETE FROM aws.codeartifact.package_groups
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>package_groups</code> resource, the following permissions are required:

### Create
```json
codeartifact:CreatePackageGroup,
codeartifact:DescribePackageGroup,
codeartifact:UpdatePackageGroup,
codeartifact:UpdatePackageGroupOriginConfiguration,
codeartifact:ListAllowedRepositoriesForGroup,
codeartifact:ListTagsForResource,
codeartifact:TagResource
```

### Read
```json
codeartifact:DescribePackageGroup,
codeartifact:ListAllowedRepositoriesForGroup,
codeartifact:ListTagsForResource
```

### Update
```json
codeartifact:UpdatePackageGroup,
codeartifact:UpdatePackageGroupOriginConfiguration,
codeartifact:DescribePackageGroup,
codeartifact:ListAllowedRepositoriesForGroup,
codeartifact:ListTagsForResource,
codeartifact:TagResource,
codeartifact:UntagResource
```

### Delete
```json
codeartifact:DeletePackageGroup,
codeartifact:DescribePackageGroup
```

### List
```json
codeartifact:ListPackageGroups
```

