---
title: object_types_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - object_types_list_only
  - customerprofiles
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

Lists <code>object_types</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/object_types/"><code>object_types</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>object_types_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An ObjectType resource of Amazon Connect Customer Profiles</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.object_types_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><CopyableCode code="object_type_name" /></td><td><code>string</code></td><td>The name of the profile object type.</td></tr>
<tr><td><CopyableCode code="allow_profile_creation" /></td><td><code>boolean</code></td><td>Indicates whether a profile should be created when data is received.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the profile object type.</td></tr>
<tr><td><CopyableCode code="encryption_key" /></td><td><code>string</code></td><td>The default encryption key</td></tr>
<tr><td><CopyableCode code="expiration_days" /></td><td><code>integer</code></td><td>The default number of days until the data within the domain expires.</td></tr>
<tr><td><CopyableCode code="fields" /></td><td><code>array</code></td><td>A list of the name and ObjectType field.</td></tr>
<tr><td><CopyableCode code="keys" /></td><td><code>array</code></td><td>A list of unique keys that can be used to map data to the profile.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time of this integration got created.</td></tr>
<tr><td><CopyableCode code="last_updated_at" /></td><td><code>string</code></td><td>The time of this integration got last updated at.</td></tr>
<tr><td><CopyableCode code="source_last_updated_timestamp_format" /></td><td><code>string</code></td><td>The format of your sourceLastUpdatedTimestamp that was previously set up.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags (keys and values) associated with the integration.</td></tr>
<tr><td><CopyableCode code="template_id" /></td><td><code>string</code></td><td>A unique identifier for the object template.</td></tr>
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
Lists all <code>object_types</code> in a region.
```sql
SELECT
region,
domain_name,
object_type_name
FROM aws.customerprofiles.object_types_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>object_types_list_only</code> resource, see <a href="/providers/aws/customerprofiles/object_types/#permissions"><code>object_types</code></a>


