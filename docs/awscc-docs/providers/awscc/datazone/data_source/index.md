---
title: data_source
hide_title: false
hide_table_of_contents: false
keywords:
  - data_source
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
Gets an individual <code>data_source</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_source</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>data_source</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.datazone.data_source</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>asset_forms_input</code></td><td><code>array</code></td><td>The metadata forms that are to be attached to the assets that this data source works with.</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The timestamp of when the data source was created.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the data source.</td></tr>
<tr><td><code>domain_id</code></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain where the data source is created.</td></tr>
<tr><td><code>domain_identifier</code></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain where the data source is created.</td></tr>
<tr><td><code>enable_setting</code></td><td><code>string</code></td><td>Specifies whether the data source is enabled.</td></tr>
<tr><td><code>environment_id</code></td><td><code>string</code></td><td>The unique identifier of the Amazon DataZone environment to which the data source publishes assets.</td></tr>
<tr><td><code>environment_identifier</code></td><td><code>string</code></td><td>The unique identifier of the Amazon DataZone environment to which the data source publishes assets.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The unique identifier of the data source.</td></tr>
<tr><td><code>configuration</code></td><td><code>undefined</code></td><td>Configuration of the data source. It can be set to either glueRunConfiguration or redshiftRunConfiguration.</td></tr>
<tr><td><code>last_run_asset_count</code></td><td><code>number</code></td><td>The number of assets created by the data source during its last run.</td></tr>
<tr><td><code>last_run_at</code></td><td><code>string</code></td><td>The timestamp that specifies when the data source was last run.</td></tr>
<tr><td><code>last_run_status</code></td><td><code>string</code></td><td>The status of the last run of this data source.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the data source.</td></tr>
<tr><td><code>project_id</code></td><td><code>string</code></td><td>The ID of the Amazon DataZone project to which the data source is added.</td></tr>
<tr><td><code>project_identifier</code></td><td><code>string</code></td><td>The identifier of the Amazon DataZone project in which you want to add the data source.</td></tr>
<tr><td><code>publish_on_import</code></td><td><code>boolean</code></td><td>Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.</td></tr>
<tr><td><code>recommendation</code></td><td><code>object</code></td><td>Specifies whether the business name generation is to be enabled for this data source.</td></tr>
<tr><td><code>schedule</code></td><td><code>object</code></td><td>The schedule of the data source runs.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the data source.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of the data source.</td></tr>
<tr><td><code>updated_at</code></td><td><code>string</code></td><td>The timestamp of when this data source was updated.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>data_source</code> resource, the following permissions are required:

### Read
```json
datazone:GetDataSource
```

### Update
```json
datazone:UpdateDataSource,
datazone:GetDataSource,
datazone:DeleteDataSource
```

### Delete
```json
datazone:DeleteDataSource,
datazone:GetDataSource
```


## Example
```sql
SELECT
region,
asset_forms_input,
created_at,
description,
domain_id,
domain_identifier,
enable_setting,
environment_id,
environment_identifier,
id,
configuration,
last_run_asset_count,
last_run_at,
last_run_status,
name,
project_id,
project_identifier,
publish_on_import,
recommendation,
schedule,
status,
type,
updated_at
FROM awscc.datazone.data_source
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DomainId&gt;'
AND data__Identifier = '&lt;Id&gt;'
```
