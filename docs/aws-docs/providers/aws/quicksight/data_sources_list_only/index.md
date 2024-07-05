---
title: data_sources_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources_list_only
  - quicksight
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

Lists <code>data_sources</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/data_sources/"><code>data_sources</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_sources_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::DataSource Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.data_sources_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="alternate_data_source_parameters" /></td><td><code>array</code></td><td><p>A set of alternate data source parameters that you want to share for the credentials<br />stored with this data source. The credentials are applied in tandem with the data source<br />parameters when you copy a data source by using a create or update request. The API<br />operation compares the <code>DataSourceParameters</code> structure that's in the request<br />with the structures in the <code>AlternateDataSourceParameters</code> allow list. If the<br />structures are an exact match, the request is allowed to use the credentials from this<br />existing data source. If the <code>AlternateDataSourceParameters</code> list is null,<br />the <code>Credentials</code> originally used with this <code>DataSourceParameters</code><br />are automatically allowed.</p></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The Amazon Resource Name (ARN) of the data source.</p></td></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td><p>The time that this data source was created.</p></td></tr>
<tr><td><CopyableCode code="credentials" /></td><td><code>object</code></td><td><p>Data source credentials. This is a variant type structure. For this structure to be<br />valid, only one of the attributes can be non-null.</p></td></tr>
<tr><td><CopyableCode code="data_source_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_source_parameters" /></td><td><code>object</code></td><td><p>The parameters that Amazon QuickSight uses to connect to your underlying data source.<br />This is a variant type structure. For this structure to be valid, only one of the<br />attributes can be non-null.</p></td></tr>
<tr><td><CopyableCode code="error_info" /></td><td><code>object</code></td><td><p>Error information for the data source creation or update.</p></td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td><p>The last time that this data source was updated.</p></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="permissions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="ssl_properties" /></td><td><code>object</code></td><td><p>Secure Socket Layer (SSL) properties that apply when Amazon QuickSight connects to your<br />underlying data source.</p></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_connection_properties" /></td><td><code>object</code></td><td><p>VPC connection properties.</p></td></tr>
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
Lists all <code>data_sources</code> in a region.
```sql
SELECT
region,
aws_account_id,
data_source_id
FROM aws.quicksight.data_sources_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>data_sources_list_only</code> resource, see <a href="/providers/aws/quicksight/data_sources/#permissions"><code>data_sources</code></a>


