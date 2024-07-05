---
title: resource_default_versions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_default_versions_list_only
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

Lists <code>resource_default_versions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/resource_default_versions/"><code>resource_default_versions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_default_versions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The default version of a resource that has been registered in the CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.resource_default_versions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="version_id" /></td><td><code>string</code></td><td>The ID of an existing version of the resource to set as the default.</td></tr>
<tr><td><CopyableCode code="type_name" /></td><td><code>string</code></td><td>The name of the type being registered.<br />We recommend that type names adhere to the following pattern: company_or_organization::service::type.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type. This is used to uniquely identify a ResourceDefaultVersion</td></tr>
<tr><td><CopyableCode code="type_version_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type version.</td></tr>
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
Lists all <code>resource_default_versions</code> in a region.
```sql
SELECT
region,
arn
FROM aws.cloudformation.resource_default_versions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>resource_default_versions_list_only</code> resource, see <a href="/providers/aws/cloudformation/resource_default_versions/#permissions"><code>resource_default_versions</code></a>


