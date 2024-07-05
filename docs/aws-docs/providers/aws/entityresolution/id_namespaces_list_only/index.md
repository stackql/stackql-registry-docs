---
title: id_namespaces_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - id_namespaces_list_only
  - entityresolution
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

Lists <code>id_namespaces</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/id_namespaces/"><code>id_namespaces</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>id_namespaces_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>IdNamespace defined in AWS Entity Resolution service</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.entityresolution.id_namespaces_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id_namespace_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="input_source_config" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="id_mapping_workflow_properties" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id_namespace_arn" /></td><td><code>string</code></td><td>The arn associated with the IdNamespace</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The date and time when the IdNamespace was created</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The date and time when the IdNamespace was updated</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
Lists all <code>id_namespaces</code> in a region.
```sql
SELECT
region,
id_namespace_name
FROM aws.entityresolution.id_namespaces_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>id_namespaces_list_only</code> resource, see <a href="/providers/aws/entityresolution/id_namespaces/#permissions"><code>id_namespaces</code></a>


