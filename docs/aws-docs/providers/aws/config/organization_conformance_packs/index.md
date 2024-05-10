---
title: organization_conformance_packs
hide_title: false
hide_table_of_contents: false
keywords:
  - organization_conformance_packs
  - config
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


Used to retrieve a list of <code>organization_conformance_packs</code> in a region or to create or delete a <code>organization_conformance_packs</code> resource, use <code>organization_conformance_pack</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organization_conformance_packs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Config::OrganizationConformancePack.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.config.organization_conformance_packs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="organization_conformance_pack_name" /></td><td><code>string</code></td><td>The name of the organization conformance pack.</td></tr>
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
organization_conformance_pack_name
FROM aws.config.organization_conformance_packs
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>organization_conformance_pack</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- organization_conformance_pack.iql (required properties only)
INSERT INTO aws.config.organization_conformance_packs (
 OrganizationConformancePackName,
 region
)
SELECT 
'{{ OrganizationConformancePackName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- organization_conformance_pack.iql (all properties)
INSERT INTO aws.config.organization_conformance_packs (
 OrganizationConformancePackName,
 TemplateS3Uri,
 TemplateBody,
 DeliveryS3Bucket,
 DeliveryS3KeyPrefix,
 ConformancePackInputParameters,
 ExcludedAccounts,
 region
)
SELECT 
 '{{ OrganizationConformancePackName }}',
 '{{ TemplateS3Uri }}',
 '{{ TemplateBody }}',
 '{{ DeliveryS3Bucket }}',
 '{{ DeliveryS3KeyPrefix }}',
 '{{ ConformancePackInputParameters }}',
 '{{ ExcludedAccounts }}',
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
  - name: organization_conformance_pack
    props:
      - name: OrganizationConformancePackName
        value: '{{ OrganizationConformancePackName }}'
      - name: TemplateS3Uri
        value: '{{ TemplateS3Uri }}'
      - name: TemplateBody
        value: '{{ TemplateBody }}'
      - name: DeliveryS3Bucket
        value: '{{ DeliveryS3Bucket }}'
      - name: DeliveryS3KeyPrefix
        value: '{{ DeliveryS3KeyPrefix }}'
      - name: ConformancePackInputParameters
        value:
          - ParameterName: '{{ ParameterName }}'
            ParameterValue: '{{ ParameterValue }}'
      - name: ExcludedAccounts
        value:
          - '{{ ExcludedAccounts[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.config.organization_conformance_packs
WHERE data__Identifier = '<OrganizationConformancePackName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>organization_conformance_packs</code> resource, the following permissions are required:

### Create
```json
config:PutOrganizationConformancePack,
config:DescribeOrganizationConformancePackStatuses,
config:GetOrganizationConformancePackDetailedStatus,
config:DescribeOrganizationConformancePacks,
s3:GetObject,
s3:GetBucketAcl,
iam:CreateServiceLinkedRole,
iam:PassRole,
organizations:ListDelegatedAdministrators,
organizations:EnableAWSServiceAccess
```

### Delete
```json
config:DeleteOrganizationConformancePack,
config:DescribeOrganizationConformancePackStatuses,
config:GetOrganizationConformancePackDetailedStatus,
organizations:ListDelegatedAdministrators
```

### List
```json
config:DescribeOrganizationConformancePacks
```

