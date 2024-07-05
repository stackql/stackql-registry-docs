---
title: public_type_versions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - public_type_versions_list_only
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>public_type_versions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/public_type_versions/"><code>public_type_versions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>public_type_versions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Test and Publish a resource that has been registered in the CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.public_type_versions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of the extension.</td></tr>
<tr><td><CopyableCode code="type_version_arn" /></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of the extension with the versionId.</td></tr>
<tr><td><CopyableCode code="public_version_number" /></td><td><code>string</code></td><td>The version number of a public third-party extension</td></tr>
<tr><td><CopyableCode code="publisher_id" /></td><td><code>string</code></td><td>The publisher id assigned by CloudFormation for publishing in this region.</td></tr>
<tr><td><CopyableCode code="public_type_arn" /></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) assigned to the public extension upon publication</td></tr>
<tr><td><CopyableCode code="type_name" /></td><td><code>string</code></td><td>The name of the type being registered.<br />We recommend that type names adhere to the following pattern: company_or_organization::service::type.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>public_type_versions</code> in a region.
```sql
SELECT
region,
public_type_arn
FROM aws.cloudformation.public_type_versions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>public_type_versions_list_only</code> resource, see <a href="/providers/aws/cloudformation/public_type_versions/#permissions"><code>public_type_versions</code></a>


