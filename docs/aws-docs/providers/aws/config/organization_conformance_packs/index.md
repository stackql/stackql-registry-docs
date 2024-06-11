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

Creates, updates, deletes or gets an <code>organization_conformance_pack</code> resource or lists <code>organization_conformance_packs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organization_conformance_packs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Config::OrganizationConformancePack.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.config.organization_conformance_packs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="organization_conformance_pack_name" /></td><td><code>string</code></td><td>The name of the organization conformance pack.</td></tr>
<tr><td><CopyableCode code="template_s3_uri" /></td><td><code>string</code></td><td>Location of file containing the template body.</td></tr>
<tr><td><CopyableCode code="template_body" /></td><td><code>string</code></td><td>A string containing full conformance pack template body.</td></tr>
<tr><td><CopyableCode code="delivery_s3_bucket" /></td><td><code>string</code></td><td>AWS Config stores intermediate files while processing conformance pack template.</td></tr>
<tr><td><CopyableCode code="delivery_s3_key_prefix" /></td><td><code>string</code></td><td>The prefix for the delivery S3 bucket.</td></tr>
<tr><td><CopyableCode code="conformance_pack_input_parameters" /></td><td><code>array</code></td><td>A list of ConformancePackInputParameter objects.</td></tr>
<tr><td><CopyableCode code="excluded_accounts" /></td><td><code>array</code></td><td>A list of AWS accounts to be excluded from an organization conformance pack while deploying a conformance pack.</td></tr>
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
    <td><CopyableCode code="OrganizationConformancePackName, region" /></td>
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
List all <code>organization_conformance_packs</code> in a region.
```sql
SELECT
region,
organization_conformance_pack_name
FROM aws.config.organization_conformance_packs
WHERE region = 'us-east-1';
```
Gets all properties from an <code>organization_conformance_pack</code>.
```sql
SELECT
region,
organization_conformance_pack_name,
template_s3_uri,
template_body,
delivery_s3_bucket,
delivery_s3_key_prefix,
conformance_pack_input_parameters,
excluded_accounts
FROM aws.config.organization_conformance_packs
WHERE region = 'us-east-1' AND data__Identifier = '<OrganizationConformancePackName>';
```


## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
config:DescribeOrganizationConformancePacks
```

### Delete
```json
config:DeleteOrganizationConformancePack,
config:DescribeOrganizationConformancePackStatuses,
config:GetOrganizationConformancePackDetailedStatus,
organizations:ListDelegatedAdministrators
```

### Update
```json
config:PutOrganizationConformancePack,
config:DescribeOrganizationConformancePackStatuses,
config:GetOrganizationConformancePackDetailedStatus,
s3:GetObject,
s3:GetBucketAcl,
iam:CreateServiceLinkedRole,
iam:PassRole,
organizations:ListDelegatedAdministrators,
organizations:EnableAWSServiceAccess
```

### List
```json
config:DescribeOrganizationConformancePacks
```

