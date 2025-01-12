---
title: data_accessors_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - data_accessors_list_only
  - qbusiness
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

Lists <code>data_accessors</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/data_accessors/"><code>data_accessors</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_accessors_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::QBusiness::DataAccessor Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.qbusiness.data_accessors_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_accessor_id" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>data_accessors</code> in a region.
```sql
SELECT
region,
application_id,
data_accessor_id
FROM aws.qbusiness.data_accessors_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>data_accessors_list_only</code> resource, see <a href="/providers/aws/qbusiness/data_accessors/#permissions"><code>data_accessors</code></a>
