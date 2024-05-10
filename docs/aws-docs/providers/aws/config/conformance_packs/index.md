---
title: conformance_packs
hide_title: false
hide_table_of_contents: false
keywords:
  - conformance_packs
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


Used to retrieve a list of <code>conformance_packs</code> in a region or to create or delete a <code>conformance_packs</code> resource, use <code>conformance_pack</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>conformance_packs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A conformance pack is a collection of AWS Config rules and remediation actions that can be easily deployed as a single entity in an account and a region or across an entire AWS Organization.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.config.conformance_packs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="conformance_pack_name" /></td><td><code>string</code></td><td>Name of the conformance pack which will be assigned as the unique identifier.</td></tr>
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
conformance_pack_name
FROM aws.config.conformance_packs
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>conformance_pack</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- conformance_pack.iql (required properties only)
INSERT INTO aws.config.conformance_packs (
 ConformancePackName,
 region
)
SELECT 
'{{ ConformancePackName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- conformance_pack.iql (all properties)
INSERT INTO aws.config.conformance_packs (
 ConformancePackName,
 DeliveryS3Bucket,
 DeliveryS3KeyPrefix,
 TemplateBody,
 TemplateS3Uri,
 TemplateSSMDocumentDetails,
 ConformancePackInputParameters,
 region
)
SELECT 
 '{{ ConformancePackName }}',
 '{{ DeliveryS3Bucket }}',
 '{{ DeliveryS3KeyPrefix }}',
 '{{ TemplateBody }}',
 '{{ TemplateS3Uri }}',
 '{{ TemplateSSMDocumentDetails }}',
 '{{ ConformancePackInputParameters }}',
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
  - name: conformance_pack
    props:
      - name: ConformancePackName
        value: '{{ ConformancePackName }}'
      - name: DeliveryS3Bucket
        value: '{{ DeliveryS3Bucket }}'
      - name: DeliveryS3KeyPrefix
        value: '{{ DeliveryS3KeyPrefix }}'
      - name: TemplateBody
        value: '{{ TemplateBody }}'
      - name: TemplateS3Uri
        value: '{{ TemplateS3Uri }}'
      - name: TemplateSSMDocumentDetails
        value:
          DocumentName: '{{ DocumentName }}'
          DocumentVersion: '{{ DocumentVersion }}'
      - name: ConformancePackInputParameters
        value:
          - ParameterName: '{{ ParameterName }}'
            ParameterValue: '{{ ParameterValue }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.config.conformance_packs
WHERE data__Identifier = '<ConformancePackName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>conformance_packs</code> resource, the following permissions are required:

### Create
```json
config:PutConformancePack,
config:DescribeConformancePackStatus,
config:DescribeConformancePacks,
s3:GetObject,
s3:GetBucketAcl,
iam:CreateServiceLinkedRole,
iam:PassRole
```

### Delete
```json
config:DeleteConformancePack,
config:DescribeConformancePackStatus
```

### List
```json
config:DescribeConformancePacks
```

