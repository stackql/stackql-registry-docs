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

Creates, updates, deletes or gets a <code>conformance_pack</code> resource or lists <code>conformance_packs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>conformance_packs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A conformance pack is a collection of AWS Config rules and remediation actions that can be easily deployed as a single entity in an account and a region or across an entire AWS Organization.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.config.conformance_packs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="conformance_pack_name" /></td><td><code>string</code></td><td>Name of the conformance pack which will be assigned as the unique identifier.</td></tr>
<tr><td><CopyableCode code="delivery_s3_bucket" /></td><td><code>string</code></td><td>AWS Config stores intermediate files while processing conformance pack template.</td></tr>
<tr><td><CopyableCode code="delivery_s3_key_prefix" /></td><td><code>string</code></td><td>The prefix for delivery S3 bucket.</td></tr>
<tr><td><CopyableCode code="template_body" /></td><td><code>string</code></td><td>A string containing full conformance pack template body. You can only specify one of the template body or template S3Uri fields.</td></tr>
<tr><td><CopyableCode code="template_s3_uri" /></td><td><code>string</code></td><td>Location of file containing the template body which points to the conformance pack template that is located in an Amazon S3 bucket. You can only specify one of the template body or template S3Uri fields.</td></tr>
<tr><td><CopyableCode code="template_ssm_document_details" /></td><td><code>object</code></td><td>The TemplateSSMDocumentDetails object contains the name of the SSM document and the version of the SSM document.</td></tr>
<tr><td><CopyableCode code="conformance_pack_input_parameters" /></td><td><code>array</code></td><td>A list of ConformancePackInputParameter objects.</td></tr>
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
    <td><CopyableCode code="ConformancePackName, region" /></td>
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
List all <code>conformance_packs</code> in a region.
```sql
SELECT
region,
conformance_pack_name
FROM aws.config.conformance_packs
WHERE region = 'us-east-1';
```
Gets all properties from a <code>conformance_pack</code>.
```sql
SELECT
region,
conformance_pack_name,
delivery_s3_bucket,
delivery_s3_key_prefix,
template_body,
template_s3_uri,
template_ssm_document_details,
conformance_pack_input_parameters
FROM aws.config.conformance_packs
WHERE region = 'us-east-1' AND data__Identifier = '<ConformancePackName>';
```


## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
config:DescribeConformancePacks
```

### Update
```json
config:PutConformancePack,
config:DescribeConformancePackStatus,
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

