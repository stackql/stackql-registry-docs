---
title: namespaces_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces_list_only
  - redshiftserverless
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

Lists <code>namespaces</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/namespaces/"><code>namespaces</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>namespaces_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RedshiftServerless::Namespace Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshiftserverless.namespaces_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="namespace" /></td><td><code>object</code></td><td>Definition of Namespace resource.</td></tr>
<tr><td><CopyableCode code="namespace_name" /></td><td><code>string</code></td><td>A unique identifier for the namespace. You use this identifier to refer to the namespace for any subsequent namespace operations such as deleting or modifying. All alphabetical characters must be lower case. Namespace name should be unique for all namespaces within an AWS account.</td></tr>
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
Lists all <code>namespaces</code> in a region.
```sql
SELECT
region,
namespace_name
FROM aws.redshiftserverless.namespaces_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>namespaces_list_only</code> resource, see <a href="/providers/aws/redshiftserverless/namespaces/#permissions"><code>namespaces</code></a>

