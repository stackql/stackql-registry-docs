---
title: public_type_version
hide_title: false
hide_table_of_contents: false
keywords:
  - public_type_version
  - cloudformation
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

Gets or operates on an individual <code>public_type_version</code> resource, use <code>public_type_versions</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>public_type_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Test and Publish a resource that has been registered in the CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.public_type_version" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of the extension.</td></tr>
<tr><td><CopyableCode code="type_version_arn" /></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of the extension with the versionId.</td></tr>
<tr><td><CopyableCode code="public_version_number" /></td><td><code>string</code></td><td>The version number of a public third-party extension</td></tr>
<tr><td><CopyableCode code="publisher_id" /></td><td><code>string</code></td><td>The publisher id assigned by CloudFormation for publishing in this region.</td></tr>
<tr><td><CopyableCode code="public_type_arn" /></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) assigned to the public extension upon publication</td></tr>
<tr><td><CopyableCode code="type_name" /></td><td><code>string</code></td><td>The name of the type being registered.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;We recommend that type names adhere to the following pattern: company_or_organization::service::type.</td></tr>
<tr><td><CopyableCode code="log_delivery_bucket" /></td><td><code>string</code></td><td>A url to the S3 bucket where logs for the testType run will be available</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The kind of extension</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
arn,
type_version_arn,
public_version_number,
publisher_id,
public_type_arn,
type_name,
log_delivery_bucket,
type
FROM aws.cloudformation.public_type_version
WHERE data__Identifier = '<PublicTypeArn>';
```

## Permissions

To operate on the <code>public_type_version</code> resource, the following permissions are required:

### Read
```json
cloudformation:DescribeType,
cloudformation:DescribePublisher
```

