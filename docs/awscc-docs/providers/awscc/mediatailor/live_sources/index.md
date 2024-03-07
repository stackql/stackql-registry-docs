---
title: live_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - live_sources
  - mediatailor
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>live_sources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>live_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>live_sources</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.mediatailor.live_sources</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>live_source_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source_location_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>live_sources</code> resource, the following permissions are required:

### Create
```json
mediatailor:CreateLiveSource,
mediatailor:DescribeLiveSource,
mediatailor:TagResource
```

### List
```json
mediatailor:ListLiveSources
```


## Example
```sql
SELECT
region,
live_source_name,
source_location_name
FROM awscc.mediatailor.live_sources
WHERE region = 'us-east-1'
```
