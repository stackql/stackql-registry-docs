---
title: id_namespace_association_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - id_namespace_association_tags
  - cleanrooms
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

Expands all tag keys and values for <code>id_namespace_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>id_namespace_association_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents an association between an ID namespace and a collaboration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cleanrooms.id_namespace_association_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id_namespace_association_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="membership_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="membership_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collaboration_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collaboration_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="input_reference_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id_mapping_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="input_reference_properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>id_namespace_associations</code> in a region.
```sql
SELECT
region,
id_namespace_association_identifier,
arn,
membership_identifier,
membership_arn,
collaboration_identifier,
collaboration_arn,
input_reference_config,
name,
description,
id_mapping_config,
input_reference_properties,
tag_key,
tag_value
FROM aws.cleanrooms.id_namespace_association_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>id_namespace_association_tags</code> resource, see <a href="/providers/aws/cleanrooms/id_namespace_associations/#permissions"><code>id_namespace_associations</code></a>

