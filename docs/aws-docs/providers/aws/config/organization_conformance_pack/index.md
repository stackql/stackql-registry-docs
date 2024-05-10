---
title: organization_conformance_pack
hide_title: false
hide_table_of_contents: false
keywords:
  - organization_conformance_pack
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


Gets or updates an individual <code>organization_conformance_pack</code> resource, use <code>organization_conformance_packs</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organization_conformance_pack</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Config::OrganizationConformancePack.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.config.organization_conformance_pack" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="organization_conformance_pack_name" /></td><td><code>string</code></td><td>The name of the organization conformance pack.</td></tr>
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

## `SELECT` Example
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
FROM aws.config.organization_conformance_pack
WHERE region = 'us-east-1' AND data__Identifier = '<OrganizationConformancePackName>';
```


## Permissions

To operate on the <code>organization_conformance_pack</code> resource, the following permissions are required:

### Read
```json
config:DescribeOrganizationConformancePacks
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

