---
title: data_sources_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources_list_only
  - datazone
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
<tr><td><b>Description</b></td><td>A data source is used to import technical metadata of assets (data) from the source databases or data warehouses into Amazon DataZone.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.data_sources_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="asset_forms_input" /></td><td><code>array</code></td><td>The metadata forms that are to be attached to the assets that this data source works with.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The timestamp of when the data source was created.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the data source.</td></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain where the data source is created.</td></tr>
<tr><td><CopyableCode code="domain_identifier" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain where the data source is created.</td></tr>
<tr><td><CopyableCode code="enable_setting" /></td><td><code>string</code></td><td>Specifies whether the data source is enabled.</td></tr>
<tr><td><CopyableCode code="environment_id" /></td><td><code>string</code></td><td>The unique identifier of the Amazon DataZone environment to which the data source publishes assets.</td></tr>
<tr><td><CopyableCode code="environment_identifier" /></td><td><code>string</code></td><td>The unique identifier of the Amazon DataZone environment to which the data source publishes assets.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique identifier of the data source.</td></tr>
<tr><td><CopyableCode code="configuration" /></td><td><code>undefined</code></td><td>Configuration of the data source. It can be set to either glueRunConfiguration or redshiftRunConfiguration.</td></tr>
<tr><td><CopyableCode code="last_run_asset_count" /></td><td><code>number</code></td><td>The number of assets created by the data source during its last run.</td></tr>
<tr><td><CopyableCode code="last_run_at" /></td><td><code>string</code></td><td>The timestamp that specifies when the data source was last run.</td></tr>
<tr><td><CopyableCode code="last_run_status" /></td><td><code>string</code></td><td>The status of the last run of this data source.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the data source.</td></tr>
<tr><td><CopyableCode code="project_id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone project to which the data source is added.</td></tr>
<tr><td><CopyableCode code="project_identifier" /></td><td><code>string</code></td><td>The identifier of the Amazon DataZone project in which you want to add the data source.</td></tr>
<tr><td><CopyableCode code="publish_on_import" /></td><td><code>boolean</code></td><td>Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.</td></tr>
<tr><td><CopyableCode code="recommendation" /></td><td><code>object</code></td><td>Specifies whether the business name generation is to be enabled for this data source.</td></tr>
<tr><td><CopyableCode code="schedule" /></td><td><code>object</code></td><td>The schedule of the data source runs.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the data source.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the data source.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The timestamp of when this data source was updated.</td></tr>
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
domain_id,
id
FROM aws.datazone.data_sources_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>data_sources_list_only</code> resource, see <a href="/providers/aws/datazone/data_sources/#permissions"><code>data_sources</code></a>


