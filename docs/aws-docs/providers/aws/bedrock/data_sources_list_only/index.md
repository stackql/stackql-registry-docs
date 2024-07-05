---
title: data_sources_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources_list_only
  - bedrock
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
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::DataSource Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.bedrock.data_sources_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="data_source_configuration" /></td><td><code>object</code></td><td>Specifies a raw data source location to ingest.</td></tr>
<tr><td><CopyableCode code="data_source_id" /></td><td><code>string</code></td><td>Identifier for a resource.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the Resource.</td></tr>
<tr><td><CopyableCode code="knowledge_base_id" /></td><td><code>string</code></td><td>The unique identifier of the knowledge base to which to add the data source.</td></tr>
<tr><td><CopyableCode code="data_source_status" /></td><td><code>string</code></td><td>The status of a data source.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the data source.</td></tr>
<tr><td><CopyableCode code="server_side_encryption_configuration" /></td><td><code>object</code></td><td>Contains details about the server-side encryption for the data source.</td></tr>
<tr><td><CopyableCode code="vector_ingestion_configuration" /></td><td><code>object</code></td><td>Details about how to chunk the documents in the data source. A chunk refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried.</td></tr>
<tr><td><CopyableCode code="data_deletion_policy" /></td><td><code>string</code></td><td>The deletion policy for the data source.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time at which the data source was created.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The time at which the knowledge base was last updated.</td></tr>
<tr><td><CopyableCode code="failure_reasons" /></td><td><code>array</code></td><td>The details of the failure reasons related to the data source.</td></tr>
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
knowledge_base_id,
data_source_id
FROM aws.bedrock.data_sources_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>data_sources_list_only</code> resource, see <a href="/providers/aws/bedrock/data_sources/#permissions"><code>data_sources</code></a>


